# This is an example of how to create a dataset with GCP official documentation

from google.cloud import automl

# TODO(developer): Uncomment and set the following variables
#project_id = ""
#display_name = ""

client = automl.AutoMlClient()
project_location = client.location_path(project_id, "us-central1")
# Specify the classification type
# Types:
# MultiLabel: Multiple labels are allowed for one example.
# MultiClass: At most one label is allowed per example.
metadata = automl.types.TextClassificationDatasetMetadata(
    classification_type=automl.enums.ClassificationType.MULTICLASS
)
dataset = automl.types.Dataset(
    display_name=display_name,
    text_classification_dataset_metadata=metadata,
)

response = client.create_dataset(project_location, dataset)
created_dataset = response.result()

# Display the dataset information
print("Dataset name: {}".format(created_dataset.name))
print("Dataset id: {}".format(created_dataset.name.split("/")[-1]))
