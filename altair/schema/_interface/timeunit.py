# This file auto-generated by `generate_schema_interface.py`.
# Do not modify this file directly.

import traitlets as T


class TimeUnit(T.Enum):
    """One of ['year', 'month', 'day', 'date', 'hours', 'minutes', 'seconds', 'milliseconds', 'yearmonth', 'yearmonthdate', 'yearmonthdatehours', 'yearmonthdatehoursminutes', 'yearmonthdatehoursminutesseconds', 'hoursminutes', 'hoursminutesseconds', 'minutesseconds', 'secondsmilliseconds', 'quarter', 'yearquarter', 'quartermonth', 'yearquartermonth']"""
    def __init__(self, default_value=T.Undefined, **metadata):
        super(TimeUnit, self).__init__(['year', 'month', 'day', 'date', 'hours', 'minutes', 'seconds', 'milliseconds', 'yearmonth', 'yearmonthdate', 'yearmonthdatehours', 'yearmonthdatehoursminutes', 'yearmonthdatehoursminutesseconds', 'hoursminutes', 'hoursminutesseconds', 'minutesseconds', 'secondsmilliseconds', 'quarter', 'yearquarter', 'quartermonth', 'yearquartermonth'],
                                    default_value=default_value,
                                    **metadata)
