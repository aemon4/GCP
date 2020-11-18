import random as rand
from google.cloud import storage

def create_mockfile(num=1000,filename="sport-data.txt",bucket_name="testing",brands=None,equipments=None,costs=None):
  if not brands:
    brands = ["Adidas","Nike","Puma","Reebok","FILA"]
  if not equipments:
    equipments = ["Wristband","Leggings","Tracksuit","Shoes","Shirt","Socks","Hoodie","Headband"]
  if not costs:
    costs = {0:[1,9],1:[4,30],2:[9,50],3:[15,120],4:[6,40],5:[2,5],6:[15,80],7:[1,9]} 
  
  for i in range(0,num):
    brand = brands[rand.randint(0,4)]
    equipment_num = int(rand.gauss(0.35,0.20)*10)
    if equipment_num > 7:
      equipment_num = 7
    if equipment_num < 0:
      equipment_num = 0
    cost = rand.randint(costs[equipment_num][0],costs[equipment_num][1])
    equipment = equipments[equipment_num]

    #Write a csv file with lines brand,equipment,cost into GCS
    f = open("sport-data.txt", "a")
    line = brand+' '+equipment+','+str(cost)+'$\n'
    f.write(line)
    f.close()

  upload_blob(bucket_name,"sport-data.txt",filename)

  return 1


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # bucket_name = "your-bucket-name"
    # source_file_name = "local/path/to/file"
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )

