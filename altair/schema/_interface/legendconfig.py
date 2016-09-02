# This file auto-generated by `generate_schema_interface.py`.
# Do not modify this file directly.

import traitlets as T
from ..baseobject import BaseObject


class LegendConfig(BaseObject):
    """Wrapper for Vega-Lite LegendConfig definition.
    
    Attributes
    ----------
    gradientHeight: CFloat
        The height of the gradient, in pixels.
    gradientStrokeColor: Unicode
        The color of the gradient stroke, can be in hex color code or regular color name.
    gradientStrokeWidth: CFloat
        The width of the gradient stroke, in pixels.
    gradientWidth: CFloat
        The width of the gradient, in pixels.
    labelAlign: Unicode
        The alignment of the legend label, can be left, middle or right.
    labelBaseline: Unicode
        The position of the baseline of legend label, can be top, middle or bottom.
    labelColor: Unicode
        The color of the legend label, can be in hex color code or regular color name.
    labelFont: Unicode
        The font of the lengend label.
    labelFontSize: CFloat
        The font size of lengend lable.
    labelOffset: CFloat
        The offset of the legend label.
    margin: CFloat
        The margin around the legend, in pixels.
    offset: CFloat
        The offset, in pixels, by which to displace the legend from the edge of the enclosing group or data rectangle.
    orient: Unicode
        The orientation of the legend.
    padding: CFloat
        The padding, in pixels, between the lengend and axis.
    properties: Any
        Optional mark property definitions for custom legend styling.
    shortTimeLabels: Bool
        Whether month names and weekday names should be abbreviated.
    symbolColor: Unicode
        The color of the legend symbol,.
    symbolShape: Unicode
        The shape of the legend symbol, can be the 'circle', 'square', 'cross', 'diamond', 'triangle-up', 'triangle-down', or else a custom SVG path string.
    symbolSize: CFloat
        The size of the lengend symbol, in pixels.
    symbolStrokeWidth: CFloat
        The width of the symbol's stroke.
    titleColor: Unicode
        Optional mark property definitions for custom legend styling.
    titleFont: Unicode
        The font of the legend title.
    titleFontSize: CFloat
        The font size of the legend title.
    titleFontWeight: Unicode
        The font weight of the legend title.
    """
    gradientHeight = T.CFloat(allow_none=True, default_value=None, help="""The height of the gradient, in pixels.""")
    gradientStrokeColor = T.Unicode(allow_none=True, default_value=None, help="""The color of the gradient stroke, can be in hex color code or regular color name.""")
    gradientStrokeWidth = T.CFloat(allow_none=True, default_value=None, help="""The width of the gradient stroke, in pixels.""")
    gradientWidth = T.CFloat(allow_none=True, default_value=None, help="""The width of the gradient, in pixels.""")
    labelAlign = T.Unicode(allow_none=True, default_value=None, help="""The alignment of the legend label, can be left, middle or right.""")
    labelBaseline = T.Unicode(allow_none=True, default_value=None, help="""The position of the baseline of legend label, can be top, middle or bottom.""")
    labelColor = T.Unicode(allow_none=True, default_value=None, help="""The color of the legend label, can be in hex color code or regular color name.""")
    labelFont = T.Unicode(allow_none=True, default_value=None, help="""The font of the lengend label.""")
    labelFontSize = T.CFloat(allow_none=True, default_value=None, help="""The font size of lengend lable.""")
    labelOffset = T.CFloat(allow_none=True, default_value=None, help="""The offset of the legend label.""")
    margin = T.CFloat(allow_none=True, default_value=None, help="""The margin around the legend, in pixels.""")
    offset = T.CFloat(allow_none=True, default_value=None, help="""The offset, in pixels, by which to displace the legend from the edge of the enclosing group or data rectangle.""")
    orient = T.Unicode(allow_none=True, default_value=None, help="""The orientation of the legend.""")
    padding = T.CFloat(allow_none=True, default_value=None, help="""The padding, in pixels, between the lengend and axis.""")
    properties = T.Any(allow_none=True, default_value=None, help="""Optional mark property definitions for custom legend styling.""")
    shortTimeLabels = T.Bool(allow_none=True, default_value=None, help="""Whether month names and weekday names should be abbreviated.""")
    symbolColor = T.Unicode(allow_none=True, default_value=None, help="""The color of the legend symbol,.""")
    symbolShape = T.Unicode(allow_none=True, default_value=None, help="""The shape of the legend symbol, can be the 'circle', 'square', 'cross', 'diamond', 'triangle-up', 'triangle-down', or else a custom SVG path string.""")
    symbolSize = T.CFloat(allow_none=True, default_value=None, help="""The size of the lengend symbol, in pixels.""")
    symbolStrokeWidth = T.CFloat(allow_none=True, default_value=None, help="""The width of the symbol's stroke.""")
    titleColor = T.Unicode(allow_none=True, default_value=None, help="""Optional mark property definitions for custom legend styling.""")
    titleFont = T.Unicode(allow_none=True, default_value=None, help="""The font of the legend title.""")
    titleFontSize = T.CFloat(allow_none=True, default_value=None, help="""The font size of the legend title.""")
    titleFontWeight = T.Unicode(allow_none=True, default_value=None, help="""The font weight of the legend title.""")
    
    def __init__(self, gradientHeight=None, gradientStrokeColor=None, gradientStrokeWidth=None, gradientWidth=None, labelAlign=None, labelBaseline=None, labelColor=None, labelFont=None, labelFontSize=None, labelOffset=None, margin=None, offset=None, orient=None, padding=None, properties=None, shortTimeLabels=None, symbolColor=None, symbolShape=None, symbolSize=None, symbolStrokeWidth=None, titleColor=None, titleFont=None, titleFontSize=None, titleFontWeight=None, **kwargs):
        kwds = dict(gradientHeight=gradientHeight, gradientStrokeColor=gradientStrokeColor, gradientStrokeWidth=gradientStrokeWidth, gradientWidth=gradientWidth, labelAlign=labelAlign, labelBaseline=labelBaseline, labelColor=labelColor, labelFont=labelFont, labelFontSize=labelFontSize, labelOffset=labelOffset, margin=margin, offset=offset, orient=orient, padding=padding, properties=properties, shortTimeLabels=shortTimeLabels, symbolColor=symbolColor, symbolShape=symbolShape, symbolSize=symbolSize, symbolStrokeWidth=symbolStrokeWidth, titleColor=titleColor, titleFont=titleFont, titleFontSize=titleFontSize, titleFontWeight=titleFontWeight)
        kwargs.update({k:v for k, v in kwds.items() if v is not None})
        super(LegendConfig, self).__init__(**kwargs)