from PySide2 import QtCore, QtWidgets
from hyo2.abc.lib.gdal_aux import GdalAux

GdalAux.check_proj4_data()

from mpl_toolkits.basemap import Basemap, __version__

import matplotlib.pyplot as plt

print(__version__)

map = Basemap(projection='ortho',
              lat_0=0, lon_0=0)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()

lons = [0, 10, -20, -20]
lats = [0, -10, 40, -20]

x, y = map(lons, lats)

map.scatter(x, y, marker='D',color='m')

plt.show()
