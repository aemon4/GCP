from apache_beam.options.pipeline_options import PipelineOptions
from google.cloud import pubsub_v1
from google.cloud import bigquery
import apache_beam as beam
import logging
import argparse
import datetime

# Fill accordingly, we are using a table-id sport_simple for future reference
schema = 'ex1:STRING, ex2:String, ex3:Int'
table= '<dataset_id>.sport_simple'
gcs_file = "gs://<MyBucket>/sport-data.txt"

# We need to define a transformation step to clean the incoming data
# Given that the data has the format 'Brand Equipment, cost$' we use the following transformation: 
class Transform_text(beam.DoFn):
  def process(self,element):
    element = element.strip()
    splitted = element.split(',')
    full_splitted = splitted[0].split(' ')
    # Transform incoming gcs data into bq writable, meaning a dictionary
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
  # Uncomment the service account email parameter if you wish to use a custom service account
  p = beam.Pipeline(argv=beam_args,options=PipelineOptions(save_main_session=True,
region='us-central1'))#, service_account_email='email'))

  (p
      | 'ReadData' >> beam.io.textio.ReadFromText(args.input_file) # This creates a PCollection of lines
      | "Transform text" >> beam.ParDo(Transform_text()) # This transform the lines into BQ writtable
      | 'WriteToBigQuery' >> beam.io.WriteToBigQuery(args.output_table, schema=schema, write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND)
  ) # This writes the data to BQ

  result = p.run()
  result.wait_until_finish()

if __name__ == '__main__':
  logger = logging.getLogger().setLevel(logging.INFO)
  main()
