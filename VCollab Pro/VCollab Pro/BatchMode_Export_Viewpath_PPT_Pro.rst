Generate MS-Power Point file for viewpoints
===========================================

This option helps user to export viewpoints of a cax file into another ppt file. Input file is an xml file which consists of all the information to export viewpoints into a PPT file. Below is given the syntax and a sample xml batch file.

**Syntax:**

 Prompt :\VCollabPro.exe file folder> *VCollabPro.exe* -b <*input xml file path*>

Example:

 C:\Program Files\VCollab\VCollabPro32> VCollabPro.exe -b  "C:\test\batch.xml"
   


**Sample Batch File - Basic**

 File Name: VCollabProBatch_ViewPt2PPT_Basic.xml

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
 |  | <!-- Purpose : This sample explains, How to generate       |
 |    MS-PowerPoint PPT files from VCollab Pro application       |
 |    in batch mode -->                                          |
 |  | <!-- Here, each viewpoints in cax file are exported as     |
 |    PowerPoint slide -->                                       |
 |  | <VCollabBatch                                              |
 |                                                               |
 |      | fVersion = "0.1"                                       |
 |      | sInputFile = "..\\Samples\\BatchMode Inputs\\          |
 |        cylinder.cax"  >                                       |
 |      | <!-- sPPtTemplatePath is PowerPoint template (.pot)    |
 |        file path. If there is no PowerPoint template          |
 |        input then set bUsePptTemplate="FALSE" -->             |
 |      | <!-- To Skip viewpoint state Set bApplyViewPointState  |
 |        = "FALSE" -->                                          |
 |      | <ViewPoint2PPT ENABLE = "TRUE"                         |
 |                                                               |
 |          | sOutputPPTPath = "C:\\output.ppt"                  |
 |          | bUsePptTemplate = "TRUE"                           |
 |          | sPPtTemplatePath = "..\\Samples\\BatchMode         |
 |           Inputs\\template.pot"                               |
 |                                                               |
 |      | <!--For more options, See                              |
 |        VCollabProBatch_ViewPt2PPT_Advanced.xml-->             |
 |                                                               |
 |  | </VCollabBatch>                                            |
 +---------------------------------------------------------------+

**Dynamic Arguments**

 This section explains how to set values for xml fields through
 command line argument.

 Means, To do a fixed set of repeated operation, it is not needed to
 edit values in xml file .

 This XML files can be used as template and its values will be set
 from external command line arguments.

 E.g.

  C:\Program Files\VCollab\VCollabPro32> VCollabPro.exe -b 
  "C:\test\batch.xml" "..\Samples\BatchMode Inputs\cylinder.cax"
  "..\Samples\BatchMode Inputs\template.pot" "C:\output.ppt"

 This examples sets values of xml fields in command arguments.

 To input the command line arguments, xml fields need to to set as,

 | sInputFile = "@arg#3"
 | sPPtTemplatePath ="@arg#4" 
 | sOutputPPTPath = "@arg#5"

 Here, @arg# is required prefix followed by a number.

 The number is the index of command line argument list.

 In this example,

  @arg#0 =VCollabPro.exe
 
  @arg#1 = -b
 
  @arg#2 = C:/test/batch.xml
 
  @arg#3 = ..\Samples\BatchMode Inputs\cylinder.cax
 
  @arg#4 = ..\Samples\BatchMode Inputs\template.pot
 
  @arg#5 = C:\output.ppt


