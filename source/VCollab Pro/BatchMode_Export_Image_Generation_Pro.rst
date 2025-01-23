Image Generation
================

This option helps user to generate image from a cax file. Input file is an xml file which consists of all the information to generate image.

Below is given the syntax and a sample xml batch file.

**Syntax:**

 Prompt :\VCollabPro.exe file folder> *VCollabPro.exe* -b <*input xml file path*>

 Example:

  C:\Program Files\VCollab\VCollabPro32> VCollabPro.exe -b "C:\test\batch.xml"

**Sample Batch File - Basic**

    File Name: VCollabProBatch_ImageGen_Basic.xml

    Location: "..\Samples\BatchMode Inputs\"

    +------------------------------------------------------------------------+
    || <?xml version="1.0" encoding="utf-8" ?>                               |
    |                                                                        |
    || <!-- BatchVersion 1.0 -->                                             |
    |                                                                        |
    || <!-- VCollab Pro : Allows batch mode execution using -b option        |
    |  from command line. -->                                                |
    |                                                                        |
    || <!-- Sample Usage: C:\VCollabAppPath>VCollabPro.exe -b this.xml-->    |
    || <!-- Copyright (C) 2010 Visual Collaboration Technologies Inc.-->     |
    || <!-- This xml format is alpha and it can be improved or changed       |
    |  by VCollab at the time of release VCollab Pro -->                     |
    || <!-- Purpose : This sample explains, How to generate image files      |
    |  from cax in batch mode -->                                            |
    || <!-- Here, 'sInputFile' is the input cax file and*                    |
    |  'sOutPutImageFile' is the output image file.-->                       |
    || <!-- Only bmp, jpg,tiff and png are supported -->                     |
    |                                                                        |
    |                                                                        |
    || <VCollabBatch                                                         |
    | | fVersion = "0.1"                                                     |
    | | sInputFile = "..\Samples\BatchMode Inputs\bracket.cax" >             |
    |                                                                        |
    | | <!-- This ImagGenerator block specifics image width and              |
    |   height property in pixels and image file path-->                     |
    |                                                                        |
    |  | <ImageGenerator ENABLE ="TRUE"                                      |
    |                                                                        |
    |   | iImageWidth = "600"                                                |
    |                                                                        |
    |   | iImageHeight = "400"                                               |
    |                                                                        |
    |   | sOutPutImageFile = "C:\output.jpg" />                              |
    |                                                                        |
    |  | <!-- This SelectViewPoint block specifies the                       |
    |    viewpoint position to be applied -->                                |
    |                                                                        |
    |  | <!-- Default is Isometric. Other Options are "Front"                |
    |    "Rear" "Left" "Right" "Top" And "Bottom" -->                        |
    |                                                                        |
    |                                                                        |
    | | <SelectViewPoint ENABLE = "TRUE"                                     |
    |                                                                        |
    |  | sViewPointName = "Isometric"                                        |
    |                                                                        |
    |  | sViewPathName = "StandardViews" />                                  |
    |                                                                        |
    | | <!-- For more options, See                                           |
    |     VCollabProBatch_ImageGen_Advanced.xml -->                          |
    |                                                                        |
    || </VCollabBatch>                                                       |
    +------------------------------------------------------------------------+



