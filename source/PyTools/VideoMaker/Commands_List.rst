**************************
List of Commands
**************************


Set Parameters
==============

VPANIM_PARAMS
**************

This command contains parameters responsible for smoothness of the video generation.

.. code-block:: 

    VPANIM_PARAMS,nFrame_VP2VP,nImgsPerView=1,iSectionAnimFrames,iExplodeAnimFrames,bAnimTransparency(Y/N)

    Default Values: 20,1,20,20,Y

- [1] nFrame_VP2VP: Specify number of frames while navigating from ViewPoint to ViewPoint
- [2] nImgsPerView: Specify number of images to be captured for video creation for the view 
- [3] iSectionAnimFrames: Specify number of frames for showing section cut animation; 0 => Off
- [4] iExplodeAnimFrame: Specify number of frames for Explode operation, 0 => Off
- [5] bAnimTransparency(Y/N): To set part show/hide transparancy animation on (Y) or off (N). Default Y

VPANIM_CAEPARAMS
*****************

This command contains parameters to control CAE animation smoothness. If viewpoint has animation, it will show animation after moving to that viewpoint.

.. code-block:: 

    VPANIM_CAEPARAMS,bCAEAnim(Y/N),nCylesPerView,nFramesPerCyle,nImgsPerCAEFrame

    Default Values:Y,1,0,1

- [1] bCAEAnim (Y/N): Specify if CAE Animation capture is required for video generation, Yes or No
- [2] nCylesPerView: Specify the number of cycles of the CAE animation to be captured
- [3] nFramesPerCyle: Specify the number of frames for CAE Animation. Specify 0 to use animation dialog parameter
- [4] nImgsPerCAEFrame: Specify the number of images per frame to be captured


ViewPoint Animation
====================

VP2VP_ANIM
***********
This command captures ViewPoint animation of the ViewPoints as listed in index. The animation parameters are defined using VPANIM_PARAMS and VPANIM_CAEPARAMS commands.

.. code-block:: 

    VP2VP_ANIM,index1,index2

- [1] index1: Specify ViewPoint index number to start from
- [2] index2: Specify ViewPoint index number to end with. If index2 is 0, all ViewPoints are animated

MORPHANIM_VP2VP
***************
This command captures animation of image morphing from one viewpoint to another.

.. code-block:: 

    MORPHANIM_VP2VP,vpIndex1,vpIndex2,nFrames,sMethod

- [1] vpindex1: Specify ViewPoint index of first frame. Specify N for current display
- [2] vpindex2: Specify ViewPoint index for the second frame.
- [3] nFrames: Specify number of frames for morphing
- [4] sMethod: Specify a method for morphing

    - F1 : Fade
    - R1 : Left to Right Roll/Drag from first frame image to second
    - R2 : Right to Left Roll from first frame image to second
    - R3 : Top to Bottom Roll from first frame image to second
    - R4 : Bottom to Top Roll from first frame image to second
    - C1 : Left to Right Cover - second frame image onto first
    - C2 : Right to Left Cover - second frame image onto first
    - C3 : Top to Bottom Cover - second frame image onto first
    - C4 : Bottom to Top Cover - second frame image onto first


GO2VP_ANIM
***********

This command animates from current model view to the specified ViewPoint.

    .. code-block:: 

        GO2VP_ANIM,ViewPath/N,ViewPointName/Index

    - [1] ViewPath/N: Specify the ViewPath name to be selected, user can select *N* for current ViewPath
    - [2] ViewPoint/index: Specify the ViewPoint name or index to which the model view will be moved

APPLY_VP
*********

This command applies the specified ViewPoint. Images are not captuted.

.. code-block:: 

    APPLY_VP,vpindex

- [1] vpindex: Specify the ViewPoint index value (starts from 1)

Model movements
================

ROTATE_MODEL
*************

This command rotates the model about an axis with respect to the center. Animation frames are captured.

.. code-block:: 

    ROTATE_MODEL,Axis[x,y,z],bScreen(Y/N),fTeta,nFrames,PartNameInfo=ALL/NONE/ADD/DEL/ONLY/INVERT/VP,Part name list

