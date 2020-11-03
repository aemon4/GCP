# This code loads pratitioned data from a csv file in GCS to a table in BigQuery

from google.cloud import bigquery

client = bigquery.Client()

# TODO(developer): 
#Set table_id to the ID of the table to create.
table_id = "project:dataset.table"

#Set the proper schema of your table
job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("post_abbr", "STRING"),
        bigquery.SchemaField("hour", "TIMESTAMP"),
    ],
    skip_leading_rows=1,
    time_partitioning=bigquery.TimePartitioning(
        type_=bigquery.TimePartitioningType.HOUR,
        field="hour",  # Name of the column to use for partitioning.
        expiration_ms=7776000000,  # 90 days.
    ),
)
#Set the path to the bucket where the data is stored
uri = "gs://MYBUCKET/partitioned.csv"

load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
)  

load_job.result()  

table = client.get_table(table_id)
print("Loaded {} rows to table {}".format(table.num_rows, table_id))
