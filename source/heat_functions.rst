Heat Flow Elements
==================

Heat flow elements are available for one, two, and three dimensional analysis.
For one dimensional heat flow the spring element ``spring1`` is used.

A variety of important physical phenomena are described by
the same differential equation as the heat flow problem. The heat flow element
is thus applicable in modelling different physical applications.
Table below shows the relation between the primary variable **a**,
the constitutive matrix **D**, and the load vector **f_l**
for a chosen set of two dimensional physical problems.

.. list-table:: Problem dependent parameters
    :header-rows: 1
    :widths: 20 15 20 15 30

    * - Problem type
      - **a**
      - **D**
      - **f_l**
      - Designation
    * - Heat flow
      - :math:`T`
      - :math:`\lambda_x`, :math:`\lambda_y`
      - :math:`Q`
      - :math:`T` = temperature  
         :math:`\lambda_x`, :math:`\lambda_y` = thermal conductivity  
         :math:`Q` = heat supply
    * - Groundwater flow
      - :math:`\phi`
      - :math:`k_x`, :math:`k_y`
      - :math:`Q`
      - :math:`\phi` = piezometric head  
         :math:`k_x`, :math:`k_y` = permeabilities  
         :math:`Q` = fluid supply
    * - St. Venant torsion
      - :math:`\phi`
      - :math:`1/G_{zy}`, :math:`1/G_{zx}`
      - :math:`2\Theta`
      - :math:`\phi` = stress function  
         :math:`G_{zy}`, :math:`G_{zx}` = shear moduli  
         :math:`\Theta` = angle of torsion per unit length

Element types
-------------

.. list-table::
    :widths: 50 50

    * - .. image:: images/flw2t.png
           :width: 50%
           :align: center

        ``flw2te``
      - .. image:: images/flw2i4.png
           :width: 50%
           :align: center

        ``flw2qe``, ``flw2i4e``
    * - .. image:: images/flw2i8.png
           :width: 50%
           :align: center

        ``flw2i8e``
      - .. image:: images/flw3i8.png
           :width: 50%
           :align: center

        ``flw3i8e``


.. list-table:: 2D heat flow functions
    :widths: 20 120 
    :header-rows: 0

    * - flw2te
      - Compute element matrices for a triangular element
    * - flw2ts
      - Compute temperature gradients and flux
    * - flw2qe
      - Compute element matrices for a quadrilateral element
    * - flw2qs
      - Compute temperature gradients and flux
    * - flw2i4e
      - Compute element matrices, 4 node isoparametric element
    * - flw2i4s
      - Compute temperature gradients and flux
    * - flw2i8e
      - Compute element matrices, 8 node isoparametric element
    * - flw2i8s
      - Compute temperature gradients and flux

.. list-table:: 3D heat flow functions
    :widths: 20 120 
    :header-rows: 0

    * - flw3i8e
      - Compute element matrices, 8 node isoparametric element
    * - flw3i8s
      - Compute temperature gradients and flux

.. 2D Heat Flow Functions
.. ----------------------

.. include:: flw2te.rst
.. include:: flw2ts.rst
.. include:: flw2qe.rst
.. include:: flw2qs.rst
.. include:: flw2i4e.rst
.. include:: flw2i4s.rst
.. include:: flw2i8e.rst
.. include:: flw2i8s.rst


.. 3D Heat Flow Functions
.. ----------------------

.. include:: flw3i8e.rst
.. include:: flw3i8s.rst

