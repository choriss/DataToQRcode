import pyqrcode
import base64
import uuid
import os

file_path = "sample\MtFuji.jpg"

with open(file_path,mode="rb") as f:
    data = f.read()

chunk_size = 954 #max
binary_chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
dirname = "output/"+str(uuid.uuid4())
os.mkdir(dirname)
data_length = len(binary_chunks)

for i in range(data_length):
    encoded_data = base64.b64encode(binary_chunks[i]).decode('utf-8')
    # print(encoded_data)
    code = pyqrcode.create(encoded_data)
    code.png(f"{dirname}/{i+1}of{data_length}.png", scale=5, module_color=[0, 0, 0, 128], background=[255, 255, 255])
    print(f"{i+1}of{data_length}")

