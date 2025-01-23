**************************
List of Commands
**************************


General Commands
=================

SAVE
*****

This command saves the 3D Report into various formats as listed.

.. code-block::

   SAVE, <HTML/WCAX/CAX/PDF>, Output File Name <String>

- Output file name is optional. By default, it will take same name as native file name.


.. admonition:: Examples

    ::

        SAVE,CAX
        SAVE,HTML

    - Saves the CAX report with the same name as native file name.
    - Saves the HTML file with the same name as CAX file name.


CUR_FOLDER
***********

This command sets default Folder Path for files.

.. code-block::

    CUR_FOLDER,<CAX/PY/TEMP> or <Path>

- CAX : CAX file path is set as current folder.
- PY : Script file path.
- TEMP : VCollab Temp path or or log file path.
- <Path> : full path.
    
LOADCAX
********

This command opens the CAX file from the specified. 

.. code-block::

    LOADCAX, <CAXFilePath>


MERGECAX
*********

This command merges the CAX file into the current used CAX file.

.. code-block::

    MERGECAX, <Merge_CAXFilePath>


SET_VAR
********

Define list of variables.

.. code-block::

    SET_VAR,<variable_name>=<variable Value>


.. admonition:: Examples

    ::

        SET_VAR,A=L3M1
        SET_VAR,VMStress_Limit=390

    - Defines a variable 'A' which is assigned a VCollab Instance L3M1.
    - Defines a variable 'VMStress_Limit' which is assigned a value of 390.


SHOWCMDS
*********

Popup Display commands (for debugging).

.. code-block::

    SHOWCMDS, <Y/N>


SET_MODEL
**********

This sets model as current.

.. code-block::

    SET_MODEL, <model Name> 


AXIS_POS
*********

This sets the postion of axis on the screen based on X and Y position.

.. code-block::

    AXIS_POS, <X position>, <Y position> 

- <X position> and <Y position> can be floating values.
- <X position> increases from left to right on the screen.
- <Y position> increases from top to bottom on the screen.

.. image:: media/Axis_Position.PNG


Set Camera Commands
===================

CAMERA_VIEW
************

This command sets camera Z direction vector <dx,dy,dz> and Up-vector <ux,uy,uz>.

.. code-block::

    CAMERA_VIEW, dx, dy, dz, ux, uy, uz

- This command specifies camera orientation of a model in VCollab Pro GUI.

.. admonition:: Example

    ::

        CAMERA_VIEW,-0.63,0.36,-0.69,-0.57,0.4,0.72 

    .. image:: media/Camera_Settings.PNG


CAMERA_XYAXIS
**************

This command sets Camera axis X-dir and Y Dir(Upvector).

.. code-block::

    CAMERA_XYAXIS, dx, dy, dz, ux, uy, uz


.. admonition:: Example

    ::

        CAMERA_XYAXIS,1,0,0,0,1,0


FIT_VIEW
*********

This command zooms the model view in VCollab Pro GUI. 

.. code-block::

    FIT_VIEW, <zoom factor>

- <zoom factor> is optional.
- The zoom factor varies from -0.5 to +0.5, default is 1.0.

.. admonition:: Example

    ::

        FIT_VIEW 
        FIT_VIEW,-0.3 


    - It fits the model view in VCollab Pro GUI.
    - It fits the model view in VCollab Pro GUI with a zoom factor of -0.3.


ORTHO_VIEW
***********

This command sets Ortho/Perspective Projection.

.. code-block::

    ORTHO_VIEW, <Y/N>


.. |img_ortho| image:: media/Ortho.PNG
    :width: 300

.. |img_pers| image:: media/Perspective.PNG
    :width: 300

+-------------+-------------------------+
| Ortho View  |    Perspective View     |
+-------------+-------------------------+
| |img_ortho| |      |img_pers|         |
+-------------+-------------------------+


ViewPoint Commands
==================

VIEWPATH
*********

This generates a ViewPath with user defined name.

