#TODO fill job-name and gcs location accordingly
#Uncomment and fill the parameters should you want to use your own

gcloud dataflow jobs run <job-name> \
        --gcs-location "gs://<MYBUCKET>/dataflow/templates/mytemplate" 
   #     --parameters input_topic="", output_table=""
