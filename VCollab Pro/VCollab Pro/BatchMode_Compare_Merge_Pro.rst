Compare and Merge cax files
===========================

This option helps user to compare two cax model meshes and merge them into a single cax file with compared result as contour. Input file is an xml file which consists of all the information to merge.

**Syntax:**

 Prompt :\\VCollabPro.exe file folder> *VCollabPro.exe* -b  <*input xml file path*>

**Example:**

    C:\Program Files\VCollab\VCollabPro32> VCollabPro.exe -b
    "C:\test\batch.xml"

**Sample Batch File**

    File Name: VCollabProBatch_MergeCAX.xml

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
 |  | <!-- Purpose : This sample explains, How to merge two cax  |
 |    files, to compare both models and generate new cax with    |
 |    new compare result -->                                     |
 |  | <!-- Here fields, 'sInputFile' and 'sInputMergeCaxFile'    |
 |    are input cax files and 'sOutputFile' is the merged        |
 |    file-->                                                    |
 |  | <VCollabBatch                                              |
 |                                                               |
 |   | fVersion = "0.1"                                          |
 |   | sInputFile = "g:/Beam.cax" />                             |
 |                                                               |
 |   | <Output sOutputFile ="g:/ComparedBeam.cax" />             |
 |   | <!-- Merged file can be repositioned from its original    |
 |     coordinate system using ENABLE_TRANSLATION,               |
 |     ENABLE_ROTATION or ENABLE_SCALE -->                       |
 |   | <!-- Note : Set either 'bCombinedPalette' or              |
 |     'bMultiPalette' as TRUE at once, only if needed -->       |
 |   | <!-- Note : iMergePosition value is 0-AsIs; 1-left;       |
 |     2-right;3-top; 4-bottom; 5-Relative translate;            |
 |     6-Absolute posistion; Default is  0 -->                   |
 |   | <!-- Translation Rotation Scale will work only when       |
 |     iMergePosition="5" or "6" other wise they are ignored.--> |
 |   | <!-- New viewpath will be added as 'MergeAsNewDataset'    |
 |     with a viewpoint named 'Merge' in which all the CAE       |
 |     states will be retained.-->                               |
 |   | <MergeAsNewDataSet ENABLE = "TRUE"                        |
 |                                                               |
 |     | sInputMergeCaxFile = "g:/new_file.cax"                  |
 |     | bCombinedPalette = "FALSE"                              |
 |     | bMultiPalette = "FALSE"                                 |
 |     | bShowDataSetLabels = "TRUE"                             |
 |                                                               |
 |     | bApplyCurentSettings ="FALSE"                           |
 |     | iMergePosition="2"                                      |
 |     | ENABLE_TRANSLATION = "FALSE"                            |
 |     | fTranslationX = "3"                                     |
 |     | fTranslationY = "0"                                     |
 |     | fTranslationZ = "0"                                     |
 |     | ENABLE_ROTATION = "FALSE"                               |
 |     | fRotationX = "0"                                        |
 |     | fRotationY = "1"                                        |
 |     | fRotationZ = "0"                                        |
 |     | fRotationAngle = "0"                                    |
 |     | ENABLE_SCALE = "FALSE"                                  |
 |     | fScaleX = "1"                                           |
 |     | fScaleY = "1"                                           |
 |     | fScaleZ = "1" />                                        |
 |                                                               |
 |   | <!--The following option is to compare mesh/geometry      |
 |     first model with second model and to generate             |
 |     a result with the deviation -->                           |
 |   | <!--iCompare Mode varies from 0 to 2. 0 refers to         |
 |     same part comparision, 1 refers to visible parts          |
 |     comparison and 2 refers to all parts comparison -->       |
 |   | <!--iMaxDistance refers to maximum deviation considered   |
 |     for comparison -->                                        |
 |   | <!--bAddViewPoint (TRUE) adds current scene with          |
 |     deviation result color plot into viewpoint and save       |
 |     it to cax -->                                             |
 |   | <!--bSetPartMax (TRUE) applies part maximum deviation     |
 |     value to the color plot of the part. i.e. Each part       |
 |     will be of single contour color. -->                      |
 |                                                               |
 |   | <CompareMesh ENABLE = "TRUE"                              |
 |                                                               |
 |    | iCompareMode = "1"                                       |
 |    | fMaxDistance = "-1"                                      |
 |    | bAddViewPoint = "TRUE"                                   |
 |    | bSetPartMax = "FALSE"  />                                |
 |                                                               |
 |  | </VCollabBatch>                                            |
 +---------------------------------------------------------------+

