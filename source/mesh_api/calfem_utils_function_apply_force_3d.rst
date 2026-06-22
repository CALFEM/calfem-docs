.. _calfem-utils-function-apply-force-3d:
.. index::
   single: apply_force_3d
   single: calfem.utils.apply_force_3d

calfem.utils.apply_force_3d
^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Purpose:

    Apply boundary force to f matrix for 3D problems. The value is added to all boundaryDofs defined by marker. Applicable to 3D problems with 3 degrees of freedom per node.

:Syntax:

.. code-block:: python

    cfu.apply_force_3d(boundaryDofs, f, marker, value=0.0, dimension=0)

:Description:

    Source docstring::

        Apply boundary force to f matrix for 3D problems.
        The value is added to all boundaryDofs defined by marker. Applicable
        to 3D problems with 3 degrees of freedom per node.
        Parameters
        ----------
        boundaryDofs : dict
            Dictionary with boundary degrees of freedom.
        f : numpy.ndarray
            Force matrix to be modified.
        marker : int or str
            Boundary marker to identify which boundary condition to apply.
        value : float, optional
            Value to add to the force matrix at specified boundary DOFs.
            Default is 0.0.
        dimension : int, optional
            Dimension to apply force:
            * 0 - all dimensions (default)
            * 1 - x-direction only
            * 2 - y-direction only
            * 3 - z-direction only
        Notes
        -----
        If the specified marker does not exist in boundaryDofs, an error message
        is printed. If an invalid dimension is specified (not 0, 1, 2, or 3),
        an error message is printed.
        Examples
        --------
        >>> boundaryDofs = {1: [1, 2, 3, 4, 5, 6]}
        >>> f = np.zeros(6)
        >>> apply_force_3d(boundaryDofs, f, 1, value=100.0, dimension=1)
        # Applies force of 100.0 in x-direction to DOFs 1, 4
