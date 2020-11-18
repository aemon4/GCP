The overall structure we will follow is:

0. Create the dummy data we will use in steps 1-3.
1. Create a simple pipeline that streams data from GCS to BigQuery. The data will need to be transformed and cleaned to be inserted in BigQuery.
2. Create a more complex pipeline that writes to a partitioned table (by day or hour).
3. Create a complex pipeline that writes into several tables. A first approach could be a full data table (partitioned by day, etc) and a summary of the data table with some information for the overall day.

**0. Create dummy data**

We start creating the dummy data. Of course any "dummy" data will work, but we will try to code a more interesting dummy data which can serve of inspiration for particular "dummy" data creations moving forward. For that we have two functions (`create_mockfile()` and `upload_blob()` that you can see in `sport_functions.py`. 

Basically we will create sport equipment data with `create_mockfile()` and upload it to GCS with `upload_blob()`. To sum up, each piece of equipment belongs to a certain brand and has a cost within some boundaries depending on the piece of equipment. The sport brand is set at random, the piece of equipment follows a normal distribution where we set the most common items around the expected value. Finally, we have a dictionary of costs detailing the range of prices for each particular item. We write the data as *Brand Equipment-piece, cost$* This is intended to force us to clean the data within the pipeline. 

Clearly we could add further layers of complexity, e.g. cost depending on brand, both cost and brands following another probability distribution, etc. For the time being we will consider this data to be good enough for the purpose of the exercise. 

**1. Create a simple pipeline**

The three steps are clear,
I. Read the data from GCS
II Clean the data and transform it into BigQuery writtable
III. Write the data to BigQuery

This is done in `gcs-bigquery-simple.py`. To check it works create a table with the needed schema and run the pipeline by running `job_run.sh`. 