.. code-block::

    VIEWPATH, <ViewPath Name>

.. image:: media/Viewpath.PNG

.. admonition:: Example

    ::

        VIEWPATH,Sample

    This will create a ViewPath by name "Sample".


IMAGE_VP
*********

This creates the background and/or other images to be imported into VCollab.

.. code-block::

    IMAGE_VP, <VPName>, <image file name>, <Title String>, <Title Position(Sx,Sy)>

- [1] VPName : ViewPoint name, optional. If VPName=N, then image is set as background. ViewPoint is not created. 
- [2] Image File Name : user should provide image file name.
- [3] Title String : ViewPoint title name, optional. 
- [4,5] Title Position(Sx,Sy) : ViewPoint title X and Y position.

.. admonition:: Example

    ::

        IMAGE_VP,N,Sample.png 
        IMAGE_VP,Stress,Sample.png,VM Stress,0.2,0.1 

    - Background is created using Sample.png file.
    - ViewPoint named "Stress"is created with background image as Sample.png. Title "VM Stress" is also created in ViewPoint at the desired location.


ADD_VP
*******

This creates a ViewPoint with user defined VPName. 

.. code-block::

    ADD_VP, <vpname>, [<Title>, <title position xy>]

- [<Title>, <title position xy>] is optional. It creates title in the VP and places at desired position.

.. admonition:: Example

    ::

        ADD_VP,VM_Stress 
        ADD_VP,VM_Stress,Stress,0.2,0.1

    - It adds a ViewPoint by the name VMStress.
    - It adds a ViewPoint by the name VMStress. Title "Stress" is added to the ViewPoint at desired position.

ADD_VP_ANIM
************

This creates a ViewPoint with animation.

.. code-block::

    ADD_VP_ANIM, <vpname>, [<Title>, <title position xy>]

- [<Title>, <title position xy>] is optional. It creates title in the ViewPoint and places at desired position.

.. admonition:: Example

    ::

        ADD_VP_ANIM,VM_Stress 
        ADD_VP_ANIM,VM_Stress,Stress,0.2,0.1

    - It adds a ViewPoint with animation by the name VMStress.
    - It adds a ViewPoint with animation by the name VMStress. Title "Stress" to the ViewPoint at desired position.


Set Display Commands
====================

SET_FONT
*********

This sets the front for the entity type as listed.

.. code-block::

    SET_FONT, <Type>, <Size>, <Name>, <iR,iG,iB> , <ibR,ibG,ibB>, <iborder>

- [1] <Type> : Entity type ,<NOTE, PROBE_VALUE, PROBE_TEXT, OTHERS>
- [2] <Size> : font size 
- [3] <Name> : font name
- [4] <iR, iG, iB> : font color RGB
- [5] <ibR,ibG,ibB> : font background color
- [6] <iborder> : Border on/off (0=Off else ON)

.. image:: media/Add_Notes.PNG

.. admonition:: Example

    ::

        SET_FONT,NOTE,18,Arial Bold,92,92,92,255,255,240,0
        SET_Font,NOTE,26,Arial Bold,36,62,141

    - This will set the note settings accordingly to the parameters with no border.
    - This will set the note settings with default label background with border.


.. note::
    Values of <iR, iG, iB> and <ibR, ibG, ibB> are available in Add Notes.
    User can click on the color and decide on the values accordingly.


SET_DISPLAY
***********

This sets the display mode settings in the VCollab Pro GUI.

.. code-block::

    SET_DISPLAY, COLOR=Y, LEGEND=Y, DEFORM=Y, UDMESH=1, DMODE=1, AXIS=Y, SECTION=N, BG=1

- [1] Color: Optional, Sets CAE color plot. Y to apply color plot.
- [2] Legend: Optional, Show Legend. Y to show the legend.
- [3] Deform:  Optional, Show deformation. Y to show the deformation.
- [4] UDMesh: Optional, sets visibility for undeformed mesh (0-3).
- [5] DMode: Optional, sets display mode of the scene. Valid range is 0 to 5.

    - 0 - Shaded
    - 1 - Shaded Mesh
    - 2 - Wireframe
    - 3 - Hiddenline Removal
    - 4 - Point
    - 5 - Transparent

