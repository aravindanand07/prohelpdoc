Anti  Alias
===========
Hardware based Anti Alias for  smooth geometry display is supported in Display->AntiAlias menu. To make use of it, it is required to enable anti alias feature in **Display Hardware setting**.

.. note::
  The application must be restarted in order for the modification to take effect.
  
What is Anti-Alias?
-------------------
Antialiasing is a technique used in computer graphics to remove the aliasing effect. The aliasing effect is the appearance of jagged edges or “jaggies” in a rasterized image (an image rendered using pixels). Aliasing occurs when real-world objects which comprise of smooth, continuous curves are rasterized using pixels.

How to enable or disable Anti-Alias?
************************************
- Click to Display | Anti Alias
- Close the application
- **Restart** the application
- Load a cax file and notice the smoothness in the rendering.

How to enable or disable Antialiasing for Video Drivers?
********************************************************
 For NVIDIA Video Cards,

  #. Open the Nvidia Control Panel window by clicking the Nvidia icon in the system tray or the Start menu.

  #. Click the "Manage 3D Settings" link in the 3D Settings section.

  #. Click the "Antialiasing - Mode" option to select it, and then select "Off" or any other mode in the box next to it.

  #. Click "Apply" to apply the new settings, and then close the Nvidia Control Panel window.

  References: -

  `NVIDIA Configuring <https://www.techwalla.com/articles/how-to-disable-anti-aliasing-with-nvidia>`_.


 For ATI Video Cards,

  #. Open the AMD Catalyst Control Center window by clicking the Catalyst icon in the system tray or in the Start menu.

  #. Click the "3D" node in the left pane, and then click the "Anti-Aliasing" link to view the antialiasing settings in the right pane.

  #. Select the "Use application settings" option in the "Smoothvision HD: Anti-Aliasing" section. Each application uses its own antialiasing options, so you just need to turn off or trun on the antialiasing option in the application's settings.

  References:-

  `AMD Catalyst Control Center <https://stepmodifications.org/wiki/Guide:AMD_Catalyst_Control_Center>`_.

  `AMD Radeon Configuring <https://www.amd.com/en/support/kb/faq/dh-012#faq-Anti-Aliasing-Mode>`_.
