print("Welcome to the tip calculator")
bill = float(input("What was the total bill? €"))
percent = float(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

subtotal= bill * percent / 100 + bill
total = subtotal / people
rounded = round(total, 2)
totall = "{:.2f}".format(rounded)
print(f"Total after adding tip is {round(subtotal,2)}")
print(f"Each person should pay {totall}")