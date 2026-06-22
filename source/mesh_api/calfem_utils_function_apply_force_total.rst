.. _calfem-utils-function-apply-force-total:
.. index::
   single: apply_force_total
   single: calfem.utils.apply_force_total

calfem.utils.apply_force_total
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Purpose:

    Apply boundary force to f matrix. Total force, value, is distributed over all boundaryDofs defined by marker. Applicable to 2D problems with 2 dofs per node.

:Syntax:

.. code-block:: python

    cfu.apply_force_total(boundaryDofs, f, marker, value=0.0, dimension=0)

:Description:

    Source docstring::

        Apply boundary force to f matrix. Total force, value, is
        distributed over all boundaryDofs defined by marker. Applicable
        to 2D problems with 2 dofs per node.
        
        Parameters
        ----------
        boundaryDofs : dict
            Dictionary with boundary dofs.
        f : array_like
            Force matrix.
        marker : int
            Boundary marker to assign boundary condition.
        value : float, optional
            Total force value to assign boundary condition.
            If not given 0.0 is assigned.
        dimension : int, optional
            Dimension to apply force. 0 - all, 1 - x, 2 - y