- [6] Axis: Optional, show Axis(Y/N). Y to show the axis.
- [7] Section: Optional, show section(Y/N). Y to show the section.
- [8] BG: Optional, Valid range 0 to 2.

    - 0 - Plain
    - 1 - Gradient
    - 2 - Texture


.. admonition:: Example

    ::

        SET_DISPLAY,COLOR=Y,LEGEND=Y,DEFORM=N,SECTION=N,AXIS=Y

    - Sets the display mode settings according to the mentioned parameters.

SHOW_LABEL
***********

This sets the probe label settings.

.. code-block::

    SHOW_LABEL, ID=True, ROW=True, COL=False, Rank=True, PART=False, HEADER=False, ABR=True, PROBE=0, DISP=Y/N, ARRANGE=0-5

- [1] ID: Show node/element id (Y/N). Y to show id (optional) 
- [2] ROW: Show row header (Y/N). Y to show row header (optional)
- [3] Rank: Show Rank (Y/N). Y to show Rank (optional)
- [4] PART: Show Part name (Y/N). Y to show Part name (optional)
- [5] HEADER: Show Header Legend(Y/N). Y to show Header Legend (optional)
- [6] ABR: Display Abbreviations legend. Y to show Abbreviation Legend (optional)
- [7] PROBE: Sets current probe type. The valid range is 1 to 5 (optional)

    - 1 - CurrentResult-Derived
    - 2 - CurrentResult-Full
    - 3 - All Results-Table
    - 4 - All Instances-Table
    - 5 - All Instances-XY Plot

- [7] DISP: Show labels (Y/N). Y to show labels
- [8] ARRANGE: Sets label arrangement mode. The valid range is 0 to 5 (optional)

    - 0 - Actual.
    - 1 - Top-Bottom.
    - 2 - Compact
    - 3 - Circular
    - 4 - Silhouette
    - 5 - Rectangular

.. admonition:: Example

    ::

        SHOW_LABEL,ID=N,Rank=Y,PROBE=1

    - Sets the probe label settings according to the mentioned parameters.

LABEL_PRECISION
****************

This sets the probe label precision.

.. code-block::

    LABEL_PRECISION,iPrecision,bScientific(Y/N)

- [1] iPrecision: sets number of digits required in precision
- [2] bScientific: set Y to show number in scientific notation

.. admonition:: Example

    ::

        LABEL_PRECISION,3,Y

    - Sets the probe label precision settings according to the mentioned parameters.

SET_MODEL_COLOR
****************

This sets random colors to each part in the model (No arguments).

.. code-block::

    SET_MODEL_COLOR


DEL_ENTITY
***********

This command specifies entity types to be deleted.

.. code-block::

    DEL_ENTITY, XY, LABEL, SYMBOL, PROBE

- This command is used in the beginning of every ViewPoint to clear the data from previous ViewPoint.


Legend Commands
=================

SET_LEGEND
***********

This sets legend settings.

.. code-block::

    SET_LEGEND,<UserMax> ,<UserMin> ,<MAXLimit> ,<MINLimit> ,<Precision>, <Discrete(Y/N)>, <Reverse(Y/N)>, NColor

- [1,2] UserMax, UserMin : Sets Custom Legend Range.Set NA to skip limit setting
- [3,4] MAXLimit, MINLimit : Legend limits. Set NA to skip limit setting
- [5] Precision : sets number of digits required in precision.
- [4] Discrete : set Y to display discrete legend.
- [5] Reverse : set Y to display reverse legend.
- [6] NColor : set number of colors in legend (optional).

.. image:: media/CAE_Settings.PNG


.. admonition:: Example

    ::

        SET_LEGEND,NA,NA,NA,NA,3,Y,N

    - This will set the legend settings accordingly.




