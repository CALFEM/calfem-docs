.. _calfem-vis-mpl-function-draw-displacements:
.. index::
   single: draw_displacements
   single: calfem.vis_mpl.draw_displacements

calfem.vis_mpl.draw_displacements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Purpose:

    Draws scalar element values in 2D or 3D. Returns the world object elementsWobject that represents the mesh.

:Syntax:

.. code-block:: python

    cfv.draw_displacements(a, coords, edof, dofs_per_node, el_type, draw_undisplaced_mesh=False, magnfac=-1.0, magscale=0.25, title=None, color=(0, 0, 0), node_color=(0, 0, 0))

:Description:

    Source docstring::

        Draws scalar element values in 2D or 3D. Returns the world object
        elementsWobject that represents the mesh.
        
        Parameters
        ----------
        ev : array_like
            An N-by-1 array or a list of scalars. The Scalar values of the elements. ev[i] should be the value of element i.
        coords : array_like
            An N-by-2 or N-by-3 array. Row i contains the x,y,z coordinates of node i.
        edof : array_like
            An E-by-L array. Element topology. (E is the number of elements and L is the number of dofs per element)
        dofs_per_node : int
            Dofs per node.
        el_type : int
            Element Type. See Gmsh manual for details. Usually 2 for triangles or 3 for quadrangles.
        displacements : array_like
            An N-by-2 or N-by-3 array. Row i contains the x,y,z  displacements of node i.
        axes : matplotlib.axes.Axes
            Matlotlib Axes. The Axes where the model will be drawn. If unspecified the current Axes will be used, or a new Axes will be created if none exist.
        draw_undisplaced_mesh : bool
            True if the wire of the undisplaced mesh should be drawn on top of the displaced mesh. Default False. Use only if displacements != None.
        magnfac : float
            Magnification factor. Displacements are multiplied by this value. Use this to make small displacements more visible.
        title : str
            Changes title of the figure. Default "Element Values".
