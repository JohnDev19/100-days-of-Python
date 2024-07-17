from datetime import datetime
import pytz

def main():
    try:
        # current time in UTC
        utc_now = datetime.utcnow()

        # timezone of the viewer 
        viewer_timezone = input("Enter your timezone (e.g., Asia/Manila, Asia/Tokyo): ").strip()

        # convert UTC time to viewer's local time
        utc_now = pytz.utc.localize(utc_now)
        viewer_now = utc_now.astimezone(pytz.timezone(viewer_timezone))

        # formatting the ocal time
        formatted_date = viewer_now.strftime("%a, %b %d, %Y")
        formatted_time = viewer_now.strftime("%I:%M %p")

        # if it's AM or PM
        period = viewer_now.strftime("%p").lower()

        # printing the formatted date and time
        print(f"Current date and time in {viewer_timezone}:")
        print(f"{formatted_date}")
        print(f"{formatted_time} {period}")

    except pytz.UnknownTimeZoneError:
        print("Error: Unknown timezone. Please enter a valid timezone.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

### Imports:

## from datetime import datetime: Imports the datetime class for working with dates and times.

## import pytz: Imports the pytz library for timezone support.
