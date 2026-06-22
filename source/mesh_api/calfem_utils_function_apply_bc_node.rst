.. _calfem-utils-function-apply-bc-node:
.. index::
   single: apply_bc_node
   single: calfem.utils.apply_bc_node

calfem.utils.apply_bc_node
^^^^^^^^^^^^^^^^^^^^^^^^^^

:Purpose:

    Apply boundary conditions to a specific node. This function adds boundary condition prescriptions and values for a given node to existing boundary condition arrays.

:Syntax:

.. code-block:: python

    cfu.apply_bc_node(nodeIdx, dofs, bcPrescr, bcVal, value=0.0, dimension=0)

:Description:

    Source docstring::

        Apply boundary conditions to a specific node.
        This function adds boundary condition prescriptions and values for a given node
        to existing boundary condition arrays.
        
        Parameters
        ----------
        nodeIdx : int
            Index of the node to apply boundary conditions to.
        dofs : array_like
            Degrees of freedom array. Can be 1D (for single DOF per node) or 2D
            (for multiple DOFs per node).
        bcPrescr : array_like
            Existing array of prescribed boundary condition DOF indices.
        bcVal : array_like
            Existing array of prescribed boundary condition values.
        value : float, optional
            Value to prescribe for the boundary condition. Default is 0.0.
        dimension : int, optional
            Dimension/direction to apply BC. If 0, applies to all DOFs of the node.
            If 1, 2, or 3, applies to specific dimension (1-indexed). Default is 0.
        
        Returns
        -------
        tuple of numpy.ndarray
            A tuple containing:
            - Updated prescribed DOF indices array (bcPrescr concatenated with new DOFs)
            - Updated prescribed values array (bcVal concatenated with new values)
        
        Notes
        -----
        When dimension=0, boundary conditions are applied to all degrees of freedom
        for the specified node. When dimension is 1, 2, or 3, the boundary condition
        is applied only to that specific dimension (using 1-based indexing).
        
        Examples
        --------
        >>> # Apply BC to all DOFs of node 5 with value 0.0
        >>> bc_dofs, bc_vals = apply_bc_node(5, dofs, [], [], 0.0, 0)
        >>>
        >>> # Apply BC to x-direction (dimension 1) of node 10 with value 5.0
        >>> bc_dofs, bc_vals = apply_bc_node(10, dofs, bc_dofs, bc_vals, 5.0, 1)
