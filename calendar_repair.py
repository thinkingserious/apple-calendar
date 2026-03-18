import datetime
import appscript

# Import the k and app objects from appscript
k = appscript.k
app = appscript.app

def add_to_calendar(title, details, start_time, end_time, calendar_name):
    # Convert the start_time and end_time parameters to datetime objects
    start_datetime = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_datetime = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    
    # Create a new event in the specified calendar
    app("Calendar").calendars[calendar_name].events.end.make(
        new=k.event, 
        with_properties={
            k.summary: title,
            k.description: details,
            k.start_date: start_datetime,
            k.end_date: end_datetime
        }
    )

if __name__ == "__main__":
    # Open the file containing the events
    with open("events.txt", "r") as f:
        # Read each line in the file
        # Add each event to the calendar
        for line in f:
            # Extract the event details from the line
            title = line.split(';')[0].strip()
            calendar_name = "Thomas Family"
            start_date = line.split(';')[2].strip()
            end_date = line.split(';')[3].strip()
            
            # Add the event to the calendar
            print(title)
            print(calendar_name)
            print(start_date)
            print(end_date)
            add_to_calendar(title, "", start_date, end_date, calendar_name)