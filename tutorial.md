This workflow will guide you ** i) on how to mark spot elevations at various randomly selected and spaced points within a boundary**. You can also mark them on non-randomly selected spots. 
Spot elevations are a less information-dense representation of elevation/mean height above sea level compared to contour lines. It's largely for a broad understanding of the elevational 
pattern of an area rather than rigorous analysis of the elevational pattern. In addition, this workflow will guide you  **ii) on how to create points for the highest and lowest elevations within an
area of interest** with the use of a Python script run through QGIS.

### i) Spot elevation creation

**Step 1:** First, find a suitable and accurate DEM. You can refer to the [methods here](https://github.com/paulvpop/gis-land-cover-mapping/blob/main/05.%20Level%202%20processing.md#step-2-select-the-dem-download-it-and-process-it-if-required).

**Step 2:** Open the DEM in QGIS. Loading it in a VRT (virtual raster tile) form makes it faster (you can convert the tiff to this format in QGIS itself if already not in VRT form). I have used ALOS DEM for my area of interest in Arunachal Pradesh.

<img width="1318" height="808" alt="image" src="https://github.com/user-attachments/assets/2fc67b58-710b-4d5d-9057-4182a981b57a" /> <br>

**Step 3:** Load any boundary layer you want the the spot elevations to be represented. In this case, the boundary is taken as Mouling National Park.

<img width="820" height="716" alt="image" src="https://github.com/user-attachments/assets/08b58c56-ccb3-47ea-b886-8108e95e28a1" />

**Step 4:** For the next steps, it will be best to keep the *Processing Toolbax* panel open for ease of access to make tools/algorithms. 

```
View > Panels > Processing Toolbox
```
<img width="638" height="1034" alt="image" src="https://github.com/user-attachments/assets/7e14541a-bfe2-4f38-af90-bbb2ca9958f3" /> <br>

**Step 5:** If you need to create a buffer for the area of interest (to give better context to the elevational distribution), use the *Buffer* algorithm (type it in the *Processing Toolbox* search). 
Depending on the CRS of the boundary layer, the distance will be in degrees (more trial-and-error needed to find out the right buffer distance) or in metres (straightforward). Adjust the Segments to
adjust the smoothening of the boundary of the buffer.

<img width="1319" height="536" alt="Screenshot 2026-05-07 161758" src="https://github.com/user-attachments/assets/1b40c8c9-3f56-4173-8577-fb075759831c" />

The darker green is the buffer here:

<img width="687" height="533" alt="image" src="https://github.com/user-attachments/assets/1da369d6-2265-4a6e-bcff-c482f1965480" />

It's best to make the layer permanent if needed for later too (the temporary layer won't show up even if saved and then reopened). 
This step can be avoided if directly saving it while running the algorithm (Click on ... on the right of the [Create temporary layer] option 
at the end of the pop-up for the Buffer algorithm.

<img width="487" height="502" alt="image" src="https://github.com/user-attachments/assets/2be9f090-2bb1-4198-8fcd-404cb686c871" /> <br>

**Step 6:** Now, use the 'Random points inside polygon' algorithm  (use the *Processing Toolbox* to search). Keep the Input layer as 'Buffered' from the previous step.
Under Point counts or density, put the number of points you want (assuming you kept the Sampling Strategy as 'Points count' itself - the default). 
Set the 'Minimum distance between points' to facilitate the creation of well spaced points. 

<img width="1304" height="680" alt="Screenshot 2026-05-07 163915" src="https://github.com/user-attachments/assets/f1e34369-f40f-4574-af59-7fc8716e8059" />

The output will look like this:

<img width="1195" height="555" alt="image" src="https://github.com/user-attachments/assets/adf88bae-27ca-4d22-b451-adfcefcf1a0a" /> <br>

**Step 7:** Now , use the 'Sample raster values' algorithm to sample the elevation data from the DEM. The Input Layer should be the Random Points (or any collection of points
you acquired through another method - such as uniform sampling) and the Raster Layer as the DEM.

<img width="1034" height="718" alt="image" src="https://github.com/user-attachments/assets/77ec6e72-5224-454e-87c5-ff0f166161fb" /> <br>

**Step 8:** Click on 'Sampled' (the output from the previous step) and select 'Properties'.

<img width="348" height="457" alt="image" src="https://github.com/user-attachments/assets/507d1d7b-11a9-4b9d-9769-1c7dea48a909" /> <br>

**Step 9:** Make any cosmetic adjustments to icon under 'Symbology' > 'Marker' > 'Simple Marker'. I have made the icons triangles (select from the shapes in the bottom) with transparent fill (select under 'Fill color').

<img width="947" height="935" alt="image" src="https://github.com/user-attachments/assets/269998a9-bc42-4de4-8ee0-18c4f707567e" /> <br>

It will look like this:

<img width="735" height="580" alt="image" src="https://github.com/user-attachments/assets/6eb8772c-6ad0-4977-a812-bc8489543618" /> <br>

**Step 9:** Click on the 'Sampled' vector layer and then select the 'Layer Labelling Options' in the top panel.

<img width="719" height="657" alt="image" src="https://github.com/user-attachments/assets/2924c32a-6506-4b22-94aa-8089ed8820e1" /> <br>

**Step 10:** On the right hand side, under the 'Layer Styling' pane, select 'Single Labels'.

<img width="309" height="460" alt="image" src="https://github.com/user-attachments/assets/d1575b73-dfa2-4868-8a32-401c3168e606" /> <br>

**Step 11:** Then under 'Value' select 'SAMPLE_'.

<img width="293" height="384" alt="image" src="https://github.com/user-attachments/assets/2b75182e-8a12-4486-b113-954bb7ac049b" /> <br>

This will give the desired output of the boundary with spot elevations. You can change the fonts, font size etc on the right hand side panel.

<img width="692" height="525" alt="image" src="https://github.com/user-attachments/assets/4cfb7c65-e086-46a9-96b7-1660a7886cd2" />

### ii) Highest and lowest elevation creation

**Step 1:** First, if not already done, clip the DEM to your specific area of interest (in this case, it is the DEM clipped to the Mouling National Park boundary). 
This can be done by using the 'Clip raster by mask layer' algorithm (search in the *Processing Toolbox*). Keep the 'Input Layer' as the DEM and the 'Mask Layer' as the
area of interest. Also, check the 'Keep resolution of input raster'. Save as a permanent file (ideal).

<img width="1018" height="658" alt="image" src="https://github.com/user-attachments/assets/999507c6-3ef4-48a4-93b8-2341e73dcb33" /> <br>

Output:

<img width="655" height="504" alt="image" src="https://github.com/user-attachments/assets/473c735a-2ee8-4db9-91b1-358ccb8f184a" /> <br>

**Step 2:** 

## Option A:

*Step 2.A.i:* Download the Python script uploaded [here](https://github.com/paulvpop/spot-elevation-creation-from-dem/blob/main/create_highest_lowest_elevation_points_in_QGIS.py). Click on
'Download raw file' on the top right to download:

<img width="1883" height="163" alt="image" src="https://github.com/user-attachments/assets/aa4a94cb-a282-46bf-8855-7425cf1bd0d4" />

Preferably, download it to a location associated with the project.

*Step 2.A.ii:* Go to `Plugins > Python Console`

<img width="517" height="199" alt="image" src="https://github.com/user-attachments/assets/1f90cf82-1c2b-4c69-8c72-608b3763c720" /> <br>

*Step 2.A.iii:* Click on 'Show Editor'.

<img width="1162" height="440" alt="image" src="https://github.com/user-attachments/assets/93aa8820-9226-497d-8ff9-8468d107430c" /> <br>

*Step 2.A.iv:* Click on 'Open Script'.

<img width="1144" height="456" alt="image" src="https://github.com/user-attachments/assets/63c89a67-e1b9-453b-9c1b-50c416e76b81" /> <br>

*Step 2.A.v:* Select and 'Open' the downloaded Python script.

<img width="800" height="223" alt="image" src="https://github.com/user-attachments/assets/9f8f8cbe-3310-40c8-8c3b-8a5c20cfe56a" /> <br>

*Step 2.A.vi:* In the line 8 of the script, change the layer name (within the quotes) to the clipped DEM from Step 1.

<img width="709" height="83" alt="image" src="https://github.com/user-attachments/assets/a2a8e890-0a4d-43c6-9834-a34ce3617769" /> <br>

*Step 2.A.vii:* In the line 85 of the script, change the output_folder path to your desired location (ideally, the project folder).
The script will automatically create the folder if it doesn't exist.

<img width="664" height="79" alt="image" src="https://github.com/user-attachments/assets/b6b62c61-d755-456e-9621-cb4d8a2704ce" /> <br>

*Step 2.A.viii:* Click on 'Run Script' ( I> button). This script will will create and save the highest and lowest points separately
so that they can be styled differently later on. They will be named 'lowest_elevation_point.gpkg' and 'highest_elevation_point.gpkg'. 
It will save it as GeoPackage files which will contain the point layer with the features and their attributes. It will also zoom into 
the area encompassing the highest and lowest elevations. 

<img width="623" height="452" alt="image" src="https://github.com/user-attachments/assets/63365ca6-881c-4d51-ae7a-b75a8593a087" /> <br>

In addition, in the console (on the left), it will output the file size of the points, where it is saved, the highest and lowest
elevation values and its coordinates.

<img width="564" height="465" alt="image" src="https://github.com/user-attachments/assets/763c6be6-3880-4c55-89c5-6f2b7575626f" /> <br>

## Option B:

*Step 2.B.i:* Copy the Python script given below:

```
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
```

*Step 2.B.ii:* Go to `Plugins > Python Console`

<img width="517" height="199" alt="image" src="https://github.com/user-attachments/assets/1f90cf82-1c2b-4c69-8c72-608b3763c720" /> <br>

*Step 2.B.iii:* Click on 'Show Editor'.

<img width="1162" height="440" alt="image" src="https://github.com/user-attachments/assets/93aa8820-9226-497d-8ff9-8468d107430c" /> <br>

*Step 2.B.iv:* Paste the copied script on the empty untitled Editor (save it using the floppy disk icon to access it later too).

<img width="820" height="568" alt="image" src="https://github.com/user-attachments/assets/9c19918e-b92a-4e97-93b5-866c4e7ede5a" /> <br>

Now follow step *Step 2.A.vi:* to *Step 2.A.viii:* from Option A above. These are common steps for both the options.

**Step 3:** Style the highest and lowest elevations similar to the spot elevations (Steps 8 and 9 of the spot elevation section), but provide a different colour for each (for example,
red for the highest elevationa and blue for the lowest elevation). Change the 'Stoke Color' and 'Fill Color' for better aesthetics.

<img width="938" height="410" alt="image" src="https://github.com/user-attachments/assets/e38ffab9-7baa-4083-80ba-b89cc6ba8984" /> <br>

**Step 4:** Now, display the elevation like the spot elevation (Steps 10 and 11 of the spot elevation section).

<img width="526" height="439" alt="image" src="https://github.com/user-attachments/assets/d2a242f0-fb01-4b9f-9317-417a5c8aab9c" /> <br>










