Image Generator
===============

VCollabImageGenerator.exe is a batch mode application to generate image from cax file. This application is available at **VCollab_Installation_Directory\\VCollabPro64.**


**Usage #1 Single Image Generation**

 *Syntax :*

  *C/>:"VCollabImageGenerator.exe" [input] [output] [Image Dimension] [Model View] [Background Color] [Legend State] [Result Name] [Instance Name] [Derived Result Name]*

    Where,

    +-----------------------------------+-----------------------------------+
    | [input]                           | input cax file path.              |
    +-----------------------------------+-----------------------------------+
    | [output]                          | output image file path.           |
    +-----------------------------------+-----------------------------------+
    | [Image Dimension]                 | width and height of image. A      |
    |                                   | space is required between width   |
    |                                   | and height values.                |
    +-----------------------------------+-----------------------------------+
    | [Model View]                      | any one of the following views    |
    |                                   |                                   |
    |                                   | { "Front",                        |
    |                                   | "Rear","Top","Bottom",            |
    |                                   | "Left","Right", "Iso",            |
    |                                   |                                   |
    |                                   | "FrontMesh", "RearMesh",          |
    |                                   | "TopMesh", "BottomMesh",          |
    |                                   | "LeftMesh", "RightMesh",          |
    |                                   | "IsoMesh",                        |
    |                                   |                                   |
    |                                   | "FrontWire", "RearWire",          |
    |                                   | "TopWire", "BottomWire",          |
    |                                   | "LeftWire", "RightWire",          |
    |                                   | "IsoWire",                        |
    |                                   |                                   |
    |                                   | "FrontHiddenLine",                |
    |                                   | "RearHiddenLine",                 |
    |                                   | "TopHiddenLine",                  |
    |                                   | "BottomHiddenLine",               |
    |                                   | "LeftHiddenLine",                 |
    |                                   | "RightHiddenLine",                |
    |                                   | "IsoHiddenLine" }                 |
    +-----------------------------------+-----------------------------------+
    | [Background Color]                | Three values with space between   |
    |                                   | them. Each value should be in the |
    |                                   | interval [0,1].                   |
    +-----------------------------------+-----------------------------------+
    | [Legend State]                    | "LegendON" or "LegendOFF".        |
    +-----------------------------------+-----------------------------------+
    | [Result Name]                     | CAE result name. e.g.,            |
    |                                   | "Displacement".                   |
    +-----------------------------------+-----------------------------------+
    | [Instance Name]                   | CAE result instance name. e.g.,   |
    |                                   | "L1M3".                           |
    +-----------------------------------+-----------------------------------+
    | [Derived Result Name]             | CAE result derived name. e.g.,    |
    |                                   | "Translational Magnitude".        |
    +-----------------------------------+-----------------------------------+

 
| Example:

    "C:\\...\\bin>VCollabImageGenerator.exe "F:\\bracket_multiple.cax"
    "C:\\bracket_displacement.jpg" 600 400 "Iso" 1 1 1 "LegendON"
    "Displacement" "L1M1" "Translational Magnitude"

    

    where,

        | param[0] = "VCollabImageGenerator.exe" : application
        | param[1] = "F:\\bracket_multiple.cax" : input data File
        | param[2] = "C:\\bracket_displacement.jpg" : output jpg image
          File; bmp, jpg, tif, png, wcax, pdf(3D) and Jt, are supported
          formats
        | The following are OPTIONAL parameters, but has to be in the
          same order
        | param[3] = 600 : width of the image; Default is 600
        | param[4] = 400 : height of the image; Default is 500\n");
        | param[5] = "Front" :to set Frontview and Shaded display mode;
          "FrontWire" :to set Frontview and Wireframe display mode;
          Default is "Iso"
        | param[6] = 1 : Back ground color red field [range 0-1];
          Default is 0
        | param[7] = 0.5 : Back ground color green field [ range 0-1];
          Default is 0
        | param[8] = 0.2 : Back ground color blue field [range 0-1];
          Default is 0
        | param[9] = LegendOFF : Legend display is 'Off'; Defalut is
          "LegendON"
        | param[10] = "ResultName" : Result Name; Default is First
          result in the cax
        | param[11] = "Instance" : Instance Name; Default is First
          instance in the result
        | param[12] = "Derived Result Name" : Derived Result Name;
          Default is "Translational Magnitude" for vector type and "Von
          Mises Stress" for tensor type

     
  | Note:

    -  Set param[6]=-1, param[7]=-1, param[8]=-1 to ignore the
       background color.

    -  To set other standard views, use param[5] as "Front" for front
       view "Rear" for rear view...

    -  Note: To use software renderer, Insert param[1] as "-swrend"

        e.g.: C:\...\bin>VCollabImageGenerator.exe "-swrend"
        "F:\bracket_multiple.cax"

    Note: If you get blank images(depends on graphics cards), Insert
    param[1] as "-w",

        e.g C:\...\bin>VCollabImageGenerator.exe "-w"
        "F:\\bracket_multiple.cax" ...this will generates right image,but
        displays window.

    Note: To mix window & software renderer option, Insert param[1] as
    "-wswrend",

        e.g C:\...\bin>VCollabImageGenerator.exe "-wswrend"
        "F:\\bracket_multiple.cax" ...