LEGEND_HEXCOLORS
*****************

This sets the legend colors accoridng to the hexcolors.

.. code-block::

    LEGEND_HEXCOLORS, <list of hex colors>


.. admonition:: Example

    ::

        LEGEND_HEXCOLORS,FF0000,FFDD00,00FF00,00DDFF,0000FF


SET_LEGEND_DYNRANGE
********************

This sets the values of legend as provided.

.. code-block::

    SET_LEGEND_DYNRANGE, <list of legend values>


.. admonition:: Example

    ::

        SET_LEGEND_DYNRANGE,20,10,5,2,0


LEGENDFONT_SIZE
****************

This sets the legend font size.

.. code-block::

    LEGENDFONT_SIZE, <iSize>, <fontName>


LEGEND_POS
***********

This sets the legend position in the GUI screen.

.. code-block::

    LEGEND_POS, X_position, Y_position, bRelativeiOrientation (0-2/N)

- X_pos: increases from left to right. 
- Y_pos: increases from top to bottom
- bRelativeiOrientation (0-2/N): Optional

.. image:: media/Axis_Position.PNG

.. admonition:: Example

    ::

        LEGEND_POS,0.01,0.25



Part Commands
===============

PART_OPTIONS
*************

This command sets the Display Mode and also sets the contour plot mode or material color mode.

.. code-block::

    PART_OPTIONS,MODE=(0-5), Color(Y/N), <PartList>

- Display modes

    - 0 : Shaded.
    - 1 : Shaded Mesh.
    - 2 : WireFrame.
    - 3 : Hidden Line Removal.
    - 4 : Points.
    - 5 : Transparent.

- Color : Y for contor plot mode, N for material color mode.

.. admonition:: Example

    ::

        PART_OPTIONS,MODE=1, *Bracket*, *Lever*
        PART_OPTIONS,COLOR=Y,*Bracket*,*Lever*

    - This will show the all the parts with Bracket and Lever keywords and will switch on the shaded mode for them.
    - This will show the all the parts with Bracket and Lever keywords and will switch on contour plot mode for them.


PARTS_SHOW
***********

This shows the required Parts in the GUI.

.. code-block::

    PARTS_SHOW, <ALL/NONE/INVERT/ONLY/ADD>, <Part name list>

- ALL: show all parts.
- NONE: Hide all parts.
- INVERT: Invert part show.
- ONLY: Show Only these parts.
- ADD: Show these parts.

.. admonition:: Example

    ::

        PARTS_SHOW,ONLY,*Bracket*,*Lever*

    - This will show the only the parts with Bracket and Lever keywords.


PARTS_HIDE
***********

This hides the required Parts in the GUI. 

.. code-block::

    PARTS_HIDE, <ALL/INVERT/ONLY>, <Part name list>

- ALL: hide all parts.
- INVERT: Invert part hide.
- ONLY: Hide Only these parts.

.. admonition:: Example

    ::

        PARTS_HIDE,ONLY,*Bracket*,*Lever*

    - This will hide the only the parts with Bracket and Lever keywords.


ASM_SHOW
*********

This sets assembly show/noshow.

.. code-block::

    ASM_SHOW, <Y/N>, <Assembly Names>


FILTER_PARTS
*************

This command filters the parts based on results in the GUI screen.

.. code-block::

    FILTER_PARTS, fMin, fMax, <bFitView(Y/N)>

- [1] fMin: min result limit for filtering parts or NA can be provided.
- [2] fMax: max result limit for filtering parts or NA can be provided.
- Both fMin and fMax cannot be NA. Atleast one limit should be provided.
- [3] bFitView (Y/N): Optional, for a fit view of filtered parts.


Result Commands
=================

SEL_RESULT
***********

This selects the result to be displayed in GUI.

.. code-block::

    SEL_RESULT, <Result Name>, <Instance>, <Derived Type> 

- Result Name: Selects the name of the result to be displayed.
- Instance: Selects the instance of the result to be displayed.
- Derived Type: Selects the derived type of the result to be displayed.
- By default, Derived type is NA.