**Dynamic Arguments**

 This section explains how to set values for xml fields through
 command line argument.

 i.e., to do a fixed set of repeated operation, it is not needed to
 edit values in xml file .

 This XML files can be used as template and its values will be set
 from external command line arguments.

 E.g.

 **C:\Program Files\VCollab\VCollabPro32> VCollabPro.exe -b
 "C:\test\batch.xml" "..\Samples\BatchMode Inputs\airbag.cax"
 "..\Samples\BatchMode Inputs\audi.cax" "C:\output.cax**"

 This example sets value of xml fields in command arguments.

 To input command line arguments, xml fields need to to set as,

 sInputFile = "@arg#3"
 
 sOutputFile ="@arg#5" 
 
 sInputMergeCaxFile = "@arg#4"

 Here, @arg# is required prefix followed by a number.

 The number is the index of command line argument list.

 In this example,

  @arg#0 =VCollabPro.exe
 
  @arg#1= -b
 
  @arg#2 = C:/test/batch.xml
 
  @arg#3= ..\Samples\BatchMode Inputs\airbag.cax
 
  @arg#4=..\Samples\BatchMode Inputs\audi.cax
 
  @arg#5=C:\output.cax


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
 |  | <!-- Purpose : This sample explains, How to merge two cax  |
 |    files, to compare both models and generate new cax with    |
 |    new compare result -->                                     |
 |  | <!-- Here fields, 'sInputFile' and 'sInputMergeCaxFile'    |
 |    are input cax files and 'sOutputFile' is the merged        |
 |    file-->                                                    |
 |  | <VCollabBatch                                              |
 |                                                               |
 |   | fVersion = "0.1"                                          |
 |   | sInputFile = **"@arg#3"** />                              |
 |                                                               |
 |   | <Output sOutputFile ="g:/ComparedBeam.cax" />             |
 |   | <!-- Merged file can be repositioned from its original    |
 |     coordinate system using ENABLE_TRANSLATION,               |
 |     ENABLE_ROTATION or ENABLE_SCALE -->                       |
 |   | <!-- Note : Set either 'bCombinedPalette' or              |
 |     'bMultiPalette' as TRUE at once, only if needed -->       |
 |   | <!-- Note : iMergePosition value is 0-AsIs; 1-left;       |
 |     2-right;3-top; 4-bottom; 5-Relative translate;            |
 |     6-Absolute posistion; Default is  0 -->                   |
 |   | <!-- Translation Rotation Scale will work only when       |
 |     iMergePosition="5" or "6" other wise they are ignored.--> |
 |   | <!-- New viewpath will be added as 'MergeAsNewDataset'    |
 |     with a viewpoint named 'Merge' in which all the CAE       |
 |     states will be retained.-->                               |
 |   | <MergeAsNewDataSet ENABLE = "TRUE"                        |
 |                                                               |
 |     | sInputMergeCaxFile = **"@arg#4"**                       |
 |     | bCombinedPalette = "FALSE"                              |
 |     | bMultiPalette = "FALSE"                                 |
 |     | bShowDataSetLabels = "TRUE"                             |
 |                                                               |
 |     | bApplyCurentSettings ="FALSE"                           |
 |     | iMergePosition="2"                                      |
 |     | ENABLE_TRANSLATION = "FALSE"                            |
 |     | fTranslationX = "3"                                     |
 |     | fTranslationY = "0"                                     |
 |     | fTranslationZ = "0"                                     |
 |     | ENABLE_ROTATION = "FALSE"                               |
 |     | fRotationX = "0"                                        |
 |     | fRotationY = "1"                                        |
 |     | fRotationZ = "0"                                        |
 |     | fRotationAngle = "0"                                    |
 |     | ENABLE_SCALE = "FALSE"                                  |
 |     | fScaleX = "1"                                           |
 |     | fScaleY = "1"                                           |
 |     | fScaleZ = "1" />                                        |
 |                                                               |
 |   | <!--The following option is to compare mesh/geometry      |
 |     first model with second model and to generate             |
 |     a result with the deviation -->                           |
 |   | <!--iCompare Mode varies from 0 to 2. 0 refers to         |
 |     same part comparision, 1 refers to visible parts          |
 |     comparison and 2 refers to all parts comparison -->       |
 |   | <!--iMaxDistance refers to maximum deviation considered   |
 |     for comparison -->                                        |
 |   | <!--bAddViewPoint (TRUE) adds current scene with          |
 |     deviation result color plot into viewpoint and save       |
 |     it to cax -->                                             |
 |   | <!--bSetPartMax (TRUE) applies part maximum deviation     |
 |     value to the color plot of the part. i.e. Each part       |
 |     will be of single contour color. -->                      |
 |                                                               |
 |   | <CompareMesh ENABLE = "TRUE"                              |
 |                                                               |
 |    | iCompareMode = "1"                                       |
 |    | fMaxDistance = "-1"                                      |
 |    | bAddViewPoint = "TRUE"                                   |
 |    | bSetPartMax = "FALSE"  />                                |
 |                                                               |
 |  | </VCollabBatch>                                            |
 +---------------------------------------------------------------+

 Note: Dynamic arguments can be used in any field and in any order, but @arg#\ *Number* has to match with command line input index.
