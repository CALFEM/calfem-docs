.. _calfem-vis-mpl-function-draw-nodal-values-contour:
.. index::
   single: draw_nodal_values_contour
   single: calfem.vis_mpl.draw_nodal_values_contour

calfem.vis_mpl.draw_nodal_values_contour
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Purpose:

    Draw contour plot of nodal values on a triangulated mesh.

:Syntax:

.. code-block:: python

    cfv.draw_nodal_values_contour(values, coords, edof, levels=12, title=None, dofs_per_node=None, el_type=None, draw_elements=False)

:Description:

    Source docstring::

        Draw contour plot of nodal values on a triangulated mesh.
        
        Parameters
        ----------
        values : array_like
            Nodal values to be plotted as contours.
        coords : array_like
            Coordinates of nodes in the mesh, shape (n_nodes, 2).
        edof : array_like
            Element degrees of freedom connectivity matrix.
        levels : int, optional
            Number of contour levels to draw, default is 12.
        title : str, optional
            Title for the plot, default is None.
        dofs_per_node : int, optional
            Number of degrees of freedom per node, required if draw_elements is True.
        el_type : str, optional
            Element type, required if draw_elements is True.
        draw_elements : bool, optional
            Whether to draw the mesh elements on top of contours, default is False.
        
        Notes
        -----
        The function creates a triangulated contour plot using matplotlib's tricontour.
        If draw_elements is True, both dofs_per_node and el_type must be specified
        to draw the mesh overlay.
        
        The plot uses equal aspect ratio and displays contours of the provided
        nodal values interpolated over the triangulated mesh.
