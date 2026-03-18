import appscript
from datetime import datetime

def add_to_calendar(title, details, start_time, end_time, calendar_name):
    # Convert start_time and end_time to datetime objects
    start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M')
    end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M')

    # Create a new event in the specified calendar
    appscript.app("Calendar").calendars[calendar_name].events.end.make(
        new=appscript.k.event, 
        with_properties={
            appscript.k.summary: title,
            appscript.k.description: details,
            appscript.k.start_date: start_time,
            appscript.k.end_date: end_time
        }
    )

if __name__ == "__main__":
    # Import the k and app objects from appscript
    # [appscript documentation](https://appscript.readthedocs.io/en/latest/)
    # [k object documentation](https://appscript.readthedocs.io/en/latest/terminology/k.html)
    # [app function documentation](https://appscript.readthedocs.io/en/latest/terminology/app.html)
    k = appscript.k
    app = appscript.app
    
    # Set the base date for the itinerary
    base_date = "2023-09-29"
    
    # List of events in the itinerary
    events = [
        ("Beignets at Ralph Brennan's Jazz Kitchen", "Get beignets for Audrey.", "23:30", "23:59")
    ]

    # Add each event to the calendar
    for event in events:
        title, details, start, end = event
        start_time = f"{base_date} {start}"
        end_time = f"{base_date} {end}"
        
        # Add the event to the "Thomas Family" calendar
        add_to_calendar(title, details, start_time, end_time, "Thomas Family")
