.. _calfem-vis-mpl-function-draw-element-values:
.. index::
   single: draw_element_values
   single: calfem.vis_mpl.draw_element_values

calfem.vis_mpl.draw_element_values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Purpose:

    Draws scalar element values in 2D or 3D.

:Syntax:

.. code-block:: python

    cfv.draw_element_values(values, coords, edof, dofs_per_node, el_type, displacements=None, draw_elements=True, draw_undisplaced_mesh=False, magnfac=1.0, title=None, color=(0, 0, 0), node_color=(0, 0, 0))

:Description:

    Source docstring::

        Draws scalar element values in 2D or 3D.
        
        Parameters
        ----------
        values : array_like
            An N-by-1 array or a list of scalars. The Scalar values of the elements. ev[i] should be the value of element i.
        coords : array_like
            An N-by-2 or N-by-3 array. Row i contains the x,y,z coordinates of node i.
        edof : array_like
            An E-by-L array. Element topology. (E is the number of elements and L is the number of dofs per element)
        dofs_per_node : int
            Dofs per node.
        el_type : int
            Element Type. See Gmsh manual for details. Usually 2 for triangles or 3 for quadrangles.
        displacements : array_like, optional
            An N-by-2 or N-by-3 array. Row i contains the x,y,z displacements of node i.
        draw_elements : bool, optional
            True if mesh wire should be drawn. Default True.
        draw_undisplaced_mesh : bool, optional
            True if the wire of the undisplaced mesh should be drawn on top of the displaced mesh. Default False. Use only if displacements != None.
        magnfac : float, optional
            Magnification factor. Displacements are multiplied by this value. Use this to make small displacements more visible.
        title : str, optional
            Changes title of the figure. Default "Element Values".
        color : tuple or str, optional
            Color of the wire.
        node_color : tuple or str, optional
            Color of the nodes.
