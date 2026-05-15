# Author: Paul Pop
# Affiliation: BIRD Lab, ATREE, Bengaluru (PI: Rajkamal Goswami)
--------------------------------------------------------------------------------------------------------------------------------------------------------------

from osgeo import gdal
import numpy as np
from qgis.core import QgsFeature, QgsGeometry, QgsField, QgsVectorLayer, QgsProject, QgsVectorFileWriter, QgsCoordinateTransformContext
from PyQt5.QtCore import QVariant
import os

# Load the DEM layer
layer = QgsProject.instance().mapLayersByName("alos_DEM_clipped_to_Mouling")[0]
dataset = gdal.Open(layer.source())
arr = dataset.ReadAsArray()

# Get NoData value (if any)
nodata = dataset.GetRasterBand(1).GetNoDataValue()
print(f"NoData value: {nodata}")

# Create a mask for valid data (exclude NoData values)
if nodata is not None:
    valid_mask = arr != nodata
    # Also exclude other potential invalid values (very negative numbers)
    valid_mask = valid_mask & (arr > -100)  # Adjust threshold as needed
    valid_data = arr[valid_mask]
else:
    valid_data = arr
    valid_mask = np.ones_like(arr, dtype=bool)

# Find maximum and minimum elevations from valid data only
maxvalue = valid_data.max()
minvalue = valid_data.min()

# Find coordinates of maximum elevation
max_idx = np.where((arr == maxvalue) & valid_mask)
max_row = max_idx[0][0]
max_col = max_idx[1][0]

# Find coordinates of minimum elevation
min_idx = np.where((arr == minvalue) & valid_mask)
min_row = min_idx[0][0]
min_col = min_idx[1][0]

# Get geotransform
GT = dataset.GetGeoTransform()

# Calculate coordinates for maximum elevation
max_x = GT[0] + (max_col + 0.5) * GT[1] + (max_row + 0.5) * GT[2]
max_y = GT[3] + (max_col + 0.5) * GT[4] + (max_row + 0.5) * GT[5]

# Calculate coordinates for minimum elevation
min_x = GT[0] + (min_col + 0.5) * GT[1] + (min_row + 0.5) * GT[2]
min_y = GT[3] + (min_col + 0.5) * GT[4] + (min_row + 0.5) * GT[5]

# Create separate point layers for highest and lowest
highest_layer = QgsVectorLayer("Point?crs=" + layer.crs().authid(), "Highest_Elevation", "memory")
lowest_layer = QgsVectorLayer("Point?crs=" + layer.crs().authid(), "Lowest_Elevation", "memory")

# Get providers
highest_provider = highest_layer.dataProvider()
lowest_provider = lowest_layer.dataProvider()

# Add fields to both layers
for provider in [highest_provider, lowest_provider]:
    provider.addAttributes([QgsField("Type", QVariant.String), 
                           QgsField("Elevation", QVariant.Double),
                           QgsField("X_Coord", QVariant.Double),
                           QgsField("Y_Coord", QVariant.Double)])

# Update fields for both layers (this is a method of QgsVectorLayer, not provider)
highest_layer.updateFields()
lowest_layer.updateFields()

# Create highest point feature
highest_feature = QgsFeature()
highest_feature.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(max_x, max_y)))
highest_feature.setAttributes(["Highest", float(maxvalue), float(max_x), float(max_y)])

# Create lowest point feature
lowest_feature = QgsFeature()
lowest_feature.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(min_x, min_y)))
lowest_feature.setAttributes(["Lowest", float(minvalue), float(min_x), float(min_y)])

# Add features to respective layers
highest_provider.addFeatures([highest_feature])
lowest_provider.addFeatures([lowest_feature])

# Define output folder
output_folder = "D:/Paul_Pop_RS_GIS_files/Arunachal/"  # Change this path if needed
os.makedirs(output_folder, exist_ok=True)

# Save highest elevation point as separate GeoPackage
highest_output = os.path.join(output_folder, "highest_elevation_point.gpkg")
error1, error_msg1 = QgsVectorFileWriter.writeAsVectorFormatV2(
    highest_layer,
    highest_output,
    QgsCoordinateTransformContext(),
    options=QgsVectorFileWriter.SaveVectorOptions()
)

if error1 == QgsVectorFileWriter.NoError:
    print(f"✓ Highest elevation point saved to: {highest_output}")
    if os.path.exists(highest_output):
        file_size = os.path.getsize(highest_output)
        print(f"  File size: {file_size} bytes")
else:
    print(f"✗ Error saving highest point: {error1} - {error_msg1}")

# Save lowest elevation point as separate GeoPackage
lowest_output = os.path.join(output_folder, "lowest_elevation_point.gpkg")
error2, error_msg2 = QgsVectorFileWriter.writeAsVectorFormatV2(
    lowest_layer,
    lowest_output,
    QgsCoordinateTransformContext(),
    options=QgsVectorFileWriter.SaveVectorOptions()
)

if error2 == QgsVectorFileWriter.NoError:
    print(f"✓ Lowest elevation point saved to: {lowest_output}")
    if os.path.exists(lowest_output):
        file_size = os.path.getsize(lowest_output)
        print(f"  File size: {file_size} bytes")
else:
    print(f"✗ Error saving lowest point: {error2} - {error_msg2}")

# Add both layers to the map
QgsProject.instance().addMapLayer(highest_layer)
QgsProject.instance().addMapLayer(lowest_layer)

# Create a combined temporary layer for zooming purpose only
combined_layer = QgsVectorLayer("Point?crs=" + layer.crs().authid(), "Combined_Points_Temp", "memory")
combined_provider = combined_layer.dataProvider()
combined_provider.addAttributes([QgsField("Type", QVariant.String), QgsField("Elevation", QVariant.Double)])
combined_layer.updateFields()
combined_provider.addFeatures([highest_feature, lowest_feature])

# Zoom to show both points with appropriate margin
canvas = iface.mapCanvas()
extent = combined_layer.extent()
# Add a 20% margin around the points for better visibility
extent.scale(1.2)
canvas.setExtent(extent)
canvas.refresh()

# Print results
print(f"Highest elevation: {maxvalue}m at ({max_x:.2f}, {max_y:.2f})")
print(f"\nLowest elevation: {minvalue}m at ({min_x:.2f}, {min_y:.2f})")
print("\nBoth points are within the DEM extent")
print("Map view zoomed to show both points")
