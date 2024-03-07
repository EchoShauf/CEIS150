count =0
name = input("What is your full name: ")
temperature = float(input("What is your favorite temperature: "))
temperature_list = [69.0, 71.0, 84.5, 91.0, 67.4, 81.2, 84.6, 58.8, 79.3, 101.2]
for i in temperature_list:
    if i>temperature:
        count = count+1
print("Hello",name,"your favorite temperature is ",temperature)
print("There are ",count,"temperatures greater than your favorite temperature")
