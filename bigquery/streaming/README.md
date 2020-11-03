The purpose of this section is to see a few examples of how to perform streaming inserts into BigQuery.

**1. bq insert**
---
We start with streaming inserts using `bq insert` from CMD, either on a VM or in the Cloud Shell.
For this section the steps are:

**1.1. Create the table you wish to insert data to.**
In our example we use the schema`schema_inserts.json` , and create the table by running `create_table.sh`.

**1.2. Create a new-line delimited json file with the data you wish to insert.**
In our example the data is in `data.json`. 

**1.3. Perform simple streaming inserts**
We test the streaming inserts by running `insert1.sh` which inserts the data in `data.json` into our table using the `bq` command

**1.4. Perform massive streaming inserts**
We can test the performance of massive inserts by using the previous data as a basis and increasing the amount of times in needs to be inserted. This is done in     `test_massive_inserts.sh`. Feel free to change the number of times (1000) that you insert the same data into the table. The code also saves the start and end time of each insert in a logs folder in order to monitor the "speed" of the inserts. Remember that the data is inserted into the streaming buffer, and then slowly introduced in the table itself. Nevertheless, the streaming buffer is queryable. 
