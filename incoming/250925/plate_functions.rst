Plate element functions
=======================

Only one plate element is currently available, a rectangular 12 dof element.
The element presumes a linear elastic material which can be isotropic or anisotropic.

.. list-table:: **Plate elements**
    :widths: 50 50
    :header-rows: 0

    * - .. image:: images/PLATR.png
             :width: 70%

        .. centered:: ``platre``
      - ..

.. list-table:: Plate functions
    :widths: 20 120 
    :header-rows: 0

    * - planre
      - Compute element matrices
    * - planrs
      - Compute section forces

.. include:: platre.rst
.. include:: platrs.rst
