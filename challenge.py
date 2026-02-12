command_batch = [
    "MOVE 10",
    "TURN LEFT",
    "MOVE 5",
    "MOVE five",    # Corrupted: 'five' is text, not a number
    "DIG",
    "MOVE 20",
    "XÆA-12",       # Corrupted: Unknown command
    "RETURN",
    "MOVE 15"
]
rover_state = {"x": 0, "y": 0, "samples": 0}
for items in command_batch:
    split_command = items.split()
    if split_command[0] == "MOVE":
        try: 
            x=int(split_command[1])
            rover_state["y"]= rover_state["y"]+ x
        except ValueError:
            print("bad distance")
    elif split_command[0] == "DIG":
        rover_state["samples"] + 1
    elif split_command[0] == "TURN":
        print("Turning...")
    else:
        print("Error: Unknown command sequence")
print(rover_state)
        

