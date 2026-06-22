.. _calfem-vis-mpl-function-draw-mesh:
.. index::
   single: draw_mesh
   single: calfem.vis_mpl.draw_mesh

calfem.vis_mpl.draw_mesh
^^^^^^^^^^^^^^^^^^^^^^^^

:Purpose:

    Draws wire mesh of model in 2D or 3D. Returns the Mesh object that represents the mesh.

:Syntax:

.. code-block:: python

    cfv.draw_mesh(coords, edof, dofs_per_node, el_type, title=None, color=(0, 0, 0), face_color=(0.8, 0.8, 0.8), node_color=(0, 0, 0), filled=False, show_nodes=False)

:Description:

    Source docstring::

        Draws wire mesh of model in 2D or 3D. Returns the Mesh object that represents
        the mesh.
        
        Parameters
        ----------
        coords : ndarray
            An N-by-2 or N-by-3 array. Row i contains the x,y,z coordinates of node i.
        edof : ndarray
            An E-by-L array. Element topology. (E is the number of elements and L is the number of dofs per element)
        dofs_per_nodes : int
            Integer. Dofs per node.
        el_type : int
            Integer. Element Type. See Gmsh manual for details. Usually 2 for triangles or 3 for quadrangles.
        axes : matplotlib.axes.Axes, optional
            Matplotlib Axes. The Axes where the model will be drawn. If unspecified the current Axes will be used, or a new Axes will be created if none exist.
        axes_adjust : bool, optional
            Boolean. True if the view should be changed to show the whole model. Default True.
        title : str, optional
            String. Changes title of the figure. Default "Mesh".
        color : tuple or str, optional
            3-tuple or char. Color of the wire. Defaults to black (0,0,0). Can also be given as a character in 'rgbycmkw'.
        face_color : tuple or str, optional
            3-tuple or char. Color of the faces. Defaults to white (1,1,1). Parameter filled must be True or faces will not be drawn at all.
        filled : bool, optional
            Boolean. Faces will be drawn if True. Otherwise only the wire is drawn. Default False.
