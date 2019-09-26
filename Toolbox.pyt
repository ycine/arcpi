import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class Tool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Tool"
        self.description = "To printuje wszystkie warstwy jakie sa zawarte w tym pliku mxd. ale to nie wyswietli nic :P"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter()
        param0.name = "Parameter0"
        param0.displayName = "Plik mxd"
        param0.parameterType = "Required"
        param0.direction = "Input"
        param0.datatype = "ArcMap Document"
        return [param0]

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""

        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        #test = arcpy.Parameter('param0','DISPLAY NAME', 'Input', 'ArcMap Document', 'Required')

        inFeatures = parameters[0].valueAsText
        mxd = arcpy.mapping.MapDocument(inFeatures)
        mxd1 = arcpy.mapping.ListLayers(mxd)
        arcpy.AddMessage("WARSTWY:")
        for i in mxd1:
            arcpy.AddMessage(i.name)

        arcpy.AddMessage('Zakonczono.')

        return
