.. _calfem-utils-function-apply-force-total-3d:
.. index::
   single: apply_force_total_3d
   single: calfem.utils.apply_force_total_3d

calfem.utils.apply_force_total_3d
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Purpose:

    Apply boundary force to f matrix. Total force, value, is distributed over all boundaryDofs defined by marker. Applicable to 3D problems with 3 dofs per node.

:Syntax:

.. code-block:: python

    cfu.apply_force_total_3d(boundaryDofs, f, marker, value=0.0, dimension=0)

:Description:

    Source docstring::

        Apply boundary force to f matrix. Total force, value, is
        distributed over all boundaryDofs defined by marker. Applicable
        to 3D problems with 3 dofs per node.
        
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
            Dimension to apply force. 0 - all, 1 - x, 2 - y,
            3 - z
