import os
import cv2
import numpy as np
from PIL import Image
from pyzbar.pyzbar import decode, ZBarSymbol

# フォルダのパスを指定
folder_path = 'output\\090d5b46-1750-4360-8367-2e98a64288e7'
output_path = 'sample\\mtfuji_qr.jpg'

# QRコード画像のファイルを取得
qr_files = [f for f in os.listdir(folder_path) if f.endswith('.png') or f.endswith('.jpg')]
print(qr_files)

# データを格納するリスト
binary_data_list = []

# 各QRコード画像を処理
for qr_file in qr_files:
    qr_path = os.path.join(folder_path, qr_file)
    
    # QRコード画像を読み込み
    print(qr_path)
    qr_image = cv2.imread(qr_path)
    
    # QRコードをデコード
    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(qr_image)
    # value = decode(qr_image, symbols=[ZBarSymbol.QRCODE])
    if data:
        # バイナリデータとして格納
        binary_data_list.append(data.encode())

    print(data.encode())

# すべてのデータを結合
combined_data = b''.join(binary_data_list)

# バイナリデータをJPEGファイルとして保存
with open(output_path, 'wb') as f:
    f.write(combined_data)

print(f'Successfully saved combined image to {output_path}')
