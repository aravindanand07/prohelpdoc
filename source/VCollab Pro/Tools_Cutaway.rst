Cutaway
-------
This feature helps users see inside a part or model, like cutting it open. Normally, user can only cut a section with a plane and look at it. But with this new feature, called *Cutaway*, user can choose different shapes like spheres, cylinders, or boxes to cut out. This lets the users understand the inside of the object in more ways.

.. note:-
  This will work only with 'Use Shader' option enabled in Edit | Options dialog.

Cutaway Panel
*************
Cutaway function can be invoked using the menu option **Tools | Cutaway...**

 |image1|


 +------------------+----------------------------------------------------+
 | Cutaway          | Allows user to select a cutaway option. None       |
 |                  | option clears the cutaway function.                |
 +------------------+----------------------------------------------------+
 | Mouse Mode       | Allows users to pick points in the model to define |
 |                  | different cutaway shapes.                          |
 +------------------+----------------------------------------------------+
 | P1               | This point becomes Center for Sphere, Base Circle  |
 |                  | Center for cylinder, Corner 1 for Box shaphes.     |
 +------------------+----------------------------------------------------+
 | P2               | This point becomes Top Center for cylinder and     |
 |                  | Corner 2 for box shapes                            |
 +------------------+----------------------------------------------------+
 | Radius           | Radius for Sphere and Cylinder. User can modify.   |
 +------------------+----------------------------------------------------+
 | Height           | Height for Cylinder.                               |
 +------------------+----------------------------------------------------+
 | Offset           | Incremental step value for all edit fields.        |
 +------------------+----------------------------------------------------+
 | Thickness        | Enabled only for cylinder option. With thickness,  |
 |                  | it becomes pipe.                                   |
 +------------------+----------------------------------------------------+
 | Snap Vertex      | Allows user to pick a nearest vertex in picking.   |
 +------------------+----------------------------------------------------+
 | Invert           | Toggles the culling side. True will cull outside.  |
 +------------------+----------------------------------------------------+
 | Show             | Show/hides the shape with default transparency.    |
 |                  | Users can change the shape color and transparency. |
 +------------------+----------------------------------------------------+
 | Apply            | Applies the modification.                          |
 +------------------+----------------------------------------------------+
 | OK               | Applies the modification and closes dialog.        |
 +------------------+----------------------------------------------------+

Cutaway Types
-------------

|image2|

The following options are supported in cutaway.

- None 
- Sphere
- Cylinder
- Box

Cutaway None
============
Selecting this option will remove all cutaway data and present the model without any culling.

|image3|

Sphere
======

|image4|

In order to define a sphere in VCollab, users have the option to enter center and radius values. VCollab offers default center and radius values based on the model's bounding data.

The center of the sphere can be defined in three ways:
- Manually entering values
- Selecting a vertex in the model
- Selecting three points in the model to derive a circle center

Users also have the ability to manually enter the radius of the sphere.

Steps
#####
- Load a cax file.
- Click Tools | Cutaway
- Select Sphere in the Cutaway drop down list.
- Enter center values manually in the edit boxes provided, 
- Or
- Select *Center* option in the mousemode drop down list. This allows users to pick a point in the model.
- Click a point in the model.
- Enable *Snap Vertex* option to pick a nearest vertex in the model.
- Or
- Select *3Pt Arc* which allow users pick any three points to define a circular arc. Arc center will be used for cutawy sphere center.

|image13|

|image14|

- Enter Sphere radius manully.
- Click Apply.
- Notice in the viewer that cutaway sphere is displayed with transparency and inner portion is culled and visible to the user.
- To pick and move the sphere, Select CutawayPan option.
- Clcik on the cutaway surface and drag it to anywhere in the screen.

  |image7|

- Click *Invert* to toggle the culling side from inside to outside.

  |image10|

Cylinder
========
Once user selects the 'Cylinder' option, Panel changes as follows with base center and top center point.

|image5|

Users can define the cylinder by

- Entering base center and top center manually.
- Entering height will update the top center point values.
- User can pick the base center using Base Center option in mouse mode dropdown
- User can pick the top center using Top Center option in the mouse mode dropdown.
- User can define base center as well as top center by picking 3 points using '3Pt Arc' option in the mouse mode dropdown.
- Cutaway shape can be moved horizontally and vertically using *CutawayPan* option.

|image8|

- Toggle the culling side using *Invert* option

|image11|

Box
===
Once user selects the 'Box' option, Panel changes as follows with Corner 1 and Corner 2 points.

|image6|

User can define the box by, 

- Entering two extreme corner point values manually,
- Pick Corner 1 and Corner 2 points using *Corner 1* and *Corner 2* options in the mouse mode dropdown.
- Shape can be moved using CutawayPan option in mouse mode dropdown.

|image9|

- User can toggle the culling side using *Invert* option.

|image12|

Other options
=============
**Snap Vertex** - allows user to pick nearest vertex in moused mode.

**Invert** - allows to toggle the culling side and can visualize the zone in alternate way.

**Show** - allows to show or hide the cutaway shape. User can change the color of the shape and can control the shape transparency.

**Offset** and **Spin Control** - User can increment or decrement any edit field by step size value in 'Offset' field using the spin control.
For example, if the offset value is 5, then spin control for any edit fiels increase or decrease 5 units for each click.

    
.. |image1| image:: JPGImages/Cutaway_Panel.PNG    
.. |image2| image:: JPGImages/Cutaway_Shapes.png  
.. |image3| image:: JPGImages/Cutaway_None.png
.. |image4| image:: JPGImages/Cutaway_Sphere_Panel.PNG
.. |image5| image:: JPGImages/Cutaway_Cylinder_Panel.PNG
.. |image6| image:: JPGImages/Cutaway_Box_Panel.PNG

.. |image7| image:: JPGImages/Cutaway_sphere.png
.. |image8| image:: JPGImages/Cutaway_Cylinder.png
.. |image9| image:: JPGImages/Cutaway_Box.png

.. |image10| image:: JPGImages/Cutaway_Sphere_Invert.png
.. |image11| image:: JPGImages/Cutaway_Cylinder_Invert.png
.. |image12| image:: JPGImages/Cutaway_Box_Invert.png

.. |image13| image:: JPGImages/Cutaway_3Point_Arc_Pre_Sphere.png
.. |image14| image:: JPGImages/Cutaway_3Point_Arc_Sphere.png