**Dynamic Arguments**

    This section explains how to set values for xml fields through command line argument.

    Means, To do a fixed set of repeated operation, it is not needed to edit values in xml file .

    This XML files can be used as template and its values will be set from external command line arguments.

    E.g.

    *C:\Program Files\VCollab\VCollabPro32> VCollabPro.exe -b "C:\test\batch.xml" "..\Samples\BatchMode Inputs\bracket.cax" "C:\output.jpg" "Top"*

    This example sets values of xml fields in command arguments.

    To input the command line arguments, xml fields need to to set as,

    | sInputFile       = "@arg#3"
    | sOutPutImageFile = "@arg#4" 
    | sViewPointName = "@arg#5"

    Here, @arg# is required prefix followed by a number.

    The number is the index of command line argument list.

    In this example,

    @arg#0 =VCollabPro.exe

    @arg#1= -b

    @arg#2 = C:/test/batch.xml

    @arg#3= ..\Samples\BatchMode Inputs\bracket.cax

    @arg#4=C:\output.jpg

    @arg#5=Top

    **Modified xml**

    Fields that takes values from command line arguments are highlighted.
   

    +-----------------------------------------------------------------------+
    || <?xml version="1.0" encoding="utf-8" ?>                              |
    |                                                                       |
    || <!-- BatchVersion 1.0 -->                                            |
    |                                                                       |
    || <!-- VCollab Pro : Allows batch mode execution using -b option       |
    |  from command line. -->                                               |
    |                                                                       |
    || <!-- Sample Usage: C:\VCollabAppPath>VCollabPro.exe -b this.xml-->   |
    || <!-- Copyright (C) 2010 Visual Collaboration Technologies Inc.-->    |
    || <!-- This xml format is alpha and it can be improved or changed      |
    || by VCollab at the time of release VCollab Pro -->                    |
    || <!-- Purpose : This sample explains, How to generate image files     |
    || from cax in batch mode -->                                           |
    || <!-- Here, 'sInputFile' is the input cax file and                    |
    || 'sOutPutImageFile' is the output image file.-->                      |
    || <!--Only bmp, jpg,tiff and png are supported -->                     |
    |                                                                       |
    || <VCollabBatch                                                        |
    |                                                                       |
    | | fVersion = "0.1"                                                    |
    | | sInputFile = "\ **@arg#3**\ " >                                     |
    |                                                                       |
    | | <!-- This ImagGenerator block specifics image width and             |
    |   height property in pixels and image file path-->                    |
    |                                                                       |
    | | <ImageGenerator ENABLE ="TRUE"                                      |
    |                                                                       |
    |  | iImageWidth = "600"                                                |
    |  | iImageHeight = "400"                                               |
    |  | sOutPutImageFile = "**@arg#4**" />                                 |
    |                                                                       |
    |  | <!-- This SelectViewPoint block specifies the viewpoint            |
    |     position to be applied -->                                        |
    |                                                                       |
    |  | <!-- Default is Isometric. Other Options are "Front"               |
    |     "Rear" "Left" "Right" "Top" And "Bottom" -->                      |
    |                                                                       |
    |  | <SelectViewPoint ENABLE = "TRUE"                                   |
    |                                                                       |
    |   | sViewPointName = "**@arg#5**"                                     |
    |   | sViewPathName = "StandardViews" />                                |
    |                                                                       |
    |  | <!-- For more options, See                                         |
    |    VCollabProBatch_ImageGen_Advanced.xml -->                          |
    |                                                                       |
    || </VCollabBatch>                                                      |
    +-----------------------------------------------------------------------+

    Note: Dynamic arguments can be used in any field and in any order, but @arg#Number has to match with command line input index.

