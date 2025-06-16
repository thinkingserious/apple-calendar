import appscript
from datetime import datetime

def add_to_calendar(title, details, location, start_datetime, end_datetime, calendar_name):
    """Add a single event to ``calendar_name``.

    If ``start_datetime`` or ``end_datetime`` can't be parsed, the event will be
    skipped instead of raising an exception. This prevents the whole script from
    failing when placeholder values are left in ``events``.
    """

    try:
        # Convert start_datetime and end_datetime to datetime objects
        start_time = datetime.strptime(start_datetime, "%Y-%m-%d %H:%M")
        end_time = datetime.strptime(end_datetime, "%Y-%m-%d %H:%M")
    except ValueError:
        print(f"Skipping event '{title}' due to invalid date format.")
        return

    # Create a new event in the specified calendar
    appscript.app("Calendar").calendars[calendar_name].events.end.make(
        new=appscript.k.event, 
        with_properties={
            appscript.k.summary: title,
            appscript.k.description: details,
            appscript.k.location: location,
            appscript.k.start_date: start_time,
            appscript.k.end_date: end_time
        }
    )

if __name__ == "__main__":
    # Import the k and app objects from appscript
    k = appscript.k
    app = appscript.app
    
    # List of events with dates, locations, titles, and details
    events = [
        ("<Event Title>", "<Event Description>", "<Event Location>", "<Start Date>", "<End Date>"),
        ("<Event Title>", "<Event Description>", "<Event Location>", "<2023-01-26 15:00>", "<2023-01-26 16:00>"),
    ]
    
    # The name of the calendar where the events will be added
    calendar_name = "<Calendar Name>"
    
    # Add each event to the calendar
    for event in events:
        title, details, location, start_datetime, end_datetime = event
        add_to_calendar(title, details, location, start_datetime, end_datetime, calendar_name)
