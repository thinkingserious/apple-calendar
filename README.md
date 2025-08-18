# Python Access to Apple's Calendar App

This project allows users to interact with Apple's Calendar app using Python.

## Installation

To run this code, follow these steps:

1. Install the required Python packages:

```zsh
pip install appscript mcp
```

## Usage

1. Run the script to launch a small graphical interface where you can enter the event details. After filling out the form, click **Add Event** to create the event:

```zsh
python3 apple-calendar.py
```

Note: Make sure to have the Calendar app open while running the script for the events to be added to the calendar. The first time you run the script you will be prompted to allow access to the Calendar app. You will need to allow access for the script to work.

## MCP Tool

The calendar functionality can also be exposed as a [Model Context Protocol](https://github.com/modelcontextprotocol) (MCP)
tool so that other applications or LLMs can create events programmatically.

### Setup

1. Ensure the dependencies above are installed.
2. Start the MCP server:

   ```zsh
   python mcp_server.py
   ```

### Usage

With the server running, MCP clients can call the `add_event` tool with the following parameters:

- `title` – event title
- `details` – description
- `location` – event location
- `start` – start date/time in `YYYY-MM-DD HH:MM` format
- `end` – end date/time in `YYYY-MM-DD HH:MM` format
- `calendar` – name of the destination calendar

For example, using the MCP CLI:

```zsh
npx @modelcontextprotocol/cli call apple-calendar add_event '{"title":"Meeting","details":"Discuss roadmap","location":"Office","start":"2024-01-01 10:00","end":"2024-01-01 11:00","calendar":"Work"}'
```

## ToDo

- [ ] Delete the events that were created with this script.
- [ ] Add alarm functionality to the events.
- [ ] Implement color coding for different types of events.
- [ ] Add the ability to invite other people to the events.
- [ ] Include location information for the events.
- [ ] Explore the possibility of updating events via iPhone using Pythonista.

Feel free to contribute to this project or provide any feedback!
