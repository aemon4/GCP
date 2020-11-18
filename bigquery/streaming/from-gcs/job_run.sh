#Fill accordingly
PROJECT="<myproject-id>"
BUCKET="<MyBucket>/dataflow"

#run the job
python3 -m gcs-bigquery-simple \
  --runner DataflowRunner \
  --project $PROJECT \
  --staging_location gs://$BUCKET/staging \
  --temp_location gs://$BUCKET/temp \
  --streaming
