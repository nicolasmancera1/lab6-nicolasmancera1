def trigger_alarm(temperatures, threshold=80):
    alarm_sensors = []
    for sensor, temp in temperatures.items():
        if temp > threshold:
            alarm_sensors.append(sensor)
    return alarm_sensors