Comparing and Merging CAX files
===============================

VCollab Pro users can compare two CAX model meshes and merge  
them into a single CAX file in batch mode. The compared result
is in the form of a contour. The input is given through an XML
file which consists of all the information to merge the CAX   
files.                                                        
                                                              
Syntax:                                                       
                                                              
   Prompt :\VCollabPro.exe file folder> *VCollabPro.exe* -b   
   <*input xml file path*>                                    
                                                              
Example:                                                      
                                                              
   C:\Program Files\VCollab\VCollabPro64> VCollabPro.exe -b   
   "C:\test\batch.xml"                                       

**Sample Batch File**                                        
                                                             
   File Name: VCollabProBatch_MergeCAX.xml                   
                                                             
   Location: "..\Samples\BatchMode Inputs\\\"
                                                             
+-----------------------------------------------------------+
| <?xml version="1.0" encoding="utf-8" ?>                   |
|                                                           |
| <!-- Purpose : This sample explains how to merge two cax  |
| files, to compare both models and generate new cax with   |
| new compare result-->                                     |
|                                                           |
| <!-- Here the fields, 'sInputFile' and                    |
| 'sInputMergeCaxFile' are input cax files and              |
| 'sOutputFile' is the merged file -->                      |
|                                                           |
| <VCollabBatch fVersion = "0.1"                            |
|                                                           |
|    sInputFile = "g:/Beam.cax" >                           |
|                                                           |
|    <Output sOutputFile ="g:/ComparedBeam.cax" />          |
|                                                           |
| <!-- Merged file can be repositioned from its original    |
| coordinate system using ENABLE_TRANSLATION,               |
| ENABLE_ROTATION or ENABLE_SCALE -->                       |
|                                                           |
| <!-- Note : Set either 'bCombinedPalette' or              |
| 'bMultiPalette' as TRUE at once, only if needed -->       |
|                                                           |
| <!-- Note iMergePosition value is 0-AsIs; 1-left;         |
| 2-right; 3-top; 4-bottom; 5-Relative translate;           |
| 6-Absolute position; Default is 0-->                      |
|                                                           |
| <!-- Translation Rotation Scale will work only when       |
| iMergePosition="5" or "6" otherwise they are ignored.-->  |
|                                                           |
| <!-- New viewpath will be added as 'MergeAsNewDataset'    |
| with a viewpoint named 'Merge' in which all the CAE       |
| states will be retained.\`-->                             |
|                                                           |
|                                                           |
| <MergeAsNewDataSet ENABLE = "TRUE"                        |
|                                                           |
|    sInputMergeCaxFile = "g:/new_file.cax"                 |
|                                                           |
|    bCombinedPalette = "FALSE"                             |
|                                                           |
|    bMultiPalette = "FALSE"                                |
|                                                           |
|    bShowDataSetLabels= "TRUE"                             |
|                                                           |
|    bApplyCurentSettings ="FALSE"                          |
|                                                           |
|    iMergePosition="2"                                     |
|                                                           |
|    ENABLE_TRANSLATION = "FALSE"                           |
|                                                           |
|    fTranslationX = "3"                                    |
|                                                           |
|    fTranslationY = "0"                                    |
|                                                           |
|    fTranslationZ = "0"                                    |
|                                                           |
|    ENABLE_ROTATION = "FALSE"                              |
|                                                           |
|    fRotationX = "0"                                       |
|                                                           |
|    fRotationY = "1"                                       |
|                                                           |
|    fRotationZ = "0"                                       |
|                                                           |
|    fRotationAngle = "0"                                   |
|                                                           |
|    ENABLE_SCALE = "FALSE"                                 |
|                                                           |
|    fScaleX = "1"                                          |
|                                                           |
|    fScaleY = "1"                                          |
|                                                           |
|    fScaleZ = "1"                                          |
|                                                           |
|    />                                                     |
|                                                           |
| <!--The following option is to compare mesh/geometry      |
| first model with second model and to generate a result    |
| with the deviation -->                                    |
|                                                           |
| <!-- iCompare Mode varies from 0 to 2. 0 refers to same   |
| part comparison, 1 refers to visible parts comparison and |
| 2 refers to all parts comparison -->                      |
|                                                           |
| <!-- iMaxDistance refers to maximum deviation considered  |
| for comparison -->                                        |
|                                                           |
| <!-- bAddViewPoint (TRUE) adds current scene with         |
| deviation result color plot into viewpoint and save it to |
| cax -->                                                   |
|                                                           |
| <!-- bSetPartMax (TRUE) applies part maximum deviation    |
| value to the color plot of the part. i.e. Each part will  |
| be of single contour color. -->                           |
|                                                           |
| <CompareMesh ENABLE = "TRUE"                              |
|                                                           |
|    iCompareMode = "1"                                     |
|                                                           |
|    fMaxDistance= "-1"                                     |
|                                                           |
|    bAddViewPoint ="TRUE"                                  |
|                                                           |
|    bSetPartMax="FALSE"                                    |
|                                                           |
|    />                                                     |
|                                                           |
| </VCollabBatch>                                           |
+-----------------------------------------------------------+

**Dynamic Arguments**

Arguments for merging CAX files can also be set dynamically in batch
mode. This feature is useful for repeated operations without having to
edit values in the input XML file.

The XML file is thus used as a template and its values are set
externally through command line arguments.

E.g.

C:\Program Files\VCollab\VCollabPro64> VCollabPro.exe -b
"C:\test\batch.xml" "..\Samples\BatchMode Inputs\airbag.cax"
"..\Samples\BatchMode Inputs\audi.cax" "C:\output.cax"

In this example, the input CAX file, output file and input merge CAX
file have been provided dynamically.

The arguments are denoted as @arg#\ **N** where N is the index of the
argument in the command line. Dynamic arguments can be used in any field
and in any order, but @arg#\ **N** has to match with the command line
input index.

   In this example,

   @arg#0 = VCollabPro.exe

   @arg#1= -b

   @arg#2 = C:/test/batch.xml

   @arg#3= ..\Samples\BatchMode Inputs\airbag.cax which is assigned to
   sInputFile

   @arg#4=..\Samples\BatchMode Inputs\audi.cax which is assigned to
   sOutputFile

   @arg#5=C:\output.cax which is assigned to sInputMergeCaxFile

**Modified xml**

   Fields that take values from command line arguments are highlighted.

+----------------------------------------------------------------------+
| <?xml version="1.0" encoding="utf-8" ?>                              |
|                                                                      |
| <!-- Purpose : This sample explains how to merge two cax files, to   |
| compare both models and generate new cax with new compare result-->  |
|                                                                      |
| <!-- Here the fields, 'sInputFile' and 'sInputMergeCaxFile' are      |
| input cax files and 'sOutputFile' is the merged file -->             |
|                                                                      |
| <VCollabBatch fVersion = "0.1"                                       |
|                                                                      |
|    sInputFile = **"@arg#3"** >                                       |
|                                                                      |
|    <Output sOutputFile =\ **"@arg#5"** />                            |
|                                                                      |
| <!-- Merged file can be repositioned from its original coordinate    |
| system using ENABLE_TRANSLATION, ENABLE_ROTATION or ENABLE_SCALE --> |
|                                                                      |
| <!-- Note : Set either 'bCombinedPalette' or 'bMultiPalette' as TRUE |
| at once, only if needed -->                                          |
|                                                                      |
| <!-- Note iMergePosition value is 0-AsIs; 1-left; 2-right; 3-top;    |
| 4-bottom; 5-Relative translate; 6-Absolute posistion; Default is     |
| 0-->                                                                 |
|                                                                      |
| <!-- Translation Rotation Scale will work only when                  |
| iMergePosition="5" or "6" other wise they are ignored.-->            |
|                                                                      |
| <!-- New viewpath will be added as 'MergeAsNewDataset' with a        |
| viewpoint named 'Merge' in which all the CAE states will be          |
| retained.\` -->                                                      |
|                                                                      |
|                                                                      |
| <MergeAsNewDataSet ENABLE = "TRUE"                                   |
|                                                                      |
|    sInputMergeCaxFile = **"@arg#4"**                                 |
|                                                                      |
|    bCombinedPalette = "FALSE"                                        |
|                                                                      |
|    bMultiPalette = "FALSE"                                           |
|                                                                      |
|    bShowDataSetLabels= "TRUE"                                        |
|                                                                      |
|    bApplyCurentSettings ="FALSE"                                     |
|                                                                      |
|    iMergePosition="2"                                                |
|                                                                      |
|    ENABLE_TRANSLATION = "FALSE"                                      |
|                                                                      |
|    fTranslationX = "3"                                               |
|                                                                      |
|    fTranslationY = "0"                                               |
|                                                                      |
|    fTranslationZ = "0"                                               |
|                                                                      |
|    ENABLE_ROTATION = "FALSE"                                         |
|                                                                      |
|    fRotationX = "0"                                                  |
|                                                                      |
|    fRotationY = "1"                                                  |
|                                                                      |
|    fRotationZ = "0"                                                  |
|                                                                      |
|    fRotationAngle = "0"                                              |
|                                                                      |
|    ENABLE_SCALE = "FALSE"                                            |
|                                                                      |
|    fScaleX = "1"                                                     |
|                                                                      |
|    fScaleY = "1"                                                     |
|                                                                      |
|    fScaleZ = "1"                                                     |
|                                                                      |
|    />                                                                |
|                                                                      |
| <!--The following option is to compare mesh/geometry first model     |
| with second model and to generate a result with the deviation -->    |
|                                                                      |
| <!-- iCompare Mode varies from 0 to 2. 0 refers to same part         |
| comparision, 1 refers to visible parts comparison and 2 refers to    |
| all parts comparison -->                                             |
|                                                                      |
| <!-- iMaxDistance refers to maximum deviation considered for         |
| comparison -->                                                       |
|                                                                      |
| <!-- bAddViewPoint (TRUE) adds current scene with deviation result   |
| color plot into viewpoint and save it to cax -->                     |
|                                                                      |
| <!-- bSetPartMax (TRUE) applies part maximum deviation value to the  |
| color plot of the part. i.e. Each part will be of single contour     |
| color. -->                                                           |
|                                                                      |
| <CompareMesh ENABLE = "TRUE"                                         |
|                                                                      |
|    iCompareMode = "1"                                                |
|                                                                      |
|    fMaxDistance= "-1"                                                |
|                                                                      |
|    bAddViewPoint ="TRUE"                                             |
|                                                                      |
|    bSetPartMax="FALSE"                                               |
|                                                                      |
|    />                                                                |
|                                                                      |
| </VCollabBatch>                                                      |
+----------------------------------------------------------------------+
