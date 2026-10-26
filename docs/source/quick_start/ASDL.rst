AdvancedSDL
=======================================

Import SilTerra PDK into AdvancedSDL
*******************************************

Click ``PDK`` on the top toolbar of **AdvancedSDL** and select ``Open PDK Symbol Design``.

.. image:: ../images/ASDL_1.png

Locate and select the ``SilTerra`` folder.

.. image:: ../images/ASDL_2.png

After the import is complete, you will see the ``SilTerra`` component library on the left.

.. image:: ../images/ASDL_3.png

Click ``File`` and then click ``New Project``.

.. image:: ../images/ASDL_4.png

Enter the project name and path, select ``SilTerra`` PDK in the PDK column, and click ``OK``.

.. image:: ../images/ASDL_5.png

Wait for the contents of ``Import SilTerra_EMO1_RDL_PDK_rev13p0_Latitude PDK symbols succeeded`` to appear in the output. The project automatically creates a new circuit ``Untitled_1``, and the SilTerra PDK component library is at the bottom left.

.. image:: ../images/ASDL_6.png

Drag components to the center region. Click on the component, the parameters of the component can be adjusted on the right side.

.. image:: ../images/ASDL_7.png

Once the parameters are set, connect the ports to route the components and click SDL in the upper right.

.. image:: ../images/ASDL_8.png

The corresponding layout is displayed in the ``Layout View``. And it generates python layout code called ``Generated-Script.py``.

.. image:: ../images/ASDL_9.png

The ``Generated-Script.py`` can be run in **PhotoCAD** and modified to create a new layout. The script is saved in the project's Temp folder.

.. image:: ../images/ASDL_10.png

Users can also easily import a specific component to **AdvancedSDL** on **PhotoCAD** using ``fp.export_schematic``. See ``gpdk > examples`` for more information.
