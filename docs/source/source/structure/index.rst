PDK structure
======================

Process Design Kit (PDK) is a tool for designated users to generate circuit layouts based on IOPTEE design rules and technology settings.

``IOPTEE_PDK2p0_Latitudeda_BB`` package includes six subfolders: ``components``, ``examples``, ``schematic``, ``symbols``, ``technology``, and ``util``.

* ``components``

    * Fixed cells: All fixed cells, including ``Edge Coupler``, ``Grating Coupler``, ``Crossing``, ``Heater``, ``Block`` and ``MultiMode Interferometer``, are named and designed by **IOPTEE** and cannot be changed.

    * Parametrized cells (PCells): Designed by **IOPTEE**, including ``Mach-Zehnder interferometer`` and ``Microring`` and by **LDA**, including ``Bend``, ``Straight``, etc. Please see ``gpdk > components`` for more designed components by **LDA**.

* ``examples``

    * ``link.py`` : Test circuit to test if the cell (``edge_coupler_3p5um_y_BB`` and ``grating_coupler_y_BB``), auto routing, and auto link function works normally under the PDK setting. Please see ``gpdk > examples`` for more circuit examples.

    * ``ec_placement.py`` : An example of ``Edge Coupler`` (``edge_coupler_3p5um_y_BB`` and ``edge_coupler_6p5um_y_BB``) placement, **op_1** of ``Edge Coupler`` should be placed at x=0 um or x=20000 um in the ``Block``.

* ``schematic``

    * Store the schematic setting for linking PhotoCAD to AdvancedSDL.

* ``symbols``

    * Store the symbol setting for linking PhotoCAD to AdvancedSDL.

* ``technology``

    * Store the technology setting which matched the IOPTEE design rules. We recommend users not to change the settings in technology folder.

    * See chapter ``Technology setting`` for more specific definition.

* ``util``

    * Useful functions when generating circuit layouts.

    * Please see **PhotoCAD** online manual for more information.

* ``layers.lyp`` : This file allows layout tools e.g. Klayout to recognize the layer information when displaying gds file to the layout tool.

    .. image:: ../images/lyp.png

