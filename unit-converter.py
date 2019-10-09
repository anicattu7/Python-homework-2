print("Welcome to the unit converter. Here you can convert your kilometer(km) to miles(mi)")

while True:
    km = float(input("Enter your unit to convert in kilometers: "))
    mi = km * 0.62137119
    print("The miles conversion of "+str(km)+" kilometer(s) to mile(s) are: "+str(mi))
    cont = input("Do you wish to continue with unit conversion? (y/n): ").upper()

    if cont == "Y":
        continue
    elif cont == "N":
        print("See you later")
        break
    else:
        print("Wrong selection..exiting..")
        break





