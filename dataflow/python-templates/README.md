A tutorial on how to consturct a template pipeline using python that gets Pub/Sub data and writes it to BigQuery.

First we construct the main code to perform this task.
The code needs to get the messages from PubSub, transform them into what we want to insert in BigQuery and then write it to BigQuery. In essence, a three step process.

**1. Get the data from Pub/Sub**

This is directly done by `'ReadData' >> beam.io.ReadFromPubSub(topic).with_output_types(bytes)` \
Important to note that this will return the messages as a `String` which is not a valid insert type to BigQuery, needs to be a dictionary.

**2. Transform data**


The main purpose is to get a dictionary where each entry has to correspond with a column (field) name in BigQuery. \
What we do in our simple template is to get the content of the message and add the timestamp at which it was delivered. \
The important notes to consider is that the class needs to return a `yield` which basically is a return for each element that enters which allows for a good parallelization of tasks. 


**3. Write data to BigQuery**

This is done by the line `beam.io.WriteToBigQuery(table, schema, write_disposition)`. \
Bear in mind that the table needs to be created beforehand and the table schema needs to match the dictionary schema delivered in step 2. 
In our case, that means `"message_body":STRING , "publish_time": TIMESTAMP`


