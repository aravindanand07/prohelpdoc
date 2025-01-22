Image Generation in Batch Mode
================================

 VCollab Pro users can generate an image from a CAX file in      
 batch mode.The input is given through an XML file which        
 consists of all the information to generate an image.           
                                                                
 Syntax:                                                         
                                                                
    Prompt :\VCollabPro.exe file folder> VCollabPro.exe -b       
    <input xml file path>                                       
                                                                
 Example:                                                       
                                                                
    C:\Program Files\VCollab\VCollabPro64> VCollabPro.exe -b    
    "C:\test\batch.xml"                                          

 **Sample Batch File - Basic**                                   
                                                                
    File Name: VCollabProBatch_ImageGen_Basic.xml                
                                                                 
    Location: "..\Samples\BatchMode Inputs\"                    

+----------------------------------------------------------------------+
|    **<?xml version="1.0" encoding="utf-8" ?>**                       |
|                                                                      |
|    *<!-- BatchVersion 1.0 -->*                                       |
|                                                                      |
|    *<!-- VCollab Pro : Allows batch mode execution using -b option   |
|    from command line. -->*                                           |
|                                                                      |
|    *<!-- Sample Usage : C:\VCollabAppPath>VCollabPro.exe -b          |
|    this.xml -->*                                                     |
|                                                                      |
|    *<!-- Copyright (C) 2010 Visual Collaboration Technologies Inc.   |
|    -->*                                                              |
|                                                                      |
|    *<!-- This xml format is alpha and it can be improved or changed  |
|    by VCollab at the time of release VCollab Pro -->*                |
|                                                                      |
|    *<!-- Purpose : This sample explains, How to generate image       |
|    files from cax in batch mode -->*                                 |
|                                                                      |
|    *<!-- Here, 'sInputFile' is the input cax file and                |
|    'sOutPutImageFile' is the output image file. Only bmp, jpg, tiff  |
|    and png are supported -->*                                        |
|                                                                      |
|    **<VCollabBatch**                                                 |
|                                                                      |
|    **fVersion = "0.1"**                                              |
|                                                                      |
|    **sInputFile = "..\Samples\BatchMode Inputs\bracket.cax" >**      |
|                                                                      |
|    *<!-- This ImagGenerator block specifics image width and height   |
|    property in pixels and image file path-->*                        |
|                                                                      |
|    **<ImageGenerator ENABLE ="TRUE"**                                |
|                                                                      |
|    **iImageWidth = "600"**                                           |
|                                                                      |
|    **iImageHeight = "400"**                                          |
|                                                                      |
|    **sOutPutImageFile = "C:\output.jpg" />**                         |
|                                                                      |
|    *<!-- This SelectViewPoint block specifies the viewpoint          |
|    position to be applied -->*                                       |
|                                                                      |
|    *<!-- Default is Isometric. Other Options are "Front" "Rear"      |
|    "Left" "Right" "Top" And "Bottom" -->*                            |
|                                                                      |
|    **<SelectViewPoint ENABLE = "TRUE"**                              |
|                                                                      |
|    **sViewPointName = "Isometric"**                                  |
|                                                                      |
|    **sViewPathName = "StandardViews" />**                            |
|                                                                      |
|    *<!-- For more options, See                                       |
|    VCollabProBatch_ImageGen_Advanced.xml -->*                        |
|                                                                      |
|    **</VCollabBatch>**                                               |
+----------------------------------------------------------------------+


 **Dynamic Arguments**                                           
                                                                 
 Arguments for image generation can also be set dynamically in   
 batch mode. This feature is useful for repeated operations     
 without having to edit values in the input XML file.           
                                                                
 The XML file is thus used as a template and its values are set
 externally through command line arguments.                      
                                                                
 E.g. C:\Program Files\VCollab\VCollabPro64> VCollabPro.exe -b  
 "C:\test\batch.xml" "..\Samples\BatchMode Inputs\bracket.cax"   
 "C:\output.jpg" "Top"                                           
                                                                
 In this example, the input CAX file, output image file and     
 viewpoint names have been provided dynamically.                
                                                                
 The arguments are denoted as @arg#\ **N** where N is the index  
 of the argument in the command line. Dynamic arguments can be   
 used in any field and in any order, but @arg#\ **N** has to     
 match with the command line input index.                        
                                                                
 In this example,     
 
  @arg#0 = VCollabPro.exe                                     
                                                               
  @arg#1= -b                                                   
                                                                 
  @arg#2 = C:/test/batch.xml|                                                                   
  @arg#3= ..\Samples\BatchMode Inputs\bracket.cax which is     
  assigned to sInputFile                                       

  @arg#4=C:\output.jpg which is assigned to sOutPutImageFile  
                                                                 
  @arg#5=Top which is assigned to sViewPointName              
                                                                
 **Modified XML**                                            
                                                                 
  Fields that take values from command line arguments are      
  highlighted.                                                
                                                                
  +-----------------------------------------------------------+  
  |    **<?xml version="1.0" encoding="utf-8" ?>**            |   
  |                                                           | 
  |    *<!-- BatchVersion 1.0 -->*                            |  
  |                                                           |  
  |    *<!-- VCollab Pro : Allows batch mode execution using  |  
  |    -b option from command line. -->*                      |  
  |                                                           |  
  |    *<!-- Sample Usage : C:\VCollabAppPath>VCollabPro.exe  |  
  |    -b this.xml -->*                                       |  
  |                                                           | 
  |    *<!-- Copyright (C) 2010 Visual Collaboration          |  
  |    Technologies Inc. -->*                                 |  
  |                                                           |  
  |    *<!-- Purpose : This sample explains, How to generate  |  
  |    image files from cax in batch mode -->*                | 
  |                                                           | 
  |    *<!-- Here, 'sInputFile' is the input cax file and     |  
  |    'sOutPutImageFile' is the output image file. Only bmp, | 
  |    jpg, tiff and png are supported -->*                   |   
  |                                                           |  
  |    **<VCollabBatch**                                      |  
  |                                                           |  
  |    **fVersion = "0.1"**                                   | 
  |                                                           |
  |    **sInputFile = "@arg#3" >**                            | 
  |                                                           |  
  |    *<!-- This ImagGenerator block specifics image width   |  
  |    and height property in pixels and image file path-->*  |   
  |                                                           |  
  |    **<ImageGenerator ENABLE ="TRUE"**                     | 
  |                                                           |  
  |    **iImageWidth = "600"**                                |  
  |                                                           |  
  |    **iImageHeight = "400"**                               |  
  |                                                           |  
  |    **sOutPutImageFile = "@arg#4" />**                     |  
  |                                                           |   
  |    *<!-- This SelectViewPoint block specifies the         |  
  |    viewpoint position to be applied -->*                  |  
  |                                                           |   
  |    *<!-- Default is Isometric. Other Options are "Front"  |   
  |    "Rear" "Left" "Right" "Top" And "Bottom" -->*          |  
  |                                                           |  
  |    **<SelectViewPoint ENABLE = "TRUE"**                   |  
  |                                                           |  
  |    **sViewPointName = "@arg#5"**                          |  
  |                                                           |  
  |    **sViewPathName = "StandardViews" />**                 |  
  |                                                           | 
  |    *<!-- For more options, See                            |  
  |    VCollabProBatch_ImageGen_Advanced.xml -->*             | 
  |                                                           |  
  |    **</VCollabBatch>**                                    |  
  +-----------------------------------------------------------+  


