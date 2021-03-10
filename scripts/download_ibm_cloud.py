
from src.io.file_reader import FileReader


fr = FileReader()

path_prefix = "pa_raw_data"
bucket_name = "pa-raw-data"
dest_folder = '../data'

fr.download_all_files(bucket_name, dest_folder)

#{'Key': '2015_12_06/pa_raw_data_2020_09_26_08_17_50.json', 'LastModified': datetime.datetime(2020, 9, 26, 7, 5, 22, 399000, tzinfo=tzutc()), 'ETag': '"891f4c86abf8ece8d64310093cd139ea"', 'Size': 34683, 'StorageClass': 'STANDARD', 'Owner': {'DisplayName': 'c5697c18-69a5-4946-a54b-4f214086882a', 'ID': 'c5697c18-69a5-4946-a54b-4f214086882a'}}

# folder_name = "2015_12_06"
# file_name = "pa_raw_data_2020_09_26_08_17_50.json"
# fr.download_from_cloud(bucket_name=bucket_name, folder_name=folder_name, file_name=file_name, dest_folder= dest_folder)