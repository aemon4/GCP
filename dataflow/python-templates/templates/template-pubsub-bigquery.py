from apache_beam.options.pipeline_options import PipelineOptions
from google.cloud import pubsub_v1
from google.cloud import bigquery
import apache_beam as beam
import logging
import argparse
import datetime

#TODO Fill this values in order to have them by default
#Note that the table in BQ needs to have the column names message_body and publish_time

Table = 'projectid:datasetid.tableid'
schema = 'ex1:STRING, ex2:TIMESTAMP'
TOPIC = "projects/<projectid>/topics/<topicname>"

class AddTimestamps(beam.DoFn):
    def process(self, element, publish_time=beam.DoFn.TimestampParam):
        """Processes each incoming element by extracting the Pub/Sub
        message and its publish timestamp into a dictionary. `publish_time`
        defaults to the publish timestamp returned by the Pub/Sub server. It
        is bound to each element by Beam at runtime.
        """

        yield {
            "message_body": element.decode("utf-8"),
            "publish_time": datetime.datetime.utcfromtimestamp(
                float(publish_time)
            ).strftime("%Y-%m-%d %H:%M:%S.%f"),
        }


def main(argv=None):

    parser = argparse.ArgumentParser()
    parser.add_argument("--input_topic", default=TOPIC)
    parser.add_argument("--output_table", default=Table)
    args, beam_args = parser.parse_known_args(argv)
#save_main_session needs to be set to true due to modules being used among the code (mostly datetime)
#Uncomment the service account email to specify a custom service account
    p = beam.Pipeline(argv=beam_args,options=PipelineOptions(save_main_session=True,
region='us-central1'))#, service_account_email='email'))

    (p
        | 'ReadData' >> beam.io.ReadFromPubSub(topic=args.input_topic).with_output_types(bytes)
        | "Add timestamps to messages" >> beam.ParDo(AddTimestamps())
        | 'WriteToBigQuery' >> beam.io.WriteToBigQuery(args.output_table, schema=schema, write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND)
    )
    result = p.run()
    result.wait_until_finish(duration=3000)
    result.cancel()   # Cancel the streaming pipeline after a while to avoid consuming more resources

if __name__ == '__main__':
    logger = logging.getLogger().setLevel(logging.INFO)
    main()
