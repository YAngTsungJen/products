products = []

while True:
	name = input("請輸入商品名稱： ")
	if name == "q":
		break
	price = input("請輸入商品價格： ")
	p = []
	p.append(name)
	p.append(price) #小清單7,8,9 p = [name , price]
	products.append(p) #products.append(name ,price )
print(products)

for p in products:
	print(p[0], "的價格是", p[1])
#for p in products:
	# print(p) #從大清單中拿出小清單
with open("products.csv", "w") as f:
	for p in products:
		f.write(p[0] + "," + p[1] + "\n")