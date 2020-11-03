#We create a model with the base model provided by Google by providing the dataset were to train from

from google.cloud import automl

# TODO(developer): Uncomment and set the following variables
#project_id = ""
#dataset_id = ""
#display_name =""

client = automl.AutoMlClient()
project_location = client.location_path(project_id, "us-central1")

# Leave model unset to use the default base model provided by Google
metadata = automl.types.TextClassificationModelMetadata()
model = automl.types.Model(
    display_name=display_name,
    dataset_id=dataset_id,
    text_classification_model_metadata=metadata,
)

response = client.create_model(project_location, model)

print(u"Training operation name: {}".format(response.operation.name))
print("Training started...")