**Modified xml**


 Fields that takes values from command line arguments are highlighted.
 
 
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
 |  | <!-- Purpose : This sample explains, How to generate       |
 |    MS-PowerPoint PPT files from VCollab Pro application       |
 |    in batch mode -->                                          |
 |  | <!-- Here, each viewpoints in cax file are exported as     |
 |    PowerPoint slide -->                                       |
 |  | <VCollabBatch                                              |
 |                                                               |
 |      | fVersion = "0.1"                                       |
 |      | sInputFile = **@arg#3**                                |
 |      | <!-- sPPtTemplatePath is PowerPoint template (.pot)    |
 |        file path. If there is no PowerPoint template          |
 |        input then set bUsePptTemplate="FALSE" -->             |
 |      | <!-- To Skip viewpoint state Set bApplyViewPointState  |
 |        = "FALSE" -->                                          |
 |      | <ViewPoint2PPT ENABLE = "TRUE"                         |
 |                                                               |
 |          | sOutputPPTPath = **@arg#5**                        |
 |          | bUsePptTemplate = "TRUE"                           |
 |          | sPPtTemplatePath = **@arg#4**                      |
 |                                                               |
 |      | <!--For more options, See                              |
 |        VCollabProBatch_ViewPt2PPT_Advanced.xml-->             |
 |                                                               |
 |  | </VCollabBatch>                                            |                    
 +---------------------------------------------------------------+

 Note: Dynamic arguments can be used in any field and in any order, but @arg#\ *Number* has to match with command line input index.



**Sample Batch File - Advanced**

 File Name: VCollabProBatch_ViewPt2PPT_Advanced.xml

 Location: "..\Samples\BatchMode Inputs\"

 It can be used with dynamic arguments also.

 
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
 |  | <!-- Purpose : This sample explains, How to generate       |
 |    MS-PowerPoint PPT files from VCollab Pro application       |
 |    in batch mode -->                                          |
 |  | <!-- Here, each viewpoints in cax file are exported as     |
 |    PowerPoint slide -->                                       |
 |  | <VCollabBatch                                              |
 |                                                               |
 |      | fVersion = "0.1"                                       |
 |      | sInputFile = "..\\Samples\\BatchMode                   |
 |           Inputs\\AirBag_Displacement.cax" >                  |
 |      | <!-- sPPtTemplatePath is PowerPoint template (.pot)    |
 |        file path. If there is no PowerPoint template          |
 |        input then set bUsePptTemplate="FALSE" -->             |
 |      | <!-- To Skip viewpoint state Set bApplyViewPointState  |
 |        = "FALSE" -->                                          |
 |      | <ViewPoint2PPT ENABLE = "TRUE"                         |
 |                                                               |
 |        | sOutputPPTPath = "C:\AirBagDisplacement.ppt"         |
 |        | bUsePptTemplate = "TRUE"                             |
 |        | sPPtTemplatePath = "..\Samples\BatchMode             |
 |          Inputs\VCollabTemplate.pot" />                       |
 |                                                               |
 |      | <!--On all these Optional blocks, Set ENABLE as        |
 |        "FALSE", if that block need to be skipped -->          |
 |      | <!--Optional Block is Used to import viewpoint         |
 |        from external cax/vpt file -->                         |
 |      | <!--To skip state of the viewpoint then Set            |
 |        bImportViewPointState as "FALSE". So that only         |
 |        camera position imported -->                           |
 |                                                               |
 |      | <ImportViewpoint ENABLE = "TRUE"                       |
 |                                                               |
 |       | sInputViewPointFile = "..\\Samples\\BatchMode         |
 |         Inputs\AirBag_ViewPoints.vpt"                         |
 |       | bImportViewPointState = "TRUE" />                     |
 |                                                               |
 |      | <!--The above sample bImportViewPointState is set to   |
 |        FALSE, means the view state is skipped and only camera |
 |        positions will be applied-->                           |
 |      | <!--try the other sample to import viewpoint state.    |
 |        sInputViewPointFile="..\\Samples\\BatchMode Inputs\\   |
 |        AirBag_AllResults.cax" and bImportViewPointState       |
 |        ="TRUE" -->                                            |
 |      | <!--Optional Select Viewpoint Block -->                |
 |      | <!--SelectViewPoint block is used if there exists more |
 |        than one viewpath. Select a viewpath that has to be    |
 |        exported as ppt slides or First path will be           |
 |        exported -->                                           |
 |                                                               |
 |      | <SelectViewPoint ENABLE = "TRUE" sViewPathName =       |
 |        "ViewPath1" />                                         |
 |                                                               |
 |  | </VCollabBatch>                                            |
 +---------------------------------------------------------------+
 
