try:
    speed = int(input("Enter motor speed"))
    if 0<=speed<=100:
        print("speed set to:", speed)
    else:
        print("Invalid speed")
except ValueError:
    print("Error: Corrupted Signal. Maintaining current speed.")

def get_coordinate():
    while True:
        try:
            X = int(input("x coordinate"))
            if -100< X <100:
                break
            else:
                print("coordinate out of range")
                continue
        except ValueError:
            print("invalid coordinate")
        else:
            break
get_coordinate()



