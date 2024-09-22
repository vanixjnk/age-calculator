from tqdm import tqdm
import time

age = int(input("Nhập số tuổi của bạn: "))
for i in tqdm(range(50)):
    time.sleep(0.05)

print("Tuổi của bạn là: ", age)
