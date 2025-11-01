factory.py
===============


Define the straight and bend waveguide factories for auto-routing function in **PhotoCAD**.

#. ``StraightFactory`` : Import the straight waveguide to use it for straight connection.

#. ``CircularBendFactory`` : Import ``BendCircular`` from ``bend_circular.py`` and assigned each component to different situations.

    * Note that the default bend radius of every 90-degree bend used for auto-routing was set to be 10 um / 20 um. However, users should define the bend radius themselves to meet the design requirements.

#. ``EulerBendFactory`` : Import ``BendEuler`` from ``bend_euler.py`` and assigned each component to different situations.

    * Note that the default bend radius of every 90-degree bend used for auto-routing was set to be 10 um / 20 um. However, users should define the bend radius themselves to meet the design requirements.

