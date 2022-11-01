########################################################################
# CONTROL FLOW WITH IF/ELSE STATEMENTS AND CONDITIONAL OPERATORS
########################################################################

#print("Welcome to the rollercoaster!")
#height = int(input("What is your height in cm?"))

#if height > 120:
#    print("You can ride the rollercoaster!")

#else:
#    print("Sorry, you have to grow taler before you can ride.")

########################################################################
# NESTED IF STATEMENTS AND ELIF STATEMENTS
########################################################################

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?"))

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age?"))

#     if age < 12:
#         print("Please pay €5")

#     elif age <= 18:
#         print("Please pay €7")

#     else:
#         print("Please pay €12")
# else:
#     print("Sorry, you have to grow taler before you can ride.")

########################################################################
# LOGICAL OPERATORS
########################################################################

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))

    if age < 12:
        bill = 5
        print("¨Child tickets are €5")

    elif age <= 18:
        bill = 7
        print("Youth tickets are €7")
    elif age >=45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us")

    else:
        bill = 12
        print("Adult tickets are €12")

    want_photo = input("Do your want a photo taken? Y or N.")
    if want_photo == "Y":
        #Add €3 to their bill
        bill += 3
    
    print(f"Your final bill is €{bill}")

else:
    print("Sorry, you have to grow taler before you can ride.")


