This example guides you through the official GCP documentation on natural-language. It complements the [public tutorial][1].
The initial steps are the same and it adds how to perform simple curl and [batch predictions][2].

1. Create a dataset 
- Run `datasets/create_dataset_tutorial.py`
2. Fill it with the HappyDB data. 
- Run `datasets/get_dataset_data_tutorial.py`
3. Train a model and deploy it
- Run `training/train_tutorial.py`
4. Submit a simple prediciton using predictions/request.json
- In Linux/Cloud Shell 
```
curl -X POST \
-H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
-H "Content-Type: application/json; charset=utf-8" \
-d @request.json \
https://automl.googleapis.com/v1/projects/project-id/locations/location-id/models/model-id:predict
```
You will receive predictions/response.json as a result. 
5. Submit batch predictions
- You need to create the csv file in GCS that has the GCS paths to each file/text to predict. The texts to predict are `first_text.txt` and `second_text.txt` and the csv file is `predict.csv`, look carefully how it is constructed in order to reproduce it for future cases.
- Afterwards you can submit another curl request like
```
curl -X POST \
-H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
-H "Content-Type: application/json; charset=utf-8" \
-d @batch_predict_tutorial.json \
https://automl.googleapis.com/v1/projects/project-id/locations/location-id/models/model-id:batchPredict
```
Or use the `predictions/batch_predict_tutorial.py` file.

[1]: https://cloud.google.com/natural-language/automl/docs/tutorial
[2]: https://cloud.google.com/natural-language/automl/docs/predict#batch_prediction
