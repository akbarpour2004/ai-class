age = int(input("سن: "))
day = input("روز هفته: ").strip()

if age < 5:
  price = 0
  print("ورود رایگان")
elif 5 <= age <= 12:
  price = 50000
elif age >= 60:
  price = 60000
else:
  price = 100000

if day == "سه شنبه":
  price = price * 0.8  

if age >= 5:
  print(f"قیمت بلیط : {int(price)} تومان")