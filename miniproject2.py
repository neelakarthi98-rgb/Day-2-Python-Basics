inventory = {"laptop": 10, "mouse": 25, "keyboard": 15}
print("initial inventory:",inventory)

#adding the monitor count

inventory["monitor"]=5
print("Inventory after adding monitor:",inventory)

#updating the laptop stock

inventory["laptop"]-=2
print("inventory after updating the laptop stock:",inventory)
#check the keyboard stock using if

stock_count=inventory.get("keyboard")
if stock_count is  not None and stock_count > 0:
    print(f" 'keyboard' is in stock with a count of: {stock_count}")
else:
    print(" 'keyboard' is not in stock or does not exist.")

#check the mouse stock using if

stock_count=inventory.get("mouse")
if stock_count is not None and stock_count>0:
    print(f" 'mouse' is in stock with a count of :{stock_count}")
else:
    print(" 'mouse' is not in stock or does not exist.")

for item,stock in inventory.items():
    print(f"{item}:{stock}") 
