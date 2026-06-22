.. _calfem-vis-mpl-function-draw-nodal-values-contourf:
.. index::
   single: draw_nodal_values_contourf
   single: calfem.vis_mpl.draw_nodal_values_contourf

calfem.vis_mpl.draw_nodal_values_contourf
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Purpose:

    Draw filled contour plot of nodal values on a finite element mesh. This function creates a filled contour plot (tricontourf) to visualize scalar values at the nodes of a finite element mesh. The contours are interpolated over triangular elements derived from the mesh topology.

:Syntax:

.. code-block:: python

    cfv.draw_nodal_values_contourf(values, coords, edof, levels=12, title=None, dofs_per_node=None, el_type=None, draw_elements=False)

:Description:

    Source docstring::

        Draw filled contour plot of nodal values on a finite element mesh.
        This function creates a filled contour plot (tricontourf) to visualize scalar values
        at the nodes of a finite element mesh. The contours are interpolated over triangular
        elements derived from the mesh topology.
        Parameters
        ----------
        values : array_like
            Nodal values to be plotted as contours. Should have one value per node.
        coords : array_like
            Node coordinates array with shape (n_nodes, 2) where each row contains
            [x, y] coordinates of a node.
        edof : array_like
            Element topology array defining the connectivity between elements and
            degrees of freedom/nodes.
        levels : int, optional
            Number of contour levels to draw. Default is 12.
        title : str, optional
            Title for the plot. If None, no title is set. Default is None.
        dofs_per_node : int, optional
            Number of degrees of freedom per node. Required if draw_elements is True.
            Default is None.
        el_type : str, optional
            Element type identifier. Required if draw_elements is True. Default is None.
        draw_elements : bool, optional
            Whether to overlay the mesh elements on the contour plot. If True,
            dofs_per_node and el_type must be specified. Default is False.
        Notes
        -----
        - The function uses matplotlib's tricontourf for creating filled contours
        - Element topology is converted to triangular connectivity using topo_to_tri
        - The plot aspect ratio is set to 'equal' for proper geometric representation
        - If draw_elements is True but required parameters are missing, an info message is displayed
        Examples
        --------
        >>> coords = np.array([[0, 0], [1, 0], [0.5, 1]])
        >>> edof = np.array([[1, 2, 3]])
        >>> values = np.array([1.0, 2.0, 1.5])
        >>> draw_nodal_values_contourf(values, coords, edof, levels=10, title="Temperature")
