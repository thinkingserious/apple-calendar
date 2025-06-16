import os
import sys
import types
import importlib.util
from datetime import datetime
import unittest
from unittest import mock


class TestAddToCalendar(unittest.TestCase):
    def _load_module(self):
        path = os.path.join(os.path.dirname(__file__), os.pardir, 'apple-calendar.py')
        spec = importlib.util.spec_from_file_location('apple_calendar', path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        sys.modules['apple_calendar'] = module
        return module

    def test_make_called_on_calendar(self):
        fake_appscript = types.SimpleNamespace()
        fake_appscript.k = types.SimpleNamespace(
            event='event',
            summary='summary',
            description='description',
            location='location',
            start_date='start_date',
            end_date='end_date'
        )
        fake_appscript.app = lambda *a, **k: None

        with mock.patch.dict(sys.modules, {'appscript': fake_appscript}):
            module = self._load_module()
            class End:
                def __init__(self):
                    self.make = mock.Mock()
            class Events:
                def __init__(self):
                    self.end = End()
            class Calendar:
                def __init__(self):
                    self.events = Events()
            calendar_obj = Calendar()
            calendars = mock.MagicMock()
            calendars.__getitem__.return_value = calendar_obj
            app_instance = mock.Mock(calendars=calendars)
            with mock.patch('apple_calendar.appscript.app', return_value=app_instance) as mock_app:
                module.add_to_calendar(
                    'Title', 'Details', 'Location',
                    '2023-01-01 10:00', '2023-01-01 11:00', 'MyCal'
                )
                mock_app.assert_called_once_with('Calendar')
                calendars.__getitem__.assert_called_once_with('MyCal')
                expected_props = {
                    fake_appscript.k.summary: 'Title',
                    fake_appscript.k.description: 'Details',
                    fake_appscript.k.location: 'Location',
                    fake_appscript.k.start_date: datetime(2023, 1, 1, 10, 0),
                    fake_appscript.k.end_date: datetime(2023, 1, 1, 11, 0)
                }
                calendar_obj.events.end.make.assert_called_once_with(
                    new=fake_appscript.k.event,
                    with_properties=expected_props
                )


if __name__ == '__main__':
    unittest.main()