- [1] Axis x,y,z: Specify the axis of rotation. For example: Rotation about Z-axis will be denoted as 0,0,1
- [2] bScreen: Specify if coordinate system for rotation should be Global or Camera/Screen
- [3] fTheta: Specify the angle of rotation
- [4] nFrames: Specify the number of frames for a smoother video capture
- [5] PartNameInfo: Specify the moving parts list for rotation. Optional(Default is current moving parts list)

    - ALL/NONE: All visible parts are considered. [6] is not used for this option
    - INVERT: All visible parts which are not present in current moving parts list. [6] is not used for this option
    - ADD: Add user specified parts to the current moving parts list. [6] is parts list
    - DEL: Delete user specified parts from the current moving parts list. [6] is is parts list
    - ONLY: Only user-specified parts will be considered. [6] is parts list
    - VP: Displayed parts in the user-specified ViewPoint will be considered

- [6] Specify the part names list(Wild card character '*' is supported), or ViewPoint and ViewPath

MOVE_MODEL
***********

This command translates the model in a user-specified direction. Animation frames are captured.

.. code-block::

    MOVE_MODEL,Vector[x,y,z],bScreen(Y/N),fLength,nFrames,PartNameInfo=ALL/NONE/ADD/DEL/ONLY/INVERT/VP,Part name list

- [1] x,y,z: Specify vector direction for translation. For example: Translation in Z-axis will be denoted as 0,0,1
- [2] bScreen: Specify if coordinate system for rotation should be Global or Camera/Screen
- [3] fLength: Specify the length of translation
- [4] nFrames: Specify the number of frames for a smoother video capture
- [5] PartNameInfo: Specify the moving parts list for translation. Optional(Default is current moving parts list)

    - ALL/NONE: All visible parts are considered. [6] is not used for this option
    - INVERT: All visible parts which are not present in current moving parts list. [6] is not used for this option
    - ADD: Add user specified parts to the current moving parts list. [6] is parts list
    - DEL: Delete user specified parts from the current moving parts list. [6] is is parts list
    - ONLY: Only user-specified parts will be considered. [6] is parts list
    - VP: Displayed parts in the user-specified ViewPoint will be considered

- [6] Specify the part names list(Wild card character '*' is supported), or ViewPoint and ViewPath

SET_MOVING_PARTS
*****************

This command specifies the user-defined part name list for *ROTATE_MODEL* or *MOVE_MODEL*.

.. code-block::

    SET_MOVING_PARTS,ALL/NONE/ADD/DEL/ONLY/INVERT/VP,Part name list

- [1] PartNameInfo: Specify the part selection option:

    - ALL/NONE: All visible parts are considered. [2] is not used for this option
    - INVERT: All visible parts which are not present in current moving parts list. [2] is not used for this option
    - ADD: Add user specified parts to the current moving parts list. [2] is parts list
    - DEL: Delete user specified parts from the current moving parts list. [2] is parts list
    - ONLY: Only user-specified parts will be considered. [2] is parts list
    - VP: Displayed parts in the user-specified ViewPoint will be considered

- [2] Specify the part names list (Wild card character '*' is supported), or ViewPoint and ViewPath

RESET_ALLMOVES
****************

This command resets all moves previously specified, and no image is captured for this command for video command.

.. code-block::

    RESET_ALLMOVES

Camera movements
=================

ROTATE_CAMERA
**************

This command rotates the camera to capture video while the model remains at the same location.

.. code-block::

    ROTATE_CAMERA,Axis[x,y,z],fDegrees,nFrames,bRelativeToScreen(Y/N),vector<float> rotation_centervector

- [1] Axis x,y,z: Specify the axis of rotation. For example: Rotation about Z-axis will be denoted as 0,0,1
- [2] fDegrees: Specify the angle of rotation in degrees
- [3] nFrames: Specify the number of frames for a smoother video capture
- [4] bRelativeToScreen: Specify if rotation of camera is with respect to screen
- [5] Rotation_Center [x,y,z]: Specify the rotation center

MOVE_CAMERA
************

This command translates the camera to capture video while the model remains at the same location.

.. code-block::

    MOVE_CAMERA,Translation Vector[x,y,z],nFrames,bRelativeToScreen(Y/N)

- [1] Vector x,y,z: Specify the translation vector. For example: Translation in Z-axis will be denoted as 0,0,1
- [2] nFrames: Specify the number of frames for a smoother video capture
- [3] bRelativeToScreen: Specify if translation of camera is with respect to screen

MOVE_CAMERA_DIR
***************

This command translates the camera to capture video while the model remains at the same location.
In this case translation vector is defined by direction vector and distance.

.. code-block::

    MOVE_CAMERA_DIR, <float> Direction Vector, float Distance,int nFrames,bool bRelativeToScreen


