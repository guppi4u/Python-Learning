# this program is to findout the timezone of a given location using the timezonefinder library

from timezonefinder import TimezoneFinder

def get_timezone(lat, lng):
    tf = TimezoneFinder()
    timezone = tf.timezone_at(lng=lng, lat=lat)
    return timezone
def main():
    lat = float(input("Enter the latitude: "))
    lng = float(input("Enter the longitude: "))
    timezone = get_timezone(lat, lng)
    if timezone:
        print(f"The timezone for the location ({lat}, {lng}) is: {timezone}")
    else:
        print("Could not determine the timezone for the given location.")

if __name__ == "__main__":
    main()

    