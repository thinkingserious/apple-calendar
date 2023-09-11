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
    base_date = "2023-09-10"
    
    # List of events in the itinerary
    events = [
        ("Arrival at California Adventure", "Begin your magical journey.", "15:30", "16:00"),
        ("Option A: Musical Celebration of Coco OR Option B: Dr. Strange: Mysteries of the Mystic Arts", "Attend the chosen show.", "16:00", "16:30"),
        ("Avengers Assemble!", "Join the Avengers.", "16:40", "17:10"),
        ("Meet Baymax in San Fransokyo Square", "Meet and greet session with Baymax.", "17:10", "17:30"),
        ("Option A: Explore and Eat OR Option B: Guardians of the Galaxy: Awesome Dance Off!", "Choose one activity.", "17:30", "18:00"),
        ("Mickey's Trick and Treat at Oogie Boogie Bash", "Attend the treat session.", "18:00", "18:30"),
        ("Transition to Disneyland for Parade", "Head to Disneyland for the parade.", "18:30", "19:00"),
        ("Magic Happens Parade", "Enjoy the parade.", "19:00", "20:00"),
        ("Visit to Mickey's Toontown", "Explore the magical town.", "20:00", "20:30"),
        ("Mickey & Minnie's Runaway Railway", "Experience the ride.", "20:30", "21:00"),
    ]
    
    # Add each event to the calendar
    for event in events:
        title, details, start, end = event
        start_time = f"{base_date} {start}"
        end_time = f"{base_date} {end}"
        
        # Add the event to the "Thomas Family" calendar
        add_to_calendar(title, details, start_time, end_time, "Thomas Family")
