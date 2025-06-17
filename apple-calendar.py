import appscript
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

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
    calendar = appscript.app("Calendar").calendars[appscript.its.name == calendar_name]
    calendar.events.end.make(
        new=appscript.k.event,
        with_properties={
            appscript.k.summary: title,
            appscript.k.description: details,
            appscript.k.location: location,
            appscript.k.start_date: start_time,
            appscript.k.end_date: end_time
        }
    )

def submit_event(title_var, details_var, location_var, start_var, end_var, calendar_var):
    """Callback for the "Add Event" button."""
    title = title_var.get()
    details = details_var.get()
    location = location_var.get()
    start = start_var.get()
    end = end_var.get()
    calendar_name = calendar_var.get()

    if not all([title, start, end, calendar_name]):
        messagebox.showerror("Error", "Title, start date/time, end date/time, and calendar name are required.")
        return

    try:
        add_to_calendar(title, details, location, start, end, calendar_name)
        messagebox.showinfo("Success", "Event added to Calendar")
    except Exception as exc:
        messagebox.showerror("Error", str(exc))


if __name__ == "__main__":
    # Build a simple Tkinter UI for entering event details
    root = tk.Tk()
    root.title("Apple Calendar Event Creator")

    title_var = tk.StringVar()
    details_var = tk.StringVar()
    location_var = tk.StringVar()
    start_var = tk.StringVar()
    end_var = tk.StringVar()
    calendar_var = tk.StringVar()

    labels = [
        ("Title", title_var),
        ("Details", details_var),
        ("Location", location_var),
        ("Start (YYYY-MM-DD HH:MM)", start_var),
        ("End (YYYY-MM-DD HH:MM)", end_var),
        ("Calendar Name", calendar_var),
    ]

    for idx, (label_text, var) in enumerate(labels):
        tk.Label(root, text=label_text).grid(row=idx, column=0, sticky="e", padx=5, pady=2)
        tk.Entry(root, textvariable=var, width=40).grid(row=idx, column=1, padx=5, pady=2)

    tk.Button(
        root,
        text="Add Event",
        command=lambda: submit_event(title_var, details_var, location_var, start_var, end_var, calendar_var),
    ).grid(row=len(labels), columnspan=2, pady=5)

    root.mainloop()
