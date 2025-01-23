Image Generation using viewpoint 
================================

This option helps user to generate image for viewpoints of a cax file. Input file is an xml file which consists of all the information to generate viewpoint as image. Below is given the syntax and a       
sample xml batch file.
                                         
**Syntax:**
                                                                      
 Prompt :\VCollabPro.exe file folder> *VCollabPro.exe* -b <*input xml file path*>
                                                                      
 Example:                                                              
 
 C:\Program Files\VCollab\VCollabPro32> VCollabPro.exe -b "C:\test\batch.xml"
                                                                      

**Sample Batch File**     

 File Name: VCollabProBatch_ImageGen_ViewPtSel.xml                 
 Location: "..\Samples\BatchMode Inputs\"                          

 ::

     <?xml version="1.0" encoding="utf-8" ?>
     <!-- BatchVersion 1.0 -->
     <!-- VCollab Pro : Allows batch mode execution using -b option 
          from command line. --> 
     <!-- Sample Usage : C:\VCollabAppPath>VCollabPro.exe -b this.xml -->
     <!-- Copyright (C) 2010 Visual Collaboration Technologies Inc. -->
     <!-- This xml format is alpha and it can be improved or changed by 
          VCollab at the time of release VCollab Pro -->
     <!-- Purpose : This sample explains, How to generate an image file for 
          a specific view point -->
     <VCollabBatch
             fVersion= "0.1"
             sInputFile= "..\\Samples\\cax\\airbag_viewpoints.cax" />
     <!-- iImageWidth, iImageHeight : are width and height
          of the image file in pixels. Minimum is 200x200.
          Maximum is size of screen resuolution. -->
     <!-- sOutPutImageFile : Output image file path. Only jpg, bmp, png 
          and tiff are supported -->

     <ImageGenerator ENABLE ="TRUE"
          iImageWidth = "600"
          iImageHeight = "400"
          sOutPutImageFile = "C:\\output.jpg" />
     <!-- sViewPointName : is the view point that has to be exported as 
          image -->

     <!-- sViewPathName : is the viewpath where the above viewpoint belongs 
          in the list -->
     <SelectViewPoint ENABLE = "TRUE"
          sViewPointName = "Explode View"
          sViewPathName = "Path01" />

     <!-- These all are optional blocks, Use only when 
          required Or Set ENABLE as "FALSE" if that block need to
          be skipped -->
     <!-- 'sInputViewPointFile is the external file that has
          viewpoints to be imported. It can be cax or .vpt*file -->
     <!-- To Skip viewpoint state Set bApplyViewPointState = 
          "FALSE" -->

     <ImportViewpoint ENABLE = "FALSE"
          sInputViewPointFile = "\\ ..\\Samples\\cax\\airbag_viewpoints.vpt"
          bApplyViewPointState = "TRUE" />
     </VCollabBatch>
                
**Dynamic Arguments** 
                                                
 This section explains how to set values for xml fields through command line argument.
                                                                       
 Means, To do a fixed set of repeated operation, it is not needed to edit values in xml file .
                                                                       
 This XML files can be used as template and its values will be set from external command line arguments.

  E.g.                                                              
                                                                       
   C:\Program Files\VCollab\VCollabPro32> VCollabPro.exe -b      
      
     "C:\test\batch.xml" "..\Samples\cax\airbag.cax"                   
     "..\Samples\cax\airbag_viewpoints.vpt" "C:\output.jpg"         
     "Path01" "Explode View"                                           
                                                                       
   This examples sets values of xml fields in command arguments.    
                                                                       
   To input the command line arguments, xml fields need to to set as,
                                                                       
    | sInputFile = "@arg#3"                                           
    | sInputViewPointFile ="@arg#4"                                    
    | sOutPutImageFile = "@arg#5"                                     
    | sViewPathName = "@arg#6"                                         
    | sViewPointName = "@arg#7"                                        
                                                                       
    Here, @arg# is required prefix followed by a number.             
                                                                      
    The number is the index of command line argument list.            
                                                                      
    In this example,                                                  
                                                                      
     @arg#0 =VCollabPro.exe                                           
                                                                       
     @arg#1 = -b                                                       
                                                                       
     @arg#2 = C:/test/batch.xml                                        
                                                                       
     @arg#3 = ..\Samples\BatchMode Inputs\airbag.cax                   
                                                                       
     @arg#4 = ..\Samples\cax\airbag_viewpoints.vpt                     
                                                                       
     @arg#5 = C:\output.jpg                                            
                                                                       
     @arg#6 = Path01                                                   
                                                                       
     @arg#7 = Explode View                                             
                                                                       

																	   
**Modified xml**
                                                                       
 Fields that takes values from command line arguments are highlighted.
 
 ::
 
  <?xml version="1.0" encoding="utf-8" ?>
  <!-- BatchVersion 1.0 -->
  <!-- VCollab Pro : Allows batch mode execution using -b
       option from command line. -->
  <!-- Sample Usage : C:\VCollabAppPath>VCollabPro.exe -b
       this.xml -->
  <!-- Copyright (C) 2010 Visual Collaboration Technologies
       Inc. -->
  <!-- This xml format is alpha and it can be improved or 
       changed by VCollab at the time of release VCollab Pro -->
  <!-- Purpose : This sample explains, How to generate an
       image file for a specific view point -->
  <VCollabBatch
       fVersion = "0.1"
       sInputFile = **@arg#3**  />
  <!-- iImageWidth, iImageHeight : are width and height
       of the image file in pixels. Minimum is 200x200.
       Maximum is size of screen resuolution. -->
  <!-- sOutPutImageFile : Output image file path. Only
       jpg, bmp, png and tiff are supported -->
  <ImageGenerator ENABLE ="TRUE"
       iImageWidth = "600"
       iImageHeight = "400"
       sOutPutImageFile = **@arg#5** />
  <!-- sViewPointName : is the view point that has to be
       exported as image -->
  <!-- sViewPathName : is the viewpath where the above
       viewpoint belongs in the list -->
  <SelectViewPoint ENABLE = "TRUE"
       sViewPointName = **@arg#7**
       sViewPathName = **@arg#6** />
  <!-- These all are optional blocks, Use only when
       required Or Set ENABLE as "FALSE" if that block need to
       be skipped -->
  <!-- 'sInputViewPointFile is the external file that has
       viewpoints to be imported. It can be cax or .vpt*file -->
  <!-- To Skip viewpoint state Set bApplyViewPointState =
       "FALSE" -->
  <ImportViewpoint ENABLE = "FALSE"
       sInputViewPointFile = **@arg#4**
       bApplyViewPointState = "TRUE" />
  </VCollabBatch>


Note: Dynamic arguments can be used in any field and in any order, but @arg#\ *Number* has to match with command line input index.