**Usage#2 Multi Image Generation**

 *Syntax:*

  *C/>"VCollabImageGenerator.exe" -v [input] [output] [Image Format] [Image Dimension] [CreateDir] [View Path] [vpt File Path]*

    Where,
	
    +-----------------------------------+-----------------------------------+
    | [input]                           | input cax file path.              |
    +-----------------------------------+-----------------------------------+
    | [output]                          | output image Dir path.            |
    +-----------------------------------+-----------------------------------+
    | [Image Format]                    | "jpg" or "bmp" or "png" or "tif". |
    +-----------------------------------+-----------------------------------+
    | [Image Dimension]                 | width and height of image. A      |
    |                                   | space is required between width   |
    |                                   | and height values.                |
    +-----------------------------------+-----------------------------------+
    | [CreateDir]                       | createDir=0 or createDir=1.       |
    |                                   | 'CreateDir'=1 creates directories |
    |                                   | inside 'OutputDir' for each       |
    |                                   | 'viewpath' in 'vpt' file.         |
    |                                   | 'CreateDir'=0 makes all image     |
    |                                   | files written in 'OutputDir'      |
    +-----------------------------------+-----------------------------------+
    | [View Path]                       | **viewPath ="viewPathName".       |
    |                                   | Images will be generated for all  |
    |                                   | viewpoints of this path. If path  |
    |                                   | is empty, then images for all     |
    |                                   | available viewpaths inside the    |
    |                                   | vpt file.**                       |
    |                                   | or                                |
    |                                   |                                   |
    |                                   | To Generate images for CAE        |
    |                                   | results set,                      |
    |                                   |                                   |
    |                                   | ViewPath=="@CAE" or               |
    |                                   | "@CAE@AllInstance" or             |
    |                                   | "@CAE@AllDerived" or              |
    |                                   | "@CAE@AllInstance@AllDerived" or  |
    |                                   | "@CAE@AllDerived@AllInstance"inp  |
    |                                   | uts.                              |
    |                                   |                                   |
    |                                   | This will help to generate        |
    |                                   | multiple images of all CAE        |
    |                                   | results.                          |
    |                                   |                                   |
    |                                   | @CAE : To generate images for all |
    |                                   | CAE results, with default         |
    |                                   | instance (first) and default      |
    |                                   | derived type.                     |
    |                                   |                                   |
    |                                   | @CAE@AllInstance : To generate    |
    |                                   | images for all CAE results and    |
    |                                   | all Instances, with default       |
    |                                   | derived type.                     |
    |                                   |                                   |
    |                                   | @CAE@AllDerived : To generate     |
    |                                   | images for all CAE results and    |
    |                                   | all derived types, with default   |
    |                                   | instance.                         |
    |                                   |                                   |
    |                                   | "@CAE@AllInstance@AllDerived" or  |
    |                                   | "@CAE@AllDerived@AllInstance" :   |
    |                                   | To generate images for all CAE    |
    |                                   | result's All instances with all   |
    |                                   | derived types.                    |
    |                                   |                                   |
    |                                   |                                   |
    +-----------------------------------+-----------------------------------+
    | [vpt File Path]                   | **vpt file path.                  |
    |                                   | vptFile="vptFilePath".**          |
    |                                   | Note: If viewpath is one of @CAE  |
    |                                   | type then vptfilePath can be      |
    |                                   | ignored or can be used to set std |
    |                                   | views by passing one of the       |
    |                                   | following                         |
    |                                   | "Front/Rear/Top/Bottom/Left/Right |
    |                                   | /Iso"                             |
    |                                   |                                   |
    +-----------------------------------+-----------------------------------+

    E.g.

        C:\...\bin>VCollabImageGenerator.exe -v
        "F:\\bracket_multiple.cax" "H:\\OutputDirPath" "png" 600 500 1
        "(blank)" "C:\\bracket.vpt"

        

        Where,

            | Inputcaxfile="F:\\bracket_multiple.cax"
              outputdir="h:\\OutputDirPath" ImageFormat="png" width=600
              height=500 createDir=1 viewPath="
              vptFile="C:\\bracket.vpt"
            | 

            Note:

            #. 'OutputDir' must exist.

            #. 'CreateDir'=1 creates directories inside 'OutputDir' for
               each 'viewpath' in 'vpt' file.

            #. 'CreateDir'=0 makes all image files written in
               'OutputDir'

            #. | 'ViewPath' is data inside .vpt file. Set this field with proper value to generate images for that particular viewpath.
               | To generate all viewpath images, Set this value as " ". (a space that inside 2 double quotes). But the field should not be ignored.
          

Note:

    To have more options, VCollab Profile can be used in image generator.

    To use VCollab profile use -vp field insted of -v.

    C:\...\bin>VCollabImageGenerator.exe **-vp** "F:\\bracket_multiple.cax" "H:\\OutputDirPath" "png" 600 500 1 "@CAE" "Iso"

    

    For Example to Switch OFF Legend and change background color,

    

    1.Launch VCollab Pro Application.

    2.Set Legend OFF and change background color

    3.Enable Profile and Save Profile.

    

    All these profile settings will be reflected in generated images.

    

            

**Error Codes**

 Image generator returns one of the following error codes.

 +----------------+---------------------------------------+
 | **Error Code** | **Description**                       |
 +----------------+---------------------------------------+
 |   0            | Image is generated successfully.      |
 +----------------+---------------------------------------+
 |   1            | Unexpected error.                     |
 +----------------+---------------------------------------+
 |   2            | Write permission is not available     |
 |                | for output file.                      |
 +----------------+---------------------------------------+
 |   5            | VCollab license is not available.     |
 +----------------+---------------------------------------+
 |   6            | Out of memory.                        |
 +----------------+---------------------------------------+
 |   7            | Invalid input file extension          |
 +----------------+---------------------------------------+
 |   8            | Invalid output file extension         |
 +----------------+---------------------------------------+
 |   9            | Invalid input file path               |
 +----------------+---------------------------------------+
 |   10           | Invalid arguments                     |
 +----------------+---------------------------------------+
 |   11           | Image is not generated.               |
 +----------------+---------------------------------------+
 |   12           | Specified result is not found.        |
 +----------------+---------------------------------------+

