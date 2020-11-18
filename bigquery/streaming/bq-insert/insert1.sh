echo `date`

#TODO change dataset_id.table_id accordingly
bq insert -i -s dataset_id.table_id data.json

echo `date`