- [1] Direction Vector x,y,z: Specify the translation vector (3 float values) (Program will normalise)
- [2] Distance: translation distance
- [3] nFrames: Specify the number of frames for video capture
- [4] bRelativeToScreen: Specify if translation of camera is with respect to screen

Insert Video / Image File
==========================

INSERT_VIDEO
*************

This command inserts the video from a user-specified file path.

.. code-block::

    INSERT_VIDEO,filepath

- [1] filepath


INSERT_IMGFOLDER
*****************

This command inserts images from a user-specified folder path.

.. code-block::

    INSERT_IMGFOLDER,folderpath

- [1] folderpath


Capture CAE Animation
======================

CAPUTRE_CAEANIM
*****************

This command captures the CAE Animation in the current ViewPort. Viewpoint need not have animation stored.

.. code-block::

    CAPUTRE_CAEANIM

.. note:: It is recommended to preceed this command with *VPANIM_CAEPARAMS*. All parameters set will be used for capturing CAE animation.

Save Video to File
===================

SAVE_VIDEO
************

This command creates and saves the video (from the captured images) in the user-defined file path. Note that video can also be saved using GUI. Note that, all the images in the temporary folder will be deleted after creating the video.

.. code-block::

    SAVE_VIDEO,filepath,iSpeed[-4 to 3]

- [1] filepath: Specify user-defined location(along with filename and extension) for saving the video
- [2] iSpeed: Specify speed of the video, -4 being the slowest and 3 being the fastest


Explode Animation
==================

EXPLODE_ANIM
*************

This command captures the exploded animation.

.. code-block::

    EXPLODE_ANIM,percent(0-100),bReset,nFrames

- [1] percent: Specify the explode percentage
- [2] bReset: Specify if model needs to be reset after explosion
- [3] nFrames: Specify number of frames for smoother video capture


EXPLODE_DIR
************

This command captures the exploded animation in a user-defined direction.

.. code-block::

    EXPLODE_DIR,dirvec,Scale,SortBy(Top/Bot/Mid/Width),bReset,nFrames

- [1] dirvec: Specify the explosion direction. For example: Explosion in z-axis will be denoted as 0,0,1
- [2] Scale: Specify the explosion scale
- [3] SortBy: Specify the method used for sequencing parts during the animation

    - Top: Parts are arranged from the top
    - Bot: Parts are arranged from the bottom
    - Mid: Parts are arranged from the middle of the assembly
    - Size: Parts are arranged based on bounding box size (small parts maximum distance)

    .. image:: media/EXPLODE_DIR.PNG
        :width: 200


- [4] bReset: Specify if model needs to be reset after explosion
- [5] nFrames: Specify number of frames for smoother video capture

Capture Images
===============

CAPUTRE_WAIT
*************

This command adds specified number of frames from the current display (Animation will wait)

.. code-block::

    CAPUTRE_WAIT,nFrames

- [1] nFrames: Specify the user-defined number of frames


CAPTURE_IMAGE
**************

This command captures the current view as image.

.. code-block::

    CAPTURE_IMAGE


ViewPoint
==========

SELECT_VPATH
*************

This command selects the user-defined ViewPath and ViewPoint. Set the current viewpath.

.. code-block::

    SELECT_VPATH,ViewPath Name,VP index

- [1] Viewpath Name: Specify the user-defined ViewPath Name
- [2] VP index: Specify the user-defined ViewPoint index


Others
=======

SHOWCMDS
*********

This command enables displaying the given commands.

.. code-block::

    SHOWCMDS,bCmd=True/False

- [1] bCmd: Specify to show commands by True/False. Default is False


START_CAEANIM
***************

This command defines parameters for CAE animation indicating to start the animation during camera/model movement animation. This command can be used to show CAE animation while moving the model (independent of Viewpoint Animation)

.. code-block::

    START_CAEANIM,nCycles,Animtype(0/1/3/N),nFrames,bDeform(Y/N)

- [1] nCycles: Specify the number of times the animation would run for
- [2] Specify the CAE Animation type:

    - 0 indicates Linear Animation
    - 1 indicates Transient Animation
    - 3 indicates animating contour color based on Legend Palette using transparency
    - N use animation type from animation dialog

- [3] nFrames: Specify the number of frames for video capture
- [4] bDeform: Specify if deformation is required in the animation or not

STOP_CAEANIM
*************

This command stops the CAE Animation during the camera movement.

.. code-block::

    STOP_CAEANIM
    
EXIT
*****

This command stops the execution of command statements.

.. code-block::

    EXIT