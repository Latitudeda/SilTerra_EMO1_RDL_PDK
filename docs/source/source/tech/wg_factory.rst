factory.py
===============


Define the straight and bend waveguide factories for auto-routing function in **PhotoCAD**.

#. ``StraightFactory`` : Import the straight waveguide to use it for straight connection.

#. ``CircularBendFactory`` : Import ``BendCircular`` and ``BendCircular90`` from ``bend_circular`` and assigned each component to different situations.

    * Note that the default bend radius of every 90-degree bend used for auto-routing was set to be 80 um. However, users should define the bend radius themselves to meet the design requirements.

#. ``EulerBendFactory`` : Import ``BendEuler`` and ``BendEuler90`` from ``bend_euler`` and assigned each component to different situations.

    * Note that the default bend radius of every 90-degree bend used for auto-routing was set to be 80 um. However, users should define the bend radius themselves to meet the design requirements.

