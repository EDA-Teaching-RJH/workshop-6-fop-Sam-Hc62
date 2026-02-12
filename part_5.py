status = {
    "Power": 100, "Samples": 0
    }
inventory = []
while True:
    print("""    1 - dig for sample
    2 - report status
    3 - emergency stop""")
    y = int(input("chose an option"))
    if y == 1:
        inventory.append(input("sample name?"))
        status["Power"] = status["Power"]-10
    elif y == 2:
        print(status, inventory)
    elif y == 3:
        break
    else:
        print("invalid entry")

        

    
