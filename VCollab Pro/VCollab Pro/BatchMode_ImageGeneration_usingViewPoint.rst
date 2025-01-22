Image Generation Using View Point
=================================

VCollab Pro users can generate an image from viewpoints of a CAX    
file in batch mode. The input is given through an XML file which    
consists of all the information to generate an image using          
viewpoint.                                                          
                                                                    
**Syntax:**                                                         
                                                                    
   Prompt :\VCollabPro.exe file folder> *VCollabPro.exe* -b <*input 
   xml file path*>                                                  
                                                                    
**Example:**                                                        
                                                                    
   C:\Program Files\VCollab\VCollabPro64> VCollabPro.exe -b         
   "C:\test\batch.xml"                                              
                                                                    
**Sample Batch File**                                               
                                                                    
   File Name: VCollabProBatch_ImageGen_ViewPtSel.xml                
                                                                    
   Location: "..\Samples\BatchMode Inputs\"                         


+----------------------------------------------------------------------+
| **<?xml version="1.0" encoding="utf-8" ?>**                          |
|                                                                      |
| <!-- BatchVersion 1.0 -->                                            |
|                                                                      |
| <!-- VCollab Pro : Allows batch mode execution using -b option from  |
| command line. -->                                                    |
|                                                                      |
| <!-- Sample Usage : C:\VCollabAppPath>VCollabPro.exe -b this.xml --> |
|                                                                      |
| <!-- Copyright (C) 2010 Visual Collaboration Technologies Inc. -->   |
|                                                                      |
| <!-- This xml format is alpha and it can be improved or changed by   |
| VCollab at the time of release VCollab Pro -->                       |
|                                                                      |
| <!-- Purpose : This sample explains, How to generate an image file   |
| for a specific view point -->                                        |
|                                                                      |
| **<VCollabBatch**                                                    |
|                                                                      |
|    **fVersion = "0.1"**                                              |
|                                                                      |
|    **sInputFile ="..\Samples\cax\airbag_viewpoints.cax" >**          |
|                                                                      |
|    <!-- iImageWidth, iImageHeight : are the width and height of the  |
|    image file in pixels. Minimum is 200x200. Maximum is size of      |
|    screen resolution -->                                             |
|                                                                      |
|    <!-- sOutPutImageFile : Output image file path. Only jpg, bmp,    |
|    png and tiff are supported -->                                    |
|                                                                      |
|    **<ImageGenerator ENABLE ="TRUE"**                                |
|                                                                      |
|    **iImageWidth ="600"**                                            |
|                                                                      |
|    **iImageHeight ="400"**                                           |
|                                                                      |
|    **sOutPutImageFile ="C:\output.jpg" />**                          |
|                                                                      |
|    <!-- sViewPointName : is the viewpoint that has to be exported as |
|    image -->                                                         |
|                                                                      |
|    <!-- sViewPathName : is the viewpath where the above viewpath     |
|    belongs in the list -->                                           |
|                                                                      |
|    **<SelectViewPoint ENABLE = "TRUE"**                              |
|                                                                      |
|    **sViewPointName = "Explode View"**                               |
|                                                                      |
|    **sViewPathName = "Path01" />**                                   |
|                                                                      |
|    <!-- These all are Optional blocks, Use only when required Or Set |
|    ENABLE as "FALSE" if that block need to be skipped -->            |
|                                                                      |
|    <!-- sInputViewPointFile is the external file that has viewpoints |
|    to be imported. Either it can cax or .vpt file -->                |
|                                                                      |
|    <!-- To Skip viewpoint state Set bApplyViewPointState = "FALSE"   |
|    -->                                                               |
|                                                                      |
|    **<ImportViewpoint ENABLE ="FALSE"**                              |
|                                                                      |
|    **sInputViewPointFile ="..\Samples\cax\airbag_viewpoints.vpt"**   |
|                                                                      |
|    **bApplyViewPointState ="TRUE" />**                               |
|                                                                      |
| **</VCollabBatch>**                                                  |
+----------------------------------------------------------------------+

**Dynamic Arguments**

Arguments for image generation from viewpoints can also be set
dynamically in batch mode. This feature is useful for repeated
operations without having to edit values in the input XML file.

The XML file is thus used as a template and its values are set
externally through command line arguments.

**E.g.**

