import qrcode
import base64
import uuid
import os

def split_binary_data(binary_data, chunk_size=256):
    # Calculate the number of full chunks
    num_full_chunks = len(binary_data) // chunk_size
    # Calculate the size of the remaining part
    remainder = len(binary_data) % chunk_size

    # Create a list to hold the chunks
    chunks = []

    # Append the full chunks to the list
    for i in range(num_full_chunks):
        chunks.append(binary_data[i*chunk_size : (i+1)*chunk_size])

    # Append the remaining part to the list
    if remainder > 0:
        chunks.append(binary_data[-remainder:])

    return chunks

file_path = "sample\MtFuji.jpg"

with open(file_path,mode="rb") as f:
    data = f.read()


binary_chunks = split_binary_data(data)
dirname = "output/"+str(uuid.uuid4())
os.mkdir(dirname)
data_length = len(binary_chunks)

for i in range(data_length):
    # encoded_data = base64.b64encode(binary_chunks[i]).decode('utf-8')
    # print(encoded_data)
    code = qrcode.make(binary_chunks[i],error_correction=qrcode.constants.ERROR_CORRECT_L)
    code.save(f"{dirname.zfill(len(str()))}/{str(i+1).zfill(len(str(data_length)))}.png")
    print(len(binary_chunks[i]))

