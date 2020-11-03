#This code performs batch prediction on a deployed model using a csv file in GCS

from google.cloud import automl

# TODO(developer): Uncomment and set the following variables
#project_id = ""
#model_id = ""
#input_uri = "gs://MYBUCKET/natural-language/predict.csv"
#output_uri = "gs://MYBUCKET/natural-language"

prediction_client = automl.PredictionServiceClient()
model_full_id = prediction_client.model_path(
    project_id, "us-central1", model_id
)

gcs_source = automl.types.GcsSource(input_uris=[input_uri])

input_config = automl.types.BatchPredictInputConfig(gcs_source=gcs_source)
gcs_destination = automl.types.GcsDestination(output_uri_prefix=output_uri)
output_config = automl.types.BatchPredictOutputConfig(
    gcs_destination=gcs_destination
)

response = prediction_client.batch_predict(
    model_full_id, input_config, output_config
)

print("Waiting for operation to complete...")
print(
    "Batch Prediction results saved to Cloud Storage bucket. {}".format(
        response.result()
    )
)
