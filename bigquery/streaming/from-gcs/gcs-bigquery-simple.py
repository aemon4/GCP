from apache_beam.options.pipeline_options import PipelineOptions
from google.cloud import pubsub_v1
from google.cloud import bigquery
import apache_beam as beam
import logging
import argparse
import datetime

#Fill accordingly, we are using a table-id sport_simple for future reference
schema = 'ex1:STRING, ex2:String, ex3:Int'
table= '<dataset_id>.sport_simple'
gcs_file = "gs://<MyBucket>/sport-data.txt"

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

class Transform_text(beam.DoFn):
  def process(self,element):
    element = element.strip()
    splitted = element.split(',')
    full_splitted = splitted[0].split(' ')
    #TODO transform incoming gcs data into bq writable
    yield {
      "Brand": full_splitted[0],
      "Equipment": full_splitted[1],
      "Cost": int(splitted[1].strip('$')),
    }

def main(argv=None):

  parser = argparse.ArgumentParser()
  parser.add_argument("--input_file", default=gcs_file)
  parser.add_argument("--output_table", default=table)
  args, beam_args = parser.parse_known_args(argv)
#save_main_session needs to be set to true in order to avoid datetime not found issues
  p = beam.Pipeline(argv=beam_args,options=PipelineOptions(save_main_session=True,
region='us-central1'))#, service_account_email='email'))

  (p
      | 'ReadData' >> beam.io.textio.ReadFromText(args.input_file) #AFAIK this creates a PCollection of lines
      | "Transform text" >> beam.ParDo(Transform_text())
      | 'WriteToBigQuery' >> beam.io.WriteToBigQuery(args.output_table, schema=schema, write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND)
  )
  result = p.run()
  result.wait_until_finish()

if __name__ == '__main__':
  logger = logging.getLogger().setLevel(logging.INFO)
  main()
