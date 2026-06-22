.. _calfem-vis-mpl-function-draw-elements:
.. index::
   single: draw_elements
   single: calfem.vis_mpl.draw_elements

calfem.vis_mpl.draw_elements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Purpose:

    Draws wire mesh of model in 2D or 3D. Returns the Mesh object that represents the mesh.

:Syntax:

.. code-block:: python

    cfv.draw_elements(ex, ey, title='', color=(0, 0, 0), face_color=(0.8, 0.8, 0.8), node_color=(0, 0, 0), line_style='solid', filled=False, closed=True, show_nodes=False)

:Description:

    Source docstring::

        Draws wire mesh of model in 2D or 3D. Returns the Mesh object that represents
        the mesh.
        
        Parameters
        ----------
        ex : ndarray
            Element x-coordinates array.
        ey : ndarray
            Element y-coordinates array.
        title : str, optional
            Changes title of the figure. Default "".
        color : tuple or str, optional
            Color of the wire. Defaults to black (0,0,0). Can also be given as a character in 'rgbycmkw'.
        face_color : tuple or str, optional
            Color of the faces. Defaults to (0.8,0.8,0.8). Parameter filled must be True or faces will not be drawn at all.
        node_color : tuple or str, optional
            Color of the nodes. Defaults to black (0,0,0).
        line_style : str, optional
            Line style for drawing. Default "solid".
        filled : bool, optional
            Faces will be drawn if True. Otherwise only the wire is drawn. Default False.
        closed : bool, optional
            Whether elements should be drawn as closed polygons. Default True.
        show_nodes : bool, optional
            Whether to show nodes as markers. Default False.
