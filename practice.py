import os # operating system  模組

#讀取檔案
products = []
if os.path.isfile('products.csv'):#檢查檔案
	print("ya,找到檔案了")
	with open("products.csv", "r", encoding = 'utf-8') as f :
		for line in f:
			if "商品,價格" in line:
				continue#繼續（通常都是寫在迴圈中很高的位置),跳到下一回,89行就不執行, continue 和break一樣只能寫在迴圈裡
				#break則是直接跳出迴圈
			name, price, = line.strip().split(",")
			products.append([name, price])
	print(products)
else:
	print("找不到檔案了...")

# 讓使用者輸入
while True:
    name = input("請輸入商品名稱：")
    if name == "q":
        break
    price = input("請輸入商品價格：")
    products.append([name, price])
# 印出所有購買紀錄
for p in products:
	print(p[0], "的價格是：", p[1])

# 寫入檔案
with open("products.csv", "w", encoding = "utf-8") as f:
	f.write("商品,價格\n")
	for p in products:
		f.write(p[0] + "," + p[1] + "\n" )