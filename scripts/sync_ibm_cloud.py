
from src.io.file_writer import FileWriter

fw = FileWriter()

path_prefix = "pa_raw_data"
bucket_name = "pa-raw-data"

fw.move_to_cloud(path_prefix, bucket_name)
