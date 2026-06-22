.. _calfem-utils-function-apply-force:
.. index::
   single: apply_force
   single: calfem.utils.apply_force

calfem.utils.apply_force
^^^^^^^^^^^^^^^^^^^^^^^^

:Purpose:

    Apply boundary force to f matrix. The value is added to all boundaryDofs defined by marker. Applicable to 2D problems with 2 dofs per node.

:Syntax:

.. code-block:: python

    cfu.apply_force(boundaryDofs, f, marker, value=0.0, dimension=0)

:Description:

    Source docstring::

        Apply boundary force to f matrix. The value is
        added to all boundaryDofs defined by marker. Applicable
        to 2D problems with 2 dofs per node.
        
        Parameters:
        
            boundaryDofs        Dictionary with boundary dofs.
            f                   force matrix.
            marker              Boundary marker to assign boundary condition.
            value               Value to assign boundary condition.
                                If not given 0.0 is assigned.
            dimension           dimension to apply force. 0 - all, 1 - x, 2 - y
