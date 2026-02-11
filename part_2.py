rover_status = {
    "battery":100,
    "heater":"off",
    "camera":"standby"
}
x = dict(list(rover_status.items())[:1])
print(x)
rover_status.update({"battery":85,"heater":"on","speed":5})
print(rover_status)