C:\Program Files\VCollab\VCollabPro64> VCollabPro.exe -b
"C:\test\batch.xml" "..\Samples\cax\airbag.cax"
"..\Samples\cax\airbag_viewpoints.vpt" "C:\output.jpg" "Path01" "Explode
View"

In this example, the input CAX file, input viewpoint file, output image
file, viewpath name and viewpoint names have been provided dynamically.

The arguments are denoted as @arg#\ **N** where N is the index of the
argument in the command line. Dynamic arguments can be used in any field
and in any order, but @arg#\ **N** has to match with the command line
input index.

   In this example,

   @arg#0 = VCollabPro.exe

   @arg#1 = -b

   @arg#2 = C:/test/batch.xml

   @arg#3 = ..\Samples\BatchMode Inputs\airbag.cax which is assigned to
   sInputFile

   @arg#4 = ..\Samples\cax\airbag_viewpoints.vpt which is assigned to
   sInputViewPointFile

   @arg#5 = C:\output.jpg which is assigned to sOutPutImageFile

   @arg#6 = Path01 which is assigned to sViewPathName

   @arg#7 = Explode View which is assigned to sViewPointName

   **Modified XML**

   Fields that take values from command line arguments are highlighted.

+----------------------------------------------------------------------+
| **<**?xml version="1.0" encoding="utf-8" ?>                          |
|                                                                      |
| *<!-- BatchVersion 1.0 -->*                                          |
|                                                                      |
| *<!-- VCollab Pro : Allows batch mode execution using -b option from |
| command line. -->*                                                   |
|                                                                      |
| *<!-- Sample Usage : C:\VCollabAppPath>VCollabPro.exe -b this.xml    |
| -->*                                                                 |
|                                                                      |
| *<!-- Copyright (C) 2010 Visual Collaboration Technologies Inc. -->* |
|                                                                      |
| *<!-- This xml format is alpha and it can be improved or changed by  |
| VCollab at the time of release VCollab Pro -->*                      |
|                                                                      |
| *<!-- Purpose : This sample explains, How to generate an image file  |
| for a specific view point -->*                                       |
|                                                                      |
| <VCollabBatch                                                        |
|                                                                      |
|    fVersion = "0.1"                                                  |
|                                                                      |
|    sInputFile ="**@arg#3**" >                                        |
|                                                                      |
|    *<!-- iImageWidth, iImageHeight : are the width and height of the |
|    image file in pixels. Minimum is 200x200. Maximum is size of      |
|    screen resolution -->*                                            |
|                                                                      |
|    *<!-- sOutPutImageFile : Output image file path. Only jpg, bmp,   |
|    png and tiff are supported -->*                                   |
|                                                                      |
|    <ImageGenerator ENABLE ="TRUE"                                    |
|                                                                      |
|    iImageWidth ="600"                                                |
|                                                                      |
|    iImageHeight ="400"                                               |
|                                                                      |
|    sOutPutImageFile ="**@arg#5**" />                                 |
|                                                                      |
|    *<!-- sViewPointName : is the view point that has to be exported  |
|    as image -->*                                                     |
|                                                                      |
|    *<!-- sViewPathName : is the viewpath where the above viewpath    |
|    belongs in the list -->*                                          |
|                                                                      |
|    <SelectViewPoint ENABLE = "TRUE"                                  |
|                                                                      |
|    sViewPointName = "**@arg#7**"                                     |
|                                                                      |
|    sViewPathName = "**@arg#6"** />                                   |
|                                                                      |
|    *<!-- These all are Optional blocks, Use only when required Or    |
|    Set ENABLE as "FALSE" if that block need to be skipped -->*       |
|                                                                      |
|    *<!-- sInputViewPointFile is the external file that has           |
|    viewpoints to be imported. Either it can cax or .vpt file -->*    |
|                                                                      |
|    *<!-- To Skip viewpoint state Set bApplyViewPointState = "FALSE"  |
|    -->*                                                              |
|                                                                      |
|    <ImportViewpoint ENABLE ="FALSE"                                  |
|                                                                      |
|    sInputViewPointFile ="**@arg#4"**                                 |
|                                                                      |
|    bApplyViewPointState ="TRUE\ **" />**                             |
|                                                                      |
| </VCollabBatch>                                                      |
+----------------------------------------------------------------------+
