#Fill accordingly with your values

PROJECT="MYPROJECT-ID"
BUCKET="MYBUCKET"
TEMPLATE_NAME="TRIAL"

#create the template
python3 -m templates.template-pubsub-bigquery \
  --runner DataflowRunner \
  --project $PROJECT \
  --staging_location gs://$BUCKET/staging \
  --temp_location gs://$BUCKET/temp \
  --template_location gs://$BUCKET/templates/$TEMPLATE_NAME \
  --streaming
