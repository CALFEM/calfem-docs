.. _calfem-vis-mpl-function-draw-nodal-values-shaded:
.. index::
   single: draw_nodal_values_shaded
   single: calfem.vis_mpl.draw_nodal_values_shaded

calfem.vis_mpl.draw_nodal_values_shaded
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Purpose:

    Draw shaded contour plot of nodal values using triangular interpolation. This function creates a shaded contour plot where nodal values are interpolated across triangular elements using Gouraud shading. The visualization shows smooth color gradients representing the variation of values across the mesh.

:Syntax:

.. code-block:: python

    cfv.draw_nodal_values_shaded(values, coords, edof, title=None, dofs_per_node=None, el_type=None, draw_elements=False)

:Description:

    Source docstring::

        Draw shaded contour plot of nodal values using triangular interpolation.
        This function creates a shaded contour plot where nodal values are interpolated
        across triangular elements using Gouraud shading. The visualization shows smooth
        color gradients representing the variation of values across the mesh.
        Parameters
        ----------
        values : array-like
            Nodal values to be plotted. Should have one value per node.
        coords : array-like
            Node coordinates as a 2D array with shape (n_nodes, 2) where each row
            contains [x, y] coordinates.
        edof : array-like
            Element degrees of freedom connectivity matrix. Each row defines the
            nodes that belong to an element.
        title : str, optional
            Title for the plot. If None, no title is displayed.
        dofs_per_node : int, optional
            Number of degrees of freedom per node. Required if draw_elements is True.
        el_type : str, optional
            Element type identifier. Required if draw_elements is True.
        draw_elements : bool, default False
            If True, overlays the mesh elements on the contour plot. Requires
            dofs_per_node and el_type to be specified.
        Notes
        -----
        - The function uses matplotlib's tripcolor with Gouraud shading for smooth
          interpolation between nodal values
        - Element topology is converted to triangular format using topo_to_tri()
        - If draw_elements is True but dofs_per_node or el_type are not provided,
          an informational message is displayed and the mesh is not drawn
        - The plot aspect ratio is automatically set to equal for proper visualization
        Examples
        --------
        >>> coords = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
        >>> edof = np.array([[1, 2, 3], [1, 3, 4]])
        >>> values = np.array([0.0, 1.0, 1.5, 0.5])
        >>> draw_nodal_values_shaded(values, coords, edof, title="Temperature Distribution")
