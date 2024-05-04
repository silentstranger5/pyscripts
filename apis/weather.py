import requests, sys

def weather(latitude, longitude, args):
    payload = dict([
        ("latitude", latitude),
        ("longitude", longitude),
        ("current", ','.join(args))
    ])
    r = requests.get("https://api.open-meteo.com/v1/forecast", params=payload)
    if r.status_code != 200:
        exit("Something went wrong")

    return r.json().get("current")

def display(weather, args):
    string = weather.get("time") + " "
    for arg in args:
        unit = ""
        match arg:
            case "temperature_2m":
                unit = "°C"
            case "relative_humidity_2m":
                unit = "%"
            case "wind_speed_10m":
                unit = "m/s"
        string += str(weather.get(arg)) + unit + " "
    return string

if __name__ == "__main__":
    if len(sys.argv) != 3:
        exit("usage: python weather.py latitude longitude")
    latitude = sys.argv[1]
    longitude = sys.argv[2]
    args = ["temperature_2m", "relative_humidity_2m", "wind_speed_10m"]
    weather_data = weather(latitude, longitude, args)
    weather_data = display(weather_data, args)
    print(weather_data)