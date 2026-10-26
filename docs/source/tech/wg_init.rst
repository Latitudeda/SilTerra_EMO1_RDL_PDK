__init__.py
===================

Define the WG class which consists of classes such as ``STRIP.C.WIRE`` / ``LRIB.C.WIRE`` / ``HRIB.C.WIRE`` / ``SIN_STRIP.C.WIRE`` / ``SIN_STRIP1.C.WIRE`` / ``SIN_RIB.C.WIRE`` / ``SIN_RIB1.C.WIRE``. The width of the waveguide is set here according the parameters in ``constant.py`` file. **PhotoCAD** also supports CD bias control of the waveguide width. The CD bias setting can be implemented in ``strip.py`` / ``lrib.py`` / ``hrib.py`` / ``sin_strip.py`` / ``sin_strip1.py`` / ``sin_rib.py`` / ``sin_rib1.py``.

.. table:: Waveguide Type Table

    ================================  ==========================================
    WAVEGUIDE_TYPE                    PARAMETERS
    ================================  ==========================================
    `TECH.WG.STRIP.C.WIRE`            core_width=0.5000, cladding_width=8.5000
    `TECH.WG.STRIP.O.WIRE`            core_width=0.4000, cladding_width=8.4000
    `TECH.WG.LRIB.C.WIRE`             core_width=0.5000, cladding_width=8.5000
    `TECH.WG.LRIB.O.WIRE`             core_width=0.4000, cladding_width=8.4000
    `TECH.WG.HRIB.C.WIRE`             core_width=0.5000, cladding_width=8.5000
    `TECH.WG.HRIB.O.WIRE`             core_width=0.4000, cladding_width=8.4000
    `TECH.WG.SIN_STRIP.C.WIRE`        core_width=1.0000, cladding_width=9.0000
    `TECH.WG.SIN_STRIP.O.WIRE`        core_width=0.8000, cladding_width=8.8000
    `TECH.WG.SIN_STRIP1.C.WIRE`       core_width=1.0000, cladding_width=9.0000
    `TECH.WG.SIN_STRIP1.O.WIRE`       core_width=0.8000, cladding_width=8.8000
    `TECH.WG.SIN_RIB.C.WIRE`          core_width=1.0000, cladding_width=9.0000
    `TECH.WG.SIN_RIB.O.WIRE`          core_width=0.8000, cladding_width=8.8000
    `TECH.WG.SIN_RIB1.C.WIRE`         core_width=1.2000, trench_width=8.0000
    `TECH.WG.SIN_RIB1.O.WIRE`         core_width=1.0000, trench_width=8.0000
    ================================  ==========================================