Import Viewpoints
=================

VCollab Pro users can import viewpoints of a CAX file into another   
CAX file in batch mode. The input is given through an XML file which 
consists of all the information to import viewpoints.                
                                                                     
Syntax:                                                              
                                                                     
   Prompt :\VCollabPro.exe file folder> VCollabPro.exe -b <input xml 
   file path>                                                        
                                                                     
Example:                                                             
                                                                     
   C:\Program Files\VCollab\VCollabPro64> VCollabPro.exe -b          
   "C:\test\batch.xml"                                               
                                                                     
**Sample Batch File**                                                
                                                                     
   File Name: VCollabProBatch_ImportViewPt.xml                       
                                                                     
   Location: "..\Samples\BatchMode Inputs\"                          
                                                                     
+----------------------------------------------------------------+   
|    **<?xml version="1.0" encoding="utf-8" ?>**                 |   
|                                                                |   
|    *<!-- BatchVersion 1.0 -->*                                 |   
|                                                                |   
|    *<!-- VCollab Pro : Allows batch mode execution using -b    |   
|    option from command line. -->*                              |   
|                                                                |   
|    *<!-- Sample Usage : C:\VCollabAppPath>VCollabPro.exe -b    |   
|    this.xml -->*                                               |   
|                                                                |   
|    *<!-- Copyright (C) 2010 Visual Collaboration Technologies  |   
|    Inc. -->*                                                   |   
|                                                                |   
|    *<!-- This xml format is alpha and it can be improved or    |   
|    changed by VCollab at the time of release VCollab Pro -->*  |   
|                                                                |   
|    *<!-- Purpose : This sample explains, How to merge          |   
|    viewpoints from external file into a new cax file -->*      |   
|                                                                |   
|    *<!-- Here, viewpoints from sInputViewPointFile are merged  |   
|    with sInputFile to create sOutputFile -->*                  |   
|                                                                |   
|    **<VCollabBatch**                                           |   
|                                                                |   
|    **fVersion = "0.1"**                                        |   
|                                                                |   
|    **sInputFile = "..\Samples\BatchMode Inputs\airbag.cax" >** |   
|                                                                |   
|    *<!-- sInputViewPointFile is the external file that has     |   
|    viewpoints to be imported. Either it can cax or .vpt        |   
|    file-->*                                                    |   
|                                                                |   
|    *<!-- To Skip viewpoint state Set bApplyViewPointState =    |   
|    "FALSE" -->*                                                |   
|                                                                |   
|    **<ImportViewpoint ENABLE = "TRUE"**                        |   
|                                                                |   
|    **sInputViewPointFile = "..\Samples\BatchMode               |   
|    Inputs\airbag_viewpoints.vpt"**                             |   
|                                                                |   
|    **bApplyViewPointState = "TRUE" />**                        |   
|                                                                |   
|    *<!--sOutputFile is the merger of sInputFile and            |   
|    sInputViewPointFile-->*                                     |   
|                                                                |   
|    **<Output sOutputFile = "C:\output.cax" />**                |   
|                                                                |   
|    **</VCollabBatch>**                                         |   
+----------------------------------------------------------------+   
                                                                     
**Dynamic Arguments**                                                
                                                                     
 Arguments for importing viewpoints can also be set dynamically in    
 batch mode. This feature is useful for repeated operations without   
 having to edit values in the input XML file.                         
                                                                      
 The XML file is thus used as a template and its values are set       
 externally through command line arguments.                           
                                                                      
 E.g.                                                                 
                                                                      
 C:\Program Files\VCollab\VCollabPro64> VCollabPro.exe -b             
 "C:\test\batch.xml" "..\Samples\BatchMode Inputs\airbag.cax"         
 "..\Samples\BatchMode Inputs\airbag_viewpoints.vpt" "C:\output.cax"  
                                                                      
 In this example, the input CAX file, input viewpoint file and output 
 CAX file have been provided dynamically.                             
                                                                      
 The arguments are denoted as @arg#\ **N** where N is the index of    
 the argument in the command line. Dynamic arguments can be used in   
 any field and in any order, but @arg#\ **N** has to match with the   
 command line input index.                                            
                                                                      
 In this example,                                                     
                                                                      
 @arg#0 = VCollabPro.exe                                              
                                                                      
 @arg#1= -b                                                           
                                                                      
 @arg#2 = C:/test/batch.xml                                           
                                                                      
 @arg#3= ..\Samples\BatchMode Inputs\airbag.cax which is assigned to  
 sInputFile                                                           
                                                                      
 @arg#4=..\Samples\BatchMode Inputs\airbag_viewpoints.vpt which is    
 assigned to sInputViewPointFile                                      
                                                                      
 @arg#5=C:\output.cax which is assigned to sOutputFile                
                                                                      
 **Modified XML**
                                                                      
 Fields that take values from command line arguments are highlighted. 


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
 |    *<!-- Purpose : This sample explains, How to merge viewpoints     |
 |    from external file into a new cax file -->*                       |
 |                                                                      |
 |    *<!-- Here, viewpoints from sInputViewPointFile are merged with   |
 |    sInputFile to create sOutputFile -->*                             |
 |                                                                      |
 |    **<VCollabBatch**                                                 |
 |                                                                      |
 |    **fVersion = "0.1"**                                              |
 |                                                                      |
 |    **sInputFile = "@arg#3" >**                                       |
 |                                                                      |
 |    *<!-- sInputViewPointFile is the external file that has           |
 |    viewpoints to be imported. Either it can cax or .vpt file-->*     |
 |                                                                      |
 |    *<!-- To Skip viewpoint state Set bApplyViewPointState = "FALSE"  |
 |    -->*                                                              |
 |                                                                      |
 |    **<ImportViewpoint ENABLE = "TRUE"**                              |
 |                                                                      |
 |    **sInputViewPointFile = "@arg#4"**                                |
 |                                                                      |
 |    **bApplyViewPointState = "TRUE" />**                              |
 |                                                                      |
 |    *<!--sOutputFile is the merger of sInputFile and                  |
 |    sInputViewPointFile-->*                                           |
 |                                                                      |
 |    **<Output sOutputFile = "@arg#5" />**                             |
 |                                                                      |
 |    **</VCollabBatch>**                                               |
 +----------------------------------------------------------------------+

.. note::
 
 Dynamic arguments can be used in any field and in any order, but @arg#\ *Number* has to match with command line input index.
