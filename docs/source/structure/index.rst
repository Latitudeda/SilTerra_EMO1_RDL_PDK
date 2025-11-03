PDK structure
======================

Process Design Kit (PDK) is a tool for designated users to generate circuit layouts based on SilTerra design rules and technology settings.

``SilTerra_EMO1_RDL_PDK1p3_Latitudeda`` package includes these subfolders: ``components``, ``examples``, ``technology``, and ``util``.

* ``components``

    * Fixed cells: All fixed cells, including ``Fixed_GC_C``, ``FixedMMI_1X2_C``, etc, are designed by **SilTerra** and cannot be changed.

    * Parametrized cells (PCells): Designed by **LDA**, including ``Bend``, ``Straight``, etc. Please see ``gpdk > components`` for more designed components by **LDA**.

* ``examples``

    * ``link_test.py`` : Tests that waveguide types, metal wire types, auto routing, and auto link function works normally under the PDK setting. Please see ``gpdk > examples`` for more circuit examples.


* ``technology``

    * Store the technology setting which matched the SilTerra design rules. We recommend users not to change the settings in technology folder.

    * See chapter ``Technology setting`` for more specific definition.

* ``util``

    * Useful functions when generating circuit layouts.

    * Please see **PhotoCAD** online manual for more information.

* ``SilTerra_EMO1_RDL_PDK1p3_Latitudeda.lyp`` : This file allows layout tools e.g. Klayout to recognize the layer information when displaying gds file to the layout tool.

    .. image:: ../images/lyp.png

