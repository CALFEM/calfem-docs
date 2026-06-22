.. _calfem-utils-function-apply-bc:
.. index::
   single: apply_bc
   single: calfem.utils.apply_bc

calfem.utils.apply_bc
^^^^^^^^^^^^^^^^^^^^^

:Purpose:

    Apply boundary condition to bcPresc and bcVal matrices. For 2D problems with 2 dofs per node.

:Syntax:

.. code-block:: python

    cfu.apply_bc(boundaryDofs, bcPrescr, bcVal, marker, value=0.0, dimension=0)

:Description:

    Source docstring::

        Apply boundary condition to bcPresc and bcVal matrices. For 2D problems
        with 2 dofs per node.
        
        Parameters
        ----------
        boundaryDofs : dict
            Dictionary with boundary dofs.
        bcPresc : array_like
            1-dim integer array containing prescribed dofs.
        bcVal : array_like
            1-dim float array containing prescribed values.
        marker : int
            Boundary marker to assign boundary condition.
        value : float, optional
            Value to assign boundary condition.
            If not given 0.0 is assigned.
        dimension : int, optional
            dimension to apply bc. 0 - all, 1 - x, 2 - y
        
        Returns
        -------
        bcPresc : array_like
            Updated 1-dim integer array containing prescribed dofs.
        bcVal : array_like
            Updated 1-dim float array containing prescribed values.
