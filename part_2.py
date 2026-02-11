rover_status = {
    "battery":100,
    "heater":"off",
    "camera":"standby"
}
x = dict(list(rover_status.items())[:1])
print(x)
rover_status.update({"battery":85,"heater":"on","speed":5})
print(rover_status)
Dictionary_1 = {"Site": "Crater A", "Radiation": "Low", "Water": False}
Dictionary_2 = {"Site": "Dune B", "Radiation": "High", "Water": True}
mission_log = [Dictionary_1,Dictionary_2]
for values in mission_log:
    site = values["Site"]
    radiation = values["Radiation"]
    print(f"{site} has {radiation} radiation")