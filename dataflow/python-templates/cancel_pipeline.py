import logging, re,os
from googleapiclient.discovery import build
from oauth2client.client import GoogleCredentials

def retrieve_job_id():
  #Fill accordingly
  project = 'my-project-id'
  job_prefix = "<job-name>"
  location = 'us-central1'

  logging.info("Looking for jobs with prefix {} in region {}...".format(job_prefix, location))

  try:
    credentials = GoogleCredentials.get_application_default()
    dataflow = build('dataflow', 'v1b3', credentials=credentials)

    result = dataflow.projects().locations().jobs().list(
      projectId=project,
      location=location,
    ).execute()

    job_id = "none"

    for job in result['jobs']:
      if re.findall(r'' + re.escape(job_prefix) + '', job['name']):
        job_id = job['id']
        break

    logging.info("Job ID: {}".format(job_id))
    return job_id

  except Exception as e:
    logging.info("Error retrieving Job ID")
    raise KeyError(e)


os.system('gcloud dataflow jobs cancel {}'.format(retrieve_job_id()))
