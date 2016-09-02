# This file auto-generated by `generate_schema_interface.py`.
# Do not modify this file directly.

import traitlets as T
from ..baseobject import BaseObject
from .dataformat import DataFormat


class Data(BaseObject):
    """Wrapper for Vega-Lite Data definition.
    
    Attributes
    ----------
    format: DataFormat
        An object that specifies the format for the data file or values.
    url: Unicode
        A URL from which to load the data set.
    values: List(Any)
        Pass array of objects instead of a url to a file.
    """
    format = T.Instance(DataFormat, allow_none=True, default_value=None, help="""An object that specifies the format for the data file or values.""")
    url = T.Unicode(allow_none=True, default_value=None, help="""A URL from which to load the data set.""")
    values = T.List(T.Any(), allow_none=True, default_value=None, help="""Pass array of objects instead of a url to a file.""")
    
    def __init__(self, format=None, url=None, values=None, **kwargs):
        kwds = dict(format=format, url=url, values=values)
        kwargs.update({k:v for k, v in kwds.items() if v is not None})
        super(Data, self).__init__(**kwargs)