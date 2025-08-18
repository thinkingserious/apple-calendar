"""MCP server exposing Apple Calendar functionality.

This module exposes the :func:`add_to_calendar` function from ``apple-calendar.py``
via the Model Context Protocol (MCP).  The ``add_event`` tool mirrors the
arguments of :func:`add_to_calendar` and returns a simple confirmation message
when the event is created.

Running this module starts a FastMCP server named ``apple-calendar``.
"""

from __future__ import annotations

import importlib.util
import pathlib

# Lazily load ``add_to_calendar`` from ``apple-calendar.py``.  The source file
# uses a hyphen in its name, so we load it via ``importlib`` instead of a normal
# ``import`` statement.

def _load_add_to_calendar():
    path = pathlib.Path(__file__).with_name("apple-calendar.py")
    spec = importlib.util.spec_from_file_location("apple_calendar", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None  # for type checkers
    spec.loader.exec_module(module)
    return module.add_to_calendar

add_to_calendar = _load_add_to_calendar()


# Define the tool function that MCP clients will call.
# The function's signature matches ``add_to_calendar`` but returns a string
# confirming success so that callers receive a useful response.

def add_event(
    title: str,
    details: str,
    location: str,
    start: str,
    end: str,
    calendar: str,
) -> str:
    """Add an event to Apple's Calendar using MCP.

    Parameters mirror :func:`add_to_calendar`.  ``start`` and ``end`` should be
    in ``YYYY-MM-DD HH:MM`` format.
    """

    add_to_calendar(title, details, location, start, end, calendar)
    return "Event added"


if __name__ == "__main__":
    # Import FastMCP only when running the server so that the module can be
    # imported in environments without the ``mcp`` package (e.g. during tests).
    from mcp.server.fastmcp import FastMCP

    mcp = FastMCP("apple-calendar")
    mcp.register(add_event)
    mcp.run()
