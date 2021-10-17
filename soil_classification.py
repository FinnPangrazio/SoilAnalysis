from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessing,
                       QgsFeatureSink,
                       QgsProcessingException,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterFeatureSink)
from qgis.core import QgsExpression
from qgis.core import os
from qgis import processing

#Starts the algorithm process to create the feature sink layer 
class ExampleProcessingAlgorithm(QgsProcessingAlgorithm):

# Naming the constants so that they can be used for later functionality including for
# other algorithms.

    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'

#Returns a translatable string with the self.tr function
    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return ExampleProcessingAlgorithm()

#Returns the name of the algorithm and is also used to identify it
    def name(self):
        
        return 'myscript'

#Returns the translated algorithm name
    def displayName(self):

        return self.tr('My Script')

#Returns the name of the group that the algorithm belongs to
    def group(self):
        return self.tr('scripts')

#Returns the unique ID that the script belongs to
    def groupId(self):
        return 'scripts'

#Used for if their is a problem in the algorithm or script. Provides a basic description
#of what the problem is. 
    def shortHelpString(self):
        return self.tr("Example algorithm short description")

#Defining the inputs and outputs of the algorithm
    def initAlgorithm(self, config=None):

        # We add the input vector features source
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT,
                self.tr('Input Soil layer'),
                [QgsProcessing.TypeVectorAnyGeometry]
            )
        )

#Calculating the parameters through using the select tool
    def processAlgorithm(self, parameters, context, feedback):

#Create the selection ID string which will be used later as the parameter for what is used as the output
selectsoil_1 = ['Bleach-ferric', 'Bleached-Ferric', 'Bleached', 'Deep sandy topsoil (dunes and ri', 'Sandy topsoil']

#Creates the file name which depending on what it is for is linked to the selection that is relevant
fn = 'C:/temp/outputs/VegetableFruit_land'
#Vector file writer which uses the aforemention 'input soil layer' as the input
#Also creates the output as an ESRI shapefile and finally uses the selectsoil_1 as the parameter
writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn, 'Input Soil layer', \driverName='ESRI Shapefile', selectsoil_1=True)
#adds the vector layer to the map
selected_layer = iface.addVectorLayer(fn, '', 'ogr')


selectsoil_2 = ['petroferric', 'Petrocalcic (Crests and upper sl', 'petroferric', 'Hypercalcic', 'Endohypersodic']

fn = 'C:/temp/outputs/"CerealCropping_land'
writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn, 'Input Soil layer', \driverName='ESRI Shapefile', selectsoil_2=True)

selected_layer = iface.addVectorLayer(fn, '', 'ogr')


selectsoil_3 = ['Mottled-subnatric', 'Mottled-Sodic', 'Mottled-mesonatric  (slight rise', 'Mottled-mesonatric', 'Mottled-Mesonatric']

fn = 'C:/temp/outputs/OrnamentalCrop_land'
writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn, 'Input Soil layer', \driverName='ESRI Shapefile', selectsoil_3=True)

selected_layer = iface.addVectorLayer(fn, '', 'ogr')


selectsoil_4 = ['Bleached-Mottled', 'Humosesquic', 'Friable']

fn = 'C:/temp/outputs/Grazing_land'
writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn, 'Input Soil layer', \driverName='ESRI Shapefile', selectsoil_3=True)

selected_layer = iface.addVectorLayer(fn, '', 'ogr')
