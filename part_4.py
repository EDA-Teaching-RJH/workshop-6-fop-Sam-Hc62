travel_log = []
while True:
    try:
        X = int(input("Sensor Reading (Slope Angle):"))
        if X >45:
            print("CRITICAL TILT! HALTING.")
            print("mission terminated")
            break
        else:
            travel_log.append(X)
            print("Path Stable. Moving forward.")
            print(travel_log)
            continue
    except ValueError:
        print("sensor glitch")
    else:
        break
print(travel_log)