Sample Batch File - Advanced

    File Name: VCollabProBatch_ImageGen_Advanced.xml

    Location: "..\Samples\BatchMode Inputs\"

    It can be used with dynamic arguments also.

    +-----------------------------------------------------------------------+
    || <?xml version="1.0" encoding="utf-8" ?>                              |
    |                                                                       |
    || <!-- BatchVersion 1.0 -->                                            |
    |                                                                       |
    || <!-- VCollab Pro : Allows batch mode execution using -b option       |
    |  from command line. -->                                               |
    |                                                                       |
    || <!-- Sample Usage: C:\VCollabAppPath>VCollabPro.exe -b this.xml-->   |
    || <!-- Copyright (C) 2010 Visual Collaboration Technologies Inc.-->    |
    || <!-- This xml format is alpha and it can be improved or changed      |
    |  by VCollab at the time of release VCollab Pro -->                    |
    || <!-- Purpose : This sample explains, How to generate image files     |
    |  from cax in batch mode -->                                           |
    || <!-- Here, 'sInputFile' is the input cax file and                    |
    |  'sOutPutImageFile' is the output image file.                         |
    || Only bmp, jpg,tiff and png are supported -->                         |
    |                                                                       |
    || <VCollabBatch                                                        |
    |                                                                       |
    | | fVersion = "0.1"                                                    |
    | | sInputFile = "..\Samples\BatchMode Inputs\bracket.cax" >            |
    |                                                                       |
    | | <!-- This ImagGenerator block specifics image width and             |
    |    height property in pixels and image file path-->                   |
    |                                                                       |
    |                                                                       |
    | | <ImageGenerator ENABLE ="TRUE"                                      |
    |                                                                       |
    |  | iImageWidth = "600"                                                |
    |  | iImageHeight = "400"                                               |
    |  | sOutPutImageFile = "C:\output.jpg" />                              |
    |                                                                       |	
    | | <!-- These all are optional blocks, Use only when                   |
    |    required Or Set ENABLE as "FALSE" if that block need to            |
    |    be skipped -->                                                     |
    |                                                                       |
    | | <!-- This Background block specifies the background                 |
    |   color mode and background colors -->                                |
    | | <!-- Set 'bTextureMode' as TRUE to specify background to            |
    |   contain texture image -->                                           |
    |                                                                       |
    | | <Background ENABLE = "TRUE"                                         |
    |                                                                       |
    |  | fBackgroundTopColorRed = "0.0"                                     |
    |  | fBackgroundTopColorGreen = "0.5"                                   |
    |  | fBackgroundTopColorBlue = "1.0"                                    |
    |  | fBackgroundBottomColorRed = "0.5"                                  |
    |  | fBackgroundBottomColorGreen = "1.0"                                |
    |  | fBackgroundBottomColorBlue = "0.0"                                 |
    |  | bTextureMode = "FALSE"                                             |
    |                                                                       |
    |  | sBackgroundTextureFilePath = "..\Samples\BatchMode                 |
    |     Inputs\\texture.jpg" />                                           |
    |                                                                       |
    | | <!-- Set 'bAxis' as FALSE to remove axis display in the             |
    |         output image -->                                              |
    |                                                                       |
    | | <Display ENABLE = "TRUE"                                            |
    |                                                                       |
    |  | bAxis = "TRUE" />                                                  |
    |                                                                       |
    | | <CAE>                                                               |
    |                                                                       |
    |  | <!-- CAE Result fields specifies the result to be                  |
    |     selected for the image -->                                        |
    |                                                                       |
    |  | <!-- To use the default the result selection Set                   |
    |          ENABLE as "FALSE" -->                                        |
    |                                                                       |
    |   | <Result ENABLE ="TRUE"                                            |
    |                                                                       |
    |    | sResultName ="Displacement"                                      |
    |    | sInstance ="L2M1"                                                |
    |    | sDerivedType ="Translational X" />                               |
    |                                                                       |
    |    | <!-- CAE Legend settings can be applied using this               |
    |           CAESettings block. -->                                      |
    |    | <!-- To use the default settings set ENABLE as FALSE             |
    |            -->                                                        |
    |                                                                       |
    |    | <CAESettings ENABLE ="TRUE"                                      |
    |                                                                       |
    |     | bLegend ="TRUE"                                                 |
    |     | bColorPlot ="TRUE"                                              |
    |     | bReverseLegend ="FALSE"                                         |
    |     | bRangeMin ="TRUE"                                               |
    |     | fRangeMinValue ="0.5"                                           |
    |     | bRangeMax ="TRUE"                                               |
    |     | fRangeMaxValue ="3" />                                          |
    |                                                                       |
    | | </CAE>                                                              |
    |                                                                       |
    | | <!-- 'sInputViewPointFile; is the external file that has            |
    |   viewpoints to be imported. Either it can cax or .vpt*file-->        |
    | | <!-- To Skip viewpoint state Set bApplyViewPointState =             |
    |   "FALSE" -->                                                         |
    |                                                                       |
    | | <ImportViewpoint ENABLE = "TRUE"                                    |
    |                                                                       |
    |  | sInputViewPointFile = "..\Samples\BatchMode                        |
    |  | Inputs\beam.cax"                                                   |
    |  | bApplyViewPointState = "TRUE" />                                   |
    |                                                                       |
    | | <!-- This SelectViewPoint block specifies the                       |
    |    viewpoint position to be applied -->                               |
    |                                                                       |
    | | <!-- Default is Isometric. Other Options are "Front"                |
    |    "Rear" "Left" "Right" "Top" And "Bottom" -->                       |
    |                                                                       |
    | | <SelectViewPoint ENABLE = "TRUE"                                    |
    |                                                                       |
    |  | sViewPointName = "Isometric"                                       |
    |  | sViewPathName = "StandardViews" />                                 |
    |                                                                       |
    | | <!-- For more options, See                                          |
    |     VCollabProBatch_ImageGen_Advanced.xml -->                         |
    |                                                                       |
    || </VCollabBatch>                                                      |
    +-----------------------------------------------------------------------+

