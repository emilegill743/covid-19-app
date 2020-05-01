from bokeh.io import curdoc
from bokeh.models import (Div, ColumnDataSource, DatetimeTickFormatter,
                         DaysTicker, HoverTool, Span, Label, Title)
from bokeh.models.widgets import Tabs, Panel
from bokeh.layouts import row
from bokeh.plotting import figure
from bokeh.palettes import viridis
import pandas as pd
import numpy as np
import math
from datetime import datetime, timedelta
from tabs import lockdown_tab

div = Div(text="""Div""")

global_tab = Panel(child=div, title='Global')

countries_tab = Panel(child=div, title='Countries')

regions_tab = Panel(child=div, title='Regions')

lockdown_tab = lockdown_tab.build_lockdown_tab()

tabs = Tabs(tabs=[global_tab, countries_tab, regions_tab, lockdown_tab])

curdoc().add_root(tabs)