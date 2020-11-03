echo `date`

#TODO change dataset_id.table_id accordingly
bq insert -i -s testing.inserting_shell data.json

echo `date`
