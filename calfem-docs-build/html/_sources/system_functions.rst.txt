****************
System functions
****************

The group of system functions comprises functions for the setting up, solving,
and elimination of systems of equations. The functions are separated 
in two groups:

* Static system functions
* Dynamic system functions

Static system functions concern the linear system of equations

.. math::

    \mathbf{K} \mathbf{a} = \mathbf{f}

where :math:`\mathbf{K}` is the global stiffness matrix and :math:`\mathbf{f}` is the global load 
vector. Often used static system functions are ``assem`` and ``solveq``.
The function ``assem`` assembles the global stiffness matrix and ``solveq``
computes the global displacement vector :math:`\mathbf{a}` considering the 
boundary conditions. It should be noted that :math:`\mathbf{K}`, :math:`\mathbf{f}`, and :math:`\mathbf{a}`
also represent analogous quantities in systems other than structural mechanical systems.
For example, in a heat flow problem :math:`\mathbf{K}` represents the conductivity matrix,
:math:`\mathbf{f}` the heat flow, and :math:`\mathbf{a}` the temperature.

Dynamic system functions are related to different aspects of linear 
dynamic systems of coupled ordinary differential equations according to

.. math::

    \mathbf{C} \dot{\mathbf{a}} + \mathbf{K} \mathbf{a} = \mathbf{f}

for first-order systems and

.. math::

    \mathbf{M} \ddot{\mathbf{a}} + \mathbf{C} \dot{\mathbf{a}} + \mathbf{K} \mathbf{a} = \mathbf{f}

for second-order systems. First-order systems occur typically in transient 
heat conduction and second-order systems occur in structural dynamics.

Static system functions
=======================

The group of static system functions comprises functions for setting up and solving
the global system of equations. It also contains a function for eigenvalue
analysis, a function for static condensation, a function for extraction of element
displacements from the global displacement vector and a function for extraction of element
coordinates.

.. include:: assem.rst
.. include:: coordxtr.rst
.. include:: eigen.rst
.. include:: extract_ed.rst
.. include:: red.rst
.. include:: solveq.rst
.. include:: statcon.rst

Dynamic system functions
========================

The group of system functions comprises functions for solving linear dynamic systems
by time stepping or modal analysis, functions for frequency domain analysis, etc.

.. include:: dyna2.rst
.. include:: dyna2f.rst
.. include:: fft.rst
.. include:: freqresp.rst
.. include:: gfunc.rst
.. include:: ifft.rst
.. include:: ritz.rst
.. include:: spectra.rst
.. include:: step1.rst
.. include:: step2.rst
.. include:: sweep.rst
