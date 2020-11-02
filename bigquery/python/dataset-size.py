#This code is created to extract information from your datasets. 
#The main purpose is to extract the overall size (you need to sum the table sizes)

from google.cloud import bigquery

client = bigquery.Client()
datasets = list(client.list_datasets()) 

if datasets:
    print("BigQuery info in project {}:".format(client.project))
    for dataset in datasets:
        size = 0
        num_tables = 0
        print("Dataset \t{}".format(dataset.dataset_id))
        tables = client.list_tables(dataset.dataset_id)
        print("Tables contained in '{}':".format(dataset.dataset_id))
        for table in tables:
            #Uncomment the following lines to get the table name and size for each table
            #print("{}.{}.{}".format(table.project, table.dataset_id, table.table_id))
            table2 = client.get_table(table.dataset_id+"."+table.table_id)
            #print("Size{}".format(table2.num_bytes))
            size+=table2.num_bytes
            num_tables+=1
        print("Total size of dataset {} bytes".format(size))
        print("Total number of tables {} \n".format(num_tables))

else:
    print("{} project does not contain any datasets.".format(project))