.. image:: media/CAE_Result.PNG

.. admonition:: Example

    ::

        SEL_RESULT,*Stress*max*prin*,L3M1,NA

    - This will select the Max Principal Stress result for L3M1 instance.


SEL_INSTANCE
*************

This selects the instance for current result.

.. code-block::

    SEL_INSTANCE, <InstFlag>

- InstFlag 0: Last Instance.
- InstFlag 1: Max Instance.
- InstFlag 2: Min Instance.
- InstFlag 3: First Instance else current Instance.


CREATE_RESULT
**************

This creates the new result from the exsisting result.

.. code-block::

    CREATE_RESULT ,<New Result Name>, <Result A>, <Result B>, <Equation with A and B>

- Result A name for the expression.
- Result B name for the expression.
- Arithmetic expression or formula with variables A and B.

.. admonition:: Example

    ::

        CREATE_RESULT,Name,A,B,IF((abs(A)>abs(B)),A,B)


    - This creates a max result from result A and B.


CREATE_ENVELOP
***************

This creates Max/Min envelope result.

.. code-block::

    CREATE_ENVELOP, <sResult>, <sDerived>, <bIsMax(Y/N)>

- [1] sResult: Required result for creating envelope.
- [2] sDerived: Derived type for the result or NA can be used.
- [3] bIsMax: Optional, Y for Max envelope(default) and N for Min envelope.    


CREATE_RESULT_CYL
******************

This creates a cylindrical co-ordinate result for the selected result.

.. code-block::

    CREATE_RESULT_CYL, RefResult, NewResult, <Origin(XYZ)>, <XDir(xYZ)>, <YDir(xyz)>, U/All

- [1]: VCollab Result name. 
- [2]: New result name.
- [3:5]: Origin of the new coordinate system.
- [6:8]: X axis vector.
- [9:11]: Y axis vector.
- [12]: Component name can be empty or any one of the following

    - For Vector Result: "U","V","W"
    - For Tensor Result: "S11","S22","S33","S12","S23","S13"


.. admonition:: Example

    ::

        Displacement,Disp Radial, 53.66, 73.05, 42.747, 1, 0, 0, 0, 1, 0, U

    - This creates a new cylindrical result 'Disp Radial' with origin at <53.66 73.05 42.747>.


SET_PALETTE_MODE
*****************

This defines the result palette mode when there are merged models.

.. code-block::

    SET_PALETTE_MODE, <0/1/2/3>

- [0]: Active Model.
- [1]: Multi Model.
- [2]: Combined Model.
- [3]: Multi_Common Model.


IMPORT_XYCSV
*************

.. code-block::

    IMPORT_XYCSV, <csvfile>

- This command imports the result from CSV File.


NEW_INSTANCE
*************

This command creates instance using expression.

.. code-block::

    NEW_INSTANCE, Result, InstA, InstB, Expression, sNewInst

- [1]: VCollab Result.
- [2]: Instance A name for the expression.
- [3]: Instance B name for the expression.
- [4]: Arithmetic expression or formula with variables A and B.
- [5]: New Instance Name.

.. admonition:: Example

    ::

        NEW_INSTANCE,Damage,L1M1,L2M1,Max(A,B),MaxDamage

    - This creates a new instance by the name MaxDamage from the Damage instance L1M1 and L2M1.


NodeSet Mask Commands
======================

RES_MASK
**********

This creates a NodeSet from the selected result for masking.

.. code-block::

    RES_MASK, <mask name>, <result name>, <n Adj>, <min> ,<max> 

- [1]: User Defined NodeSet name.
- [2]: VCollab Result name.
- [3]: Number of adjacent layer to mask (optional).
- [4]: Minimum range value to get the nodes within the result (optional).
- [5]: Maximum range value to get the nodes within the result (optional).


.. admonition:: Example

    ::

        RES_MASK,CPMask,Contact Pressure,1,0.01,1000

    - This will create a NodeSet 'CPMask' based on Contact Pressure Masking limits.


