Merge cax files
===============

This option helps user to merge two cax files into a single cax file.
Input file is an xml file which consists of all the information to
merge.

There are two xml files, one is basic format and the other is advanced.

**Syntax:**

    **Prompt :\\VCollabPro.exe file folder> *VCollabPro.exe* -b
    <*input xml file path*>**

**Example:**

    C:\Program Files\VCollab\VCollabPro32> VCollabPro.exe -b
    "C:\test\batch.xml"

**Sample Batch File**

    File Name: VCollabProBatch_MergeCAX.xml

    Location: "..\Samples\BatchMode Inputs\"

..

        | <?xml version="1.0" encoding="utf-8" ?>
        | <!-- BatchVersion 1.0 -->
        | <!-- VCollab Pro : Allows batch mode execution using -b option
          from command line. -->
        | <!-- Sample Usage : C:\VCollabAppPath>VCollabPro.exe -b
          this.xml -->
        | <!-- Copyright (C) 2010 Visual Collaboration Technologies Inc.
          -->
        | <!-- This xml format is alpha and it can be improved or
          changed by VCollab at the time of release VCollab Pro -->
        | <!-- Purpose : This sample explains, How to merge another cax
          file and generate new cax -->
        | <!-- Here, 'sInputFile' and 'sInputMergeCaxFile' are input cax
          files and 'sOutputFile' is the merged file -->
        | <VCollabBatch fVersion = "0.1"

            | sInputFile = "..\Samples\BatchMode Inputs\airbag.cax" >
            | <Output sOutputFile ="C:\output.cax" />
            | <!-- Note : Set either 'bCombinedPalette' or
              'bMultiPalette' as TRUE at once, only if needed -->

            | <!-- Note iMergePosition value is 0-AsIs; 1-left; 2-right;
              3-top; 4-bottom; 5-Relative translate; 6-Absolute
              posistion; Default is 0-->
            | <MergeAsNewDataSet ENABLE = "TRUE"

                | sInputMergeCaxFile = "..\Samples\BatchMode
                  Inputs\audi.cax"
                | bCombinedPalette = "FALSE"
                | bMultiPalette = "FALSE"

                bShowDataSetLabels = "TRUE"

                bApplyCurentSettings ="FALSE"

                | iMergePosition ="1"
                | ENABLE_TRANSLATION = "FALSE"
                | fTranslationX = "3"
                | fTranslationY = "0"
                | fTranslationZ = "0"
                | ENABLE_ROTATION = "FALSE"
                | fRotationX = "0"
                | fRotationY = "1"
                | fRotationZ = "0"
                | fRotationAngle = "0"
                | ENABLE_SCALE = "FALSE"
                | fScaleX = "1"
                | fScaleY = "1"
                | fScaleZ = "1"

            />

            **<!-- Merged file can be repositioned from its original
            coordinate system using ENABLE_TRANSLATION, ENABLE_ROTATION
            or ENABLE_SCALE -->**

            **<!-- Note: Translation, Rotation and Scale will work only
            when iMergePosition="5" or "6" other wise they are
            ignored.-->**

        </VCollabBatch>





**Dynamic Arguments**

    This section explains how to set values for xml fields through
    command line argument.

    Means, To do a fixed set of repeated operation, it is not needed to
    edit values in xml file .

    This XML files can be used as template and its values will be set
    from external command line arguments.

    E.g.

    **C:\Program Files\VCollab\VCollabPro32> VCollabPro.exe -b
    "C:\test\batch.xml" "..\Samples\BatchMode Inputs\airbag.cax"
    "..\Samples\BatchMode Inputs\audi.cax" "C:\output.cax**"

    This example sets value of xml fields in command arguments.

    To input command line arguments, xml fields need to to set as,

    | sInputFile = "@arg#3"
    | sOutputFile ="@arg#5" 
    | sInputMergeCaxFile = "@arg#4"

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

    Fields that takes values from command line arguments are
    highlighted.

    +-----------------------------------------------------------------------+
    |     | <?xml version="1.0" encoding="utf-8" ?>                         |
    |     | <!-- BatchVersion 1.0 -->                                       |
    |       <!-- VCollab Pro : Allows batch mode execution using -b option  |
    |       from command line. -->                                          |
    |       <!-- Sample Usage : C:\VCollabAppPath>VCollabPro.exe -b         |
    |       this.xml -->                                                    |
    |       <!-- Copyright (C) 2010 Visual Collaboration Technologies Inc.  |
    |       -->                                                             |
    |       <!-- This xml format is alpha and it can be improved or changed |
    |       by VCollab at the time of release VCollab Pro -->               |
    |       <!-- Purpose : This sample explains, How to merge another cax   |
    |       file and generate new cax -->                                   |
    |       <!-- Here, 'sInputFile' and 'sInputMergeCaxFile' are input cax  |
    |       files and 'sOutputFile' is the merged file -->                  |
    |                                                                       |
    |     | <VCollabBatch fVersion = "0.1"                                  |
    |                                                                       |
    |         | sInputFile = "**@arg#3**" >                                 |
    |         | <Output sOutputFile ="**@arg#5**" />                        |
    |         | <!-- Note : Set either 'bCombinedPalette' or                |
    |           'bMultiPalette' as TRUE at once, only if needed -->         |
    |                                                                       |
    |         | <!-- Note iMergePosition value is 0-AsIs; 1-left; 2-right;  |
    |           3-top; 4-bottom; 5-Relative translate; 6-Absolute position; |
    |           Default is 0-->                                             |
    |         | <MergeAsNewDataSet ENABLE = "TRUE"                          |
    |                                                                       |
    |             | sInputMergeCaxFile = "**@arg#4**"                       |
    |             | bCombinedPalette = "FALSE"                              |
    |             | bMultiPalette = "FALSE"                                 |
    |                                                                       |
    |             bShowDataSetLabels = "TRUE"                               |
    |                                                                       |
    |             bApplyCurentSettings ="FALSE"                             |
    |                                                                       |
    |             | iMergePosition = "1"                                    |
    |             | ENABLE_TRANSLATION = "FALSE"                            |
    |             | fTranslationX = "3"                                     |
    |             | fTranslationY = "0"                                     |
    |             | fTranslationZ = "0"                                     |
    |             | ENABLE_ROTATION = "FALSE"                               |
    |             | fRotationX = "0"                                        |
    |             | fRotationY = "1"                                        |
    |             | fRotationZ = "0"                                        |
    |             | fRotationAngle = "0"                                    |
    |             | ENABLE_SCALE = "FALSE"                                  |
    |             | fScaleX = "1"                                           |
    |             | fScaleY = "1"                                           |
    |             | fScaleZ = "1"                                           |
    |                                                                       |
    |         />                                                            |
    |                                                                       |
    |         **<!-- Merged file can be repositioned from its original      |
    |         coordinate system using ENABLE_TRANSLATION, ENABLE_ROTATION   |
    |         or ENABLE_SCALE -->**                                         |
    |                                                                       |
    |         **<!--NOTE: Translation, Rotation & Scale will work only when |
    |         iMergePosition="5" or "6" other wise they are ignored.-->**   |
    |                                                                       |
    |     </VCollabBatch>                                                   |
    |                                                                       |
    |                                                                       |
    +-----------------------------------------------------------------------+

    Note: Dynamic arguments can be used in any field and in any order,
    but @arg#\ *Number* has to match with command line input index.

