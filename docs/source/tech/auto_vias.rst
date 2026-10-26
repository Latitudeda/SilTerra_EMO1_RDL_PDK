auto_vias.py
====================

Define the vias between different metal line types.

In SilTerra PDK, the vias array of the ``UTV`` layer will be added when the connection is made between the metal lines of the ``UTM`` layer and the ``UTM2`` layer. Accordingly, the metal lines on the ``UTM2`` layer and the ``RDL_Met`` layer will be connected via the ``RDL_Via`` layer.

Users are allowed to define vias and change related parameters by their own specific requirements. Please see ``technology > vias.py`` and ``components > via > vias.py`` to modifiy the default vias. Please note that the structure of the vias needs to follow the design rules of **SilTerra**.