PART_MASK
***********

This creates NodeSet from the selected parts for masking.

.. code-block::

    PART_MASK, <maskname>, <partname>, <Proximity dist>, <n Adj>

- [1]: User defined Node set name.
- [2]: Part name to be masked.
- [3]: Proximity of the nodes to be added to the NodeSet.
- [4]: Number of adjacent layer to be masked

.. admonition:: Example

    ::

        PART_MASK,BracketMask,*B*EXCLUDE,NA,1

    - This will create a NodeSet 'BracketMask' based on the nodes in "*B*EXCLUDE*" parts. 1 layer of adjacent nodes is also added to the masking NodeSet 'BracketMask'.


SET_MASK_MODE
**************

This sets the mode of the masking node sets.

.. code-block::

    SET_MASK_MODE ,<MODE>, <mask name list>

- Mode can be 0/1/2.
    - 0 means NA.
    - 1 means In.
    - 2 means Out.
- <mask name list> can be the NodeSet names available for masking.


NODE_MASK
***********

This creates NodeSet from the selected nodes.

.. code-block::

    NODE_MASK, <maskname>, <Radius>, <nodelist>

- [1] maskname: User defined Mask Name.
- [2] Radius: The nodes within this range are added to the NodeSet.It should be floating value.
- [3] nodelist: list of nodes ids for masking.    

.. admonition:: Example

    ::

        NODE_MASK,NodeMask,15.0,11234,3456

    - This will create a NodeSet 'NodeMask' based on the nodeslist 11234,3456.


Hotspot Commands
==================

PROBE_RES
***********

This creates a list of results to be displayed in probe label.

.. code-block::

    PROBE_RES, <ProbeResultList> 


.. admonition:: Example

    ::

        PROBE_RES,*Stress*von*mis*,*Stress*Max*prin*

    - This will create a list of VonMises and Max Principal Stress Probing.


HS_LIMITS
***********

This command sets the Hotspot Dialog Parameters.

.. code-block::

    HS_LIMITS, <filter range: min, max>, <nTop>, <nBottom> ,<ZoneRadius>

- [1]: Sets minimum range value.
- [2]: Sets maximum range value.
- [3]: Number of top hotspots.
- [4]: Number of bottom hotspots.
- [5]: Defines the zone radius for hotspots.

.. image:: media/CAE_Settings_Hotspot.PNG

.. admonition:: Example

    ::

        HS_LIMITS,NA,NA,5,0,20.0

    - This will set the hotspot dialogue box parameters.


COMP_HOTSPOTS
**************

This computes the hotspot with NodeSet masking.

.. code-block::

    COMP_HOTSPOTS, sVPName, Masklist

- [1]: ViewPoint name. 'N' for not adding ViewPoint.
- [2]: Node Sets name for masking.
- If no parameters are given, it will find the hotspot in the GUI. (ViewPoint needs to saved using *ADD_VP* command.)


SET_COMPARE_RES
****************

This sets the Hotspots compare settings.

.. code-block::

    SET_COMPARE_RES, <ON=Y/N>, <BY=0-2>, <MODE=0-2>, <WITH=0-2>, <RADIUS=5.0>, <SHOWALL=Y>, <B2A=Y/N>

- [1] ON=Y/N: Y to set hotspots compare option ON.
- [2] BY=0-2: Sets Comparison of Results mode. Valid Range 0-2.

    - 0: Same Result Name.
    - 1: Selected Results Order.
    - 2: Result's Display Name.

- [3] MODE=0-2: Sets comparison mode. Valid range 0 to 2.

    - 0: For Same Part.
    - 1: For Current Visible Parts.
    - 2: For All parts.

- [4] WITH=0-2: Sets comparison with Valid range 0 to 2.

    - 0: For Same Part.
    - 1: For Current Visible Parts.
    - 2: For All parts.

