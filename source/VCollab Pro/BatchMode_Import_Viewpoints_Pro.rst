Import viewpoints from external file
====================================

This option helps user to import viewpoints of a cax file into another cax file. Input file is an xml file which consists of all the information to import viewpoints. Below is given the syntax and a sample xml batch file.
 
Syntax:                                                               

 Prompt :\VCollabPro.exe file folder> *VCollabPro.exe* -b <*input xml file path*>
                                                                       
 Example:                                                              
                                                                       
      C:\Program Files\VCollab\VCollabPro32> VCollabPro.exe -b "C:\test\batch.xml"
 
**Sample Batch File**                                                 

 File Name: VCollabProBatch_ImportViewPt.xml                       
 
 Location: "..\Samples\BatchMode Inputs\"                          
                                                                       
 +---------------------------------------------------------------+  
 |  | <?xml version="1.0" encoding="utf-8" ?>                    |
 |  | <!-- BatchVersion 1.0 -->                                  | 
 |  | <!-- VCollab Pro : Allows batch mode execution using -b    | 
 |    option from command line. -->                              | 
 |  | <!-- Sample Usage : C:\VCollabAppPath>VCollabPro.exe -b    |
 |    this.xml -->                                               |
 |  | <!-- Copyright (C) 2010 Visual Collaboration Technologies  |
 |    Inc. -->                                                   |
 |  | <!-- This xml format is alpha and it can be improved or    |
 |    changed by VCollab at the time of release VCollab Pro -->  |
 |  | <!-- Purpose : This sample explains, How to merge          |
 |    viewpoints from external file into a new cax file -->      |
 |  | <!-- Here, viewpoints from sInputViewPointFile are merged  |
 |    with sInputFile to create sOutputFile -->                  |
 |  | <VCollabBatch                                              |
 |                                                               |
 |      | fVersion = "0.1"                                       |
 |      | sInputFile = "..\Samples\BatchMode                     |
 |        Inputs\airbag.cax" >                                   |
 |      | <!-- sInputViewPointFile is the external file that has |
 |        viewpoints to be imported. Either it can cax or .vpt   |
 |        file-->                                                |
 |      | <!-- To Skip viewpoint state Set bApplyViewPointState  |
 |        = "FALSE" -->                                          |
 |      | <ImportViewpoint ENABLE = "TRUE"                       |
 |                                                               |
 |          | sInputViewPointFile = "..\Samples\BatchMode        |
 |            Inputs\airbag_viewpoints.vpt"                      |
 |          | bApplyViewPointState = "TRUE" />                   |
 |                                                               |
 |      | <!--sOutputFile is the merger of sInputFile and        |
 |        sInputViewPointFile-->                                 |
 |      | <Output sOutputFile = "C:\output.cax" />               |
 |                                                               |
 |  | </VCollabBatch>                                            |
 +---------------------------------------------------------------+                                            

**Dynamic Arguments**

                                                                       
 This section explains how to set values for xml fields through command line argument.
                                                                   
 Means, To do a fixed set of repeated operation, it is not needed to edit values in xml file .
                                                                   
 This XML files can be used as template and its values will be set from external command line arguments.
                                                                   
 E.g.                                                              
                                                                   
  *C:\Program Files\VCollab\VCollabPro32> VCollabPro.exe -b "C:\test\batch.xml" "..\Samples\BatchMode Inputs\airbag.cax" "..\Samples\BatchMode Inputs\airbag_viewpoints.vpt" "C:\output.cax"*
                                                                   
 This example sets values of xml fields in command arguments.     
                                                                   
 To input the command line arguments, xml fields need to to set as,                                                               
                                                                   
 sInputFile = "@arg#3"                                             
                                                                   
 sInputViewPointFile = "@arg#4"                                
                                                                   
 sOutputFile ="@arg#5"                                            
                                                                   
 The number is the index of command line argument list.            
                                                                   
 In this example,                                                  
                                                                   
 @arg#0 =VCollabPro.exe                                           
                                                                   
 @arg#1= -b                                                        
                                                                   
 @arg#2 = C:/test/batch.xml                                        
                                                                   
 @arg#3= ..\Samples\BatchMode Inputs\airbag.cax                    
                                                                   
 @arg#4=..\Samples\BatchMode Inputs\airbag_viewpoints.vpt          
                                                                   
 @arg#5=C:\output.cax                                              
                                                                   
 Modified xml                                                      
                                                                   
 Fields that takes values from command line arguments are          
 highlighted.                                                      
                                                                       
                                                                       
 +------------------------------------------------------------------+
 |     | <?xml version="1.0" encoding="utf-8" ?>                    |
 |     | <!-- BatchVersion 1.0 -->                                  |
 |     | <!-- VCollab Pro : Allows batch mode execution using -b    |
 |       option from command line. -->                              |
 |     | <!-- Sample Usage : C:\VCollabAppPath>VCollabPro.exe -b    |
 |       this.xml -->                                               |
 |     | <!-- Copyright (C) 2010 Visual Collaboration Technologies  |
 |       Inc. -->                                                   |
 |     | <!-- This xml format is alpha and it can be improved or    |
 |       changed by VCollab at the time of release VCollab Pro -->  |
 |     | <!-- Purpose : This sample explains, How to merge          |
 |       viewpoints from external file into a new cax file -->      |
 |     | <!-- Here, viewpoints from sInputViewPointFile are merged  |
 |       with sInputFile to create sOutputFile -->                  |
 |     | <VCollabBatch                                              |
 |                                                                  |
 |         | fVersion = "0.1"                                       |
 |         | sInputFile = "**@arg#3**" >                            |
 |         | <!-- sInputViewPointFile is the external file that has |
 |           viewpoints to be imported. Either it can cax or .vpt   |
 |           file-->                                                |
 |         | <!-- To Skip viewpoint state Set bApplyViewPointState  |
 |           = "FALSE" -->                                          |
 |         | <ImportViewpoint ENABLE = "TRUE"                       |
 |                                                                  |
 |             | sInputViewPointFile = "**@arg#4**"                 |
 |             | bApplyViewPointState = "TRUE" />                   |
 |                                                                  |
 |         | <!--sOutputFile is the merger of sInputFile and        |
 |           sInputViewPointFile-->                                 |
 |         | <Output sOutputFile = "**@arg#5**" />                  |
 |                                                                  |
 |     </VCollabBatch>                                              |
 |                                                                  |
 |                                                                  |
 +------------------------------------------------------------------+                                                                   
                                                                       
 *Note: Dynamic arguments can be used in any field and in any order, but @arg#\ *Number* has to match with command line input index.*                                                            

