#import pandas as pd

#df = pd.read_csv("2015_Street_Tree_Census_-_Tree_Data.csv")

#print(df.head())

import geoviews as gv
import geoviews.feature as gf
import xarray as xr
from cartopy import crs

gv.extension('bokeh')

(gf.land * gf.ocean * gf.borders).opts(
    'Feature', 
    projection=crs.Mercator(), 
    global_extent=True, 
    width=500
)