- [5] RADIUS: Float value. Sets a radius to compare hotspots within a sphere.
- [6] SHOWALL: Y/N. If set to Y, Sets additional label lines to compared node/element of other models.
- [7] B2A=Y/N: If set to Y, finds hotspots in all models and compares across all models. If set to N, find Hotspots only in the current model and those Hotspots are used to compare across all models.

.. admonition:: Example

    ::

        SET_COMPARE_RES,ON=Y,BY=0,MODE=1,WITH=0,RADIUS=5.0,SHOWALL=Y,B2A=N

    - This will set the result compare settings accordingly.


HOTSPOT_VIEW
*************

This creates a ViewPoint with the given hotspots settings.

.. code-block::

    HOTSPOT_VIEW, <sVPName>, <Hotspot Params>

- sVPName: ViewPoint name.
- HS Parameters:

    - [1]: Sets minimum range value.
    - [2]: Sets maximum range value.
    - [3]: Number of top hotspots.
    - [4]: Number of bottom hotspots.
    - [5]: Zone radius for the hotspot.

.. admonition:: Example

    ::

        HOTSPOT_VIEW,Hotspots VP,NA,NA,5,0,20.0

    - This will create new ViewPoint named "Hotspots VP" with top 5 hotspots and zone radius of 20.


LOADCASE_HSVIEW
****************

This creates hotspot view for each instance.

.. code-block::

    LOADCASE_HSVIEW,<VPathName> ,<iFirstInstance>, <iLastInstance>


- [1]: ViewPath name (optional).
- [2]: Starting Instance (optional).
- [3]: Ending Instance (optional).
- If no parameters are provided then, hotspot view for all instances will be generated for the displayed result.

.. admonition:: Example

    ::

        LOADCASE_HSVIEW,sVPathName,5,9

    - This will create new hotspot ViewPoints in ViewPath for instances 5 to 9.


HEADER_POS
***********

This sets the location for header legend (set before PROBE_RES call).

.. code-block::

    HEADER_POS, <Screen_Xpos>, <Screen_Ypos>


- [1]: Screen Xpos (optional).
- [2]: Screen Ypos (optional).
- [3]: Ending Instance (optional).
- If no parameters are provided then, the Screen_Xpos and Screen_Ypos are set to 0.05 and 0.7.


Auto View Commands
====================

MODAL_VPS
************

If Modal data is available this command creates Modal views else it creates hotspot views for each result.

.. code-block::

    MODAL_VPS, <no of modes>, <summary table=Y/N>


- [1]: Number of mode case.
- [2]: Creates a mode case table if set to Y.

.. admonition:: Example

    ::

        MODAL_VPS,5,Y


ALL_RESULT_VPS
***************

This command computes hotspots and creates a ViewPoint. If Modal result is available it creates one Modal ViewPoint.

.. code-block::

    ALL_RESULT_VPS, <nhotspots>


- [1]: Number of Hotspots.
- Results with name <Thickness Bottom Material Force Volume Constraint> are not considered.

.. admonition:: Example

    ::

        ALL_RESULT_VPS,5


COMPARE_GEOM_VPS
*****************

This command finds the difference between the two model's geometry (Merged models) and creates the ViewPoints.

.. code-block::

    COMPARE_GEOM_VPS, <compare mode>, <max search distance>


- [1]: Sets compare mode(Valid range 0-2).

    - 0: Same Parts.
    - 1: Visible Parts.
    - 2: All Parts

- [2] Two model points are compared within this value. Geometry deviation more than this value is ignored.

.. admonition:: Example

    ::

        COMPARE_GEOM_VPS,1,20

ENVELOP_VIEW
*************

This command creates a CAE envelope result for transient or multi-instances data and creates hotspot view.

.. code-block::

    ENVELOP_VIEW, <sResultStr>, <hotspot parameters>


