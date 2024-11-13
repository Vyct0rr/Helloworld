asking_temperature = float(input("What is the temperature today?: "))

if asking_temperature > 30:
    print(" It's a hot day, Drink a lot of water. ")

elif asking_temperature < 10:
    print(" It's a cold day ")

else:
    print(" It's neither hot nor cold ")