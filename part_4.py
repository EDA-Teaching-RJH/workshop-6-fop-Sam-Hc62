travel_log = []
while True:
    try:
        X = int(input("Sensor Reading (Slope Angle):"))
        if X >45:
            print("CRITICAL TILT! HALTING.")
            print("mission terminated")
            print("total steps taken:", len(travel_log))
            break
        else:
            travel_log.append(X)
            print("Path Stable. Moving forward.")
            continue
    except ValueError:
        print("sensor glitch")
    else:
        print("total steps taken", len(travel_log))
        break
print(travel_log)



