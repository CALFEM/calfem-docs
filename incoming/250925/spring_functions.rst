Spring element functions
========================

The spring element, shown below, can be used for the analysis of
one-dimensional spring systems and for a variety of analogous physical problems.

.. figure:: images/SPRING1.png
    :width: 70%
    :align: center

    Spring element

Quantities corresponding to the variables
of the spring are listed in Table 1.

.. _tanalog:

.. list-table:: Analogous quantities
    :widths: 20 20 20 20 20
    :header-rows: 1

    * - Problem type
      - Spring stiffness
      - Nodal displacement
      - Element force
      - Spring force
    * - Spring
      - :math:`k`
      - :math:`u`
      - :math:`P`
      - :math:`N`
    * - Bar
      - :math:`\frac{EA}{L}`
      - :math:`u`
      - :math:`P`
      - :math:`N`
    * - Thermal conduction
      - :math:`\frac{\lambda A}{L}`
      - :math:`T`
      - :math:`\bar{H}`
      - :math:`H`
    * - Diffusion
      - :math:`\frac{D A}{L}`
      - :math:`c`
      - :math:`\bar{H}`
      - :math:`H`
    * - Electrical circuit
      - :math:`\frac{1}{R}`
      - :math:`U`
      - :math:`\bar{I}`
      - :math:`I`
    * - Groundwater flow
      - :math:`\frac{kA}{L}`
      - :math:`\phi`
      - :math:`\bar{H}`
      - :math:`H`
    * - Pipe network
      - :math:`\frac{\pi D^4}{128{\mu}L}`
      - :math:`p`
      - :math:`\bar{H}`
      - :math:`H`

.. list-table:: Quantities used in different types of problems
    :widths: 20 30 10 40
    :header-rows: 1

    * - Problem type
      - Quantities
      - Designations
      - Description
    * - Spring
      - .. image:: images/ANA1.png
             :width: 61mm
      - :math:`k`, :math:`u`, :math:`P`, :math:`N`
      - spring stiffness, displacement, element force, spring force
    * - Bar
      - .. image:: images/ANA2.png
             :width: 61mm
      - :math:`L`, :math:`E`, :math:`A`, :math:`u`, :math:`P`, :math:`N`
      - length, modulus of elasticity, area of cross section, displacement, element force, normal force
    * - Thermal conduction
      - .. image:: images/ANA3.png
             :width: 61mm
      - :math:`L`, :math:`\lambda`, :math:`T`, :math:`\bar{H}`, :math:`H`
      - length, thermal conductivity, temperature, element heat flow, internal heat flow
    * - Diffusion
      - .. image:: images/ana7.png
             :width: 61mm
      - :math:`L`, :math:`D`, :math:`c`, :math:`\bar{H}`, :math:`H`
      - length, diffusivity, nodal concentration, nodal mass flow, element mass flow
    * - Electrical circuit
      - .. image:: images/ANA4.png
             :width: 61mm
      - :math:`R`, :math:`U`, :math:`\bar{I}`, :math:`I`
      - resistance, potential, element current, internal current
    * - Groundwater flow
      - .. image:: images/ANA5.png
             :width: 61mm
      - :math:`L`, :math:`k`, :math:`\phi`, :math:`\bar{H}`, :math:`H`
      - length, permeability, piezometric head, element water flow, internal water flow
    * - Pipe network (laminar flow)
      - .. image:: images/ANA6.png
             :width: 61mm
      - :math:`L`, :math:`D`, :math:`\mu`, :math:`p`, :math:`\bar{H}`, :math:`H`
      - length, pipe diameter, viscosity, pressure, element fluid flow, internal fluid flow


The following functions are available for the spring element:

.. list-table:: Spring functions
    :widths: 20 120 
    :header-rows: 0

    * - spring1e
      - Compute element matrix
    * - spring1s
      - Compute spring force

.. include:: spring1e.rst
.. include:: spring1s.rst