**Sample Batch File - Advanced**                             
                                                             
   File Name: VCollabProBatch_ImageGen_Advanced.xml          
                                                             
   Location: "..\Samples\BatchMode Inputs\"                  
                                                             
   This file can also be used with dynamic arguments.        
                                                             
+-----------------------------------------------------------+
|    **<?xml version="1.0" encoding="utf-8" ?>**            |
|                                                           |
|    *<!-- BatchVersion 1.0 -->*                            |
|                                                           |
|    *<!-- VCollab Pro : Allows batch mode execution using  |
|    -b option from command line. -->*                      |
|                                                           |
|    *<!-- Sample Usage : C:\VCollabAppPath>VCollabPro.exe  |
|    -b this.xml -->*                                       |
|                                                           |
|    *<!-- Copyright (C) 2010 Visual Collaboration          |
|    Technologies Inc. -->*                                 |
|                                                           |
|    *<!-- This xml format is alpha and it can be improved  |
|    or changed by VCollab at the time of release           |
|    VCollabPro -->*                                        |
|                                                           |
|    *<!-- Purpose : This sample explains, How to generate  |
|    image files from cax in batch mode -->*                |
|                                                           |
|    *<!-- Here, 'sInputFile' is the input cax file and     |
|    'sOutPutImageFile' is the output image file. Only bmp, |
|    jpg, tiff and png are supported -->*                   |
|                                                           |
|    **<VCollabBatch**                                      |
|                                                           |
|    **fVersion = "0.1"**                                   |
|                                                           |
|    **sInputFile = "..\Samples\BatchMode                   |
|    Inputs\bracket.cax" >**                                |
|                                                           |
|    *<!-- This ImagGenerator block specifics image width   |
|    and height property in pixels and image file path-->*  |
|                                                           |
|    **<ImageGenerator ENABLE ="TRUE"**                     |
|                                                           |
|    **iImageWidth = "600"**                                |
|                                                           |
|    **iImageHeight = "400"**                               |
|                                                           |
|    **sOutPutImageFile = "C:\output.jpg" />**              |
|                                                           |
|    *<!-- These all are optional blocks, Use only when     |
|    required Or Set ENABLE as "FALSE" if that block need   |
|    to be skipped -->*                                     |
|                                                           |
|    *<!-- This Background block specifies the background   |
|    color mode and background colors -->*                  |
|                                                           |
|    *<!-- Set 'bTextureMode' as TRUE to specify            |
|    background to contain texture image -->*               |
|                                                           |
|    **<Background ENABLE = "TRUE"**                        |
|                                                           |
|    **fBackgroundTopColorRed = "0.0"**                     |
|                                                           |
|    **fBackgroundTopColorGreen = "0.5"**                   |
|                                                           |
|    **fBackgroundTopColorBlue = "1.0"**                    |
|                                                           |
|    **fBackgroundBottomColorRed = "0.5"**                  |
|                                                           |
|    **fBackgroundBottomColorGreen = "1.0"**                |
|                                                           |
|    **fBackgroundBottomColorBlue = "0.0"**                 |
|                                                           |
|    **bTextureMode = "FALSE"**                             |
|                                                           |
|    **sBackgroundTextureFilePath = "..\Samples\BatchMode   |
|    Inputs\texture.jpg" />**                               |
|                                                           |
|    *<!-- Set 'bAxis' as FALSE to remove axis display in   |
|    the output image -->*                                  |
|                                                           |
|    **<Display ENABLE = "TRUE"**                           |
|                                                           |
|    **bAxis = "TRUE" />**                                  |
|                                                           |
|    **<CAE>**                                              |
|                                                           |
|    *<!-- CAE Result fields specifies the result to be     |
|    selected for the image -->*                            |
|                                                           |
|    *<!-- To use the default the result selection Set      |
|    ENABLE as "FALSE" -->*                                 |
|                                                           |
|    **<Result ENABLE ="TRUE"**                             |
|                                                           |
|    **sResultName ="Displacement"**                        |
|                                                           |
|    **sInstance ="L2M1"**                                  |
|                                                           |
|    **sDerivedType ="Translational X" />**                 |
|                                                           |
|    *<!-- CAE Legend settings can be applied using this    |
|    CAESettings block. -->*                                |
|                                                           |
|    *<!-- To use the default settings set ENABLE as FALSE  |
|    -->*                                                   |
|                                                           |
|    **<CAESettings ENABLE ="TRUE"**                        |
|                                                           |
|    **bLegend ="TRUE"**                                    |
|                                                           |
|    **bColorPlot ="TRUE"**                                 |
|                                                           |
|    **bReverseLegend ="FALSE"**                            |
|                                                           |
|    **bRangeMin ="TRUE"**                                  |
|                                                           |
|    **fRangeMinValue ="0.5"**                              |
|                                                           |
|    **bRangeMax ="TRUE"**                                  |
|                                                           |
|    **fRangeMaxValue ="3" />**                             |
|                                                           |
|    **</CAE>**                                             |
|                                                           |
|    *<!-- 'sInputViewPointFile; is the external file that  |
|    has viewpoints to be imported. Either it can cax or    |
|    .vpt file-->*                                          |
|                                                           |
|    *<!-- To Skip viewpoint state Set                      |
|    bApplyViewPointState = "FALSE" -->*                    |
|                                                           |
|    **<ImportViewpoint ENABLE = "TRUE"**                   |
|                                                           |
|    **sInputViewPointFile = "..\Samples\BatchMode          |
|    Inputs\beam.cax"**                                     |
|                                                           |
|    **bApplyViewPointState = "TRUE" />**                   |
|                                                           |
|    *<!-- This SelectViewPoint block specifies the         |
|    viewpoint position to be applied -->*                  |
|                                                           |
|    **<SelectViewPoint ENABLE = "TRUE"**                   |
|                                                           |
|    **sViewPointName = "Isometric"**                       |
|                                                           |
|    **sViewPathName = "StandardViews" />**                 |
|                                                           |
|    **</VCollabBatch>**                                    |
+-----------------------------------------------------------+