- [1]: Result name for the envelop result.
- HS Parameters list (optional):

    - HS Parameter [0]: Sets minimum range value.
    - HS Parameter [1]: Sets maximum range value.
    - HS Parameter [2]: Number of top hotspots.
    - HS Parameter [3]: Number of bottom hotspots.
    - HS Parameter [4]: Zone radius for the hotspot.
    - hslimits: None, If the user does not want to change the Hotspot settings.
    - DelInst: Instance name that is to be deleted(optional).

.. admonition:: Example

    ::

        ENVELOP_VIEW,*von*Mises*,NA,NA,5,20.0


EXPLODE_VIEW
*************

This command sets parts in an exploded view.

.. code-block::

    EXPLODE_VIEW, <Y/N>, <Percentage(0-100)>


- [1] Y/N: For Explode and reset.
- [2]: Percentage value of current explode. It should be positive and less than or equal to 100.


XY Plot Commands
==================

MINMAX_PLOT
*************

This command creates Min-Max plot for current result.

.. code-block::

    MINMAX_PLOT, <Plot Name>, <iMinmax>


- [1] Min max Plot name.
- [2] iMinmax: Index of curve to be created.

    - 0: Max curve(default).
    - 1: Min curve.
    - 2: Both min and max curves.


HS_XYPLOT
***********

This command computes hotspots and creates Transient XY plot with curves for selected number of hotspots.

.. code-block::

    HS_XYPLOT, <Plot Name>, <MaxHS>


- [1] XY Plot name.
- [2] MaxHS: Max number of hotspots/curves.


SETXYPLOT_WIN
**************

This command sets the XY plot background and windows size.

.. code-block::

    SETXYPLOT_WIN, <bgColor(rgb)>, <winsize(xmin,ymin,xmax,ymax)>


- [1:3]: XY Plot background colors RGB(0 to 1).
- [4:6]: XY Plot window size(xmin,ymin,xmax,ymax).


Other Commands
==================

ADD_2DNOTE
**************

This command adds a 2d note in the ViewPoint.

.. code-block::

    ADD_2DNOTE, <Note String>, <2D position(x, y)>


- [1]: Note text.
- [2]: X and Y normalized position in GUI(0 to 1)

.. admonition:: Example

    ::

        ADD_2DNOTE,Title Page,0.4,0.3


SET_ANIM
**********

This command sets animation type and settings.

.. code-block::

    SET_ANIM, <Type>, <nFrames>, <bStaticFringe(Y/N)>, <Scale factor>, <Speed>


- [1] Type: Animation type, valid values 0/1/3.

    - 0: Linear.
    - 1: Transient.
    - 3: Harmonic.

- [2] nFrames: sets number of frames(instances).
- [3] bStaticFringe: Y for Static fringe.
- [4] Scale factor: Sets scale factor based on bounding box. Deformation percentage is with respect to geometry size.
- [5] Speed: Set delay value to slow animation in milliseconds. Valid range 0 to 100. 100 sets max speed.

.. admonition:: Example

    ::

        SET_ANIM,1,20,Y,3,20


ARRANGE_MODEL
**************

This command arranges the models in a row.

.. code-block::

    ARRANGE_MODEL, <Nrow>


- [1] Nrow: Number of rows to arrange models. If Nrow<0, it resets the model.


HS_TABLE2D
**************

This command creates a hotspots summary table.

.. code-block::

    HS_TABLE2D,<ScreenX>, <ScreenY>, <Header strings>


- [1] ScreenX: X position of table in screen.
- [2] ScreenY: Y position of table in screen.
- [3:] Header text for table fields. 


.. admonition:: Example

    ::

        HS_TABLE2D,0.1,0.6,NodeID,VonMises,StressMaxP


RUN_SCRIPT
************

This command runs a script file with given arguments.

.. code-block::

    RUN_SCRIPT, <ScriptFile>, <bReUse(Y/N)>, <FunctionName>, <Arguments..>


- [1] : Script file path.
- [2] : Set Y to reuse module(optional).
- [3] : Function name in script to be executed.
- [4:]: Arguments for the function.


.. admonition:: Example

    ::

        RUN_SCRIPT,E:\Userlocation\sample.py

