"""
ALARM CLOCK
ALGORITHM
1.Create set_alaram and countdown seconds
2. Ask user to input alaram time in HH:MM format
3. Check if the input is valid HH:MM format
4. if valid return the alaram time else throw error and ask user to input again
5. iterate through the countdown seconds b/w 0 and -1
6. Extract hours and minutes from the countdown seconds
7.For Alarm hours and minutes set it to alarm time
8. Create now datatime object
9. replace now parameters with alarm hours and minutes
10. Check if now is equal to alarm time
11. If alarm data and time is less than now then add 1 day to alarm time
12. Calculate seconds to wait by subtracting now from alarm time
13. Print alarm set time and current time
14. Print alaram and alarm message
15. ask for snooze time from user
16. and if snooze is set then wait for snooze time and repeat the alarm message
17 Snooze alaram else alarm stoped 
"""
import time
import datetime
import sys

def set_alarm():
    while True:
        alarm_time = input("Enter the alarm time in HH:MM format (24-hour): ").strip()

        try:
            # Validate the input format
            alarm_hour, alarm_minute = map(int, alarm_time.split(':'))
            if 0 <= alarm_hour <=23 and 0 <= alarm_minute <=59:
                return alarm_hour, alarm_minute
            else:
                print("Invalid time. Please enter a valid time in HH:MM format.")
        except ValueError:
            print("Invalid input. Please enter the time in HH:MM format.")
         
        
def countdown(seconds):
    for remaining in range(seconds, 0, -1):
        hours = remaining // 3600
        minutes = (remaining % 3600) // 60
        seconds = remaining % 60
        print(f"\rAlarm in: {hours:02d}:{minutes:02d}:{seconds:02d}", end="", flush=True)
        time.sleep(1)
    print("\r" + " " * 30 + "\r", end="")


def main():
    print("=== Alarm Clock ===")
    alarm_hour, alarm_minute = set_alarm()

    now = datetime.datetime.now()
    alarm_time = now.replace(hour=alarm_hour, minute=alarm_minute, second=0, microsecond=0)

    if alarm_time <= now:
        alarm_time += datetime.timedelta(days=1)

    seconds_to_wait = (alarm_time - now).total_seconds()
    print(f"Alarm set for: {alarm_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Current time: {now.strftime('%Y-%d %H:%M:%S')}")
    print(f"Waiting for {int(seconds_to_wait)} seconds until the alarm goes off...")

    print("\n⏰ ALARM! ⏰")
    message = input("Enter alarm message: ").strip() or "Time to wake up!"
    print(f"\n{message}")


    snooze = input("\nSnooze? (y/n): ").lower()
    if snooze == 'y':
        print("Snoozing for 5 minutes...")
        time.sleep(300)
        print("⏰ SNOOZE ALARM! ⏰")
    else:
        print("Alarm stopped. Have a great day!")

if __name__ == "__main__":
    main()

    