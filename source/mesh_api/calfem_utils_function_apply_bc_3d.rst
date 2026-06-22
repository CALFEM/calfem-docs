.. _calfem-utils-function-apply-bc-3d:
.. index::
   single: apply_bc_3d
   single: calfem.utils.apply_bc_3d

calfem.utils.apply_bc_3d
^^^^^^^^^^^^^^^^^^^^^^^^

:Purpose:

    Apply boundary condition to bcPresc and bcVal matrices. For 3D problems with 3 dofs per node.

:Syntax:

.. code-block:: python

    cfu.apply_bc_3d(boundaryDofs, bcPrescr, bcVal, marker, value=0.0, dimension=0)

:Description:

    Source docstring::

        Apply boundary condition to bcPresc and bcVal matrices. For 3D problems
        with 3 dofs per node.
        
        Parameters
        ----------
        boundaryDofs : dict
            Dictionary with boundary dofs.
        bcPrescr : array_like
            1-dim integer array containing prescribed dofs.
        bcVal : array_like
            1-dim float array containing prescribed values.
        marker : int
            Boundary marker to assign boundary condition.
        value : float, optional
            Value to assign boundary condition.
            If not given 0.0 is assigned.
        dimension : int, optional
            dimension to apply bc. 0 - all, 1 - x, 2 - y,
            3 - z
        
        Returns
        -------
        bcPrescr : array_like
            Updated 1-dim integer array containing prescribed dofs.
        bcVal : array_like
            Updated 1-dim float array containing prescribed values.
