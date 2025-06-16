# Python Access to Apple's Calendar App

This project allows users to interact with Apple's Calendar app using Python.

## Installation

To run this code, follow these steps:

1. Install the appscript module by running the following command in your terminal or command prompt:

```zsh
pip install appscript
```

## Usage

1. Run the script to launch a small graphical interface where you can enter the event details. After filling out the form, click **Add Event** to create the event:

```zsh
python3 apple-calendar.py
```

Note: Make sure to have the Calendar app open while running the script for the events to be added to the calendar. The first time you run the script you will be prompted to allow access to the Calendar app. You will need to allow access for the script to work.

## ToDo

- [ ] Delete the events that were created with this script.
- [ ] Add alarm functionality to the events.
- [ ] Implement color coding for different types of events.
- [ ] Add the ability to invite other people to the events.
- [ ] Include location information for the events.
- [ ] Explore the possibility of updating events via iPhone using Pythonista.

Feel free to contribute to this project or provide any feedback!
