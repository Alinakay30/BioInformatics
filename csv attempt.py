uri = "file:///Users/QueenB/Documents/new_4900/mycords.csv?encoding=%s&delimiter=%s&xField=%s&yField=%s&crs=%s" % ("UTF-8",",", "x-cor", "y-cor","epsg:5069")

#Make a vector layer
eq_layer=QgsVectorLayer(uri,"DNA","delimitedtext")

#Check if layer is valid
if not eq_layer.isValid():
    print ("Layer not loaded")

#Add CSV data    
QgsProject.instance().addMapLayer(eq_layer)