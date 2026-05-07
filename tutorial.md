This workflow will guide you on how to mark spot elevations at various randomly selected and spaced points within a boundary. You can also mark them on non-randomly selected spots. 
Spot elevations are a less information-dense representation of elevation/mean height above sea level compared to contour lines. It's largely for a broad understanding of the elevational 
pattern of an area rather than rigorous analysis of the elevational pattern.

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









