#Get the data to the dataset from a GCS path

from google.cloud import automl

# TODO(developer): Uncomment and set the following variables
#project_id = ""
#dataset_id = ""
path = "gs://hhg_nlp_project/hhg_LSVC_train.csv"

client = automl.AutoMlClient()
dataset_full_id = client.dataset_path(
    project_id, "us-central1", dataset_id
)

input_uris = path.split(",")
gcs_source = automl.types.GcsSource(input_uris=input_uris)
input_config = automl.types.InputConfig(gcs_source=gcs_source)
response = client.import_data(dataset_full_id, input_config)

print("Processing import...")
print("Data imported. {}".format(response.result()))
