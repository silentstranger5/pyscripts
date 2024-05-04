import json, requests, sys

def current_time(timezone):
    payload = dict([("timeZone", timezone)])
    r = requests.get('https://timeapi.io/api/Time/current/zone', params=payload)
    if r.status_code != 200:
        exit("Invalid timezone")
    return r.json()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit("usage: time.py timezone")
    timezone = sys.argv[1]
    time = current_time(timezone)
    print(f"{time.get("time")} {time.get("date")} {time.get("dayOfWeek")}")