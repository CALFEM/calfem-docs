.. _calfem-utils-function-apply-force-node:
.. index::
   single: apply_force_node
   single: calfem.utils.apply_force_node

calfem.utils.apply_force_node
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Purpose:

    Apply a force to a specific node in the finite element model. This function adds a force value to the global force vector at the degrees of freedom corresponding to a specified node. The force can be applied to all DOFs of the node or to a specific dimension.

:Syntax:

.. code-block:: python

    cfu.apply_force_node(nodeIdx, dofs, f, value=0.0, dimension=0)

:Description:

    Source docstring::

        Apply a force to a specific node in the finite element model.
        This function adds a force value to the global force vector at the degrees of freedom
        corresponding to a specified node. The force can be applied to all DOFs of the node
        or to a specific dimension.
        Parameters
        ----------
        nodeIdx : int
            Index of the node where the force is to be applied.
        dofs : array_like
            Degrees of freedom array that maps nodes to their DOF indices in the global system.
            Can be 1D (for single DOF per node) or 2D (for multiple DOFs per node).
        f : array_like
            Global force vector where the force will be added.
        value : float, optional
            Magnitude of the force to be applied. Default is 0.0.
        dimension : int, optional
            Specific dimension/DOF to apply the force to. If 0, applies to all DOFs of the node.
            If 1 or higher, applies to the specified dimension (1-indexed). Default is 0.
        Notes
        -----
        - When dimension=0, the force is applied to all DOFs of the node (assumes 1D dofs array)
        - When dimension>=1, the force is applied to the specific dimension of the node
          (assumes 2D dofs array with shape [node, dimension])
        - The dimension parameter uses 1-based indexing (dimension=1 corresponds to first DOF)
        Examples
        --------
        >>> # Apply force to all DOFs of node 5
        >>> apply_force_node(5, dofs, f, value=100.0, dimension=0)
        >>> # Apply force to x-direction (dimension 1) of node 3
        >>> apply_force_node(3, dofs, f, value=50.0, dimension=1)
