.. _calfem-vis-mpl-function-draw-node-circles:
.. index::
   single: draw_node_circles
   single: calfem.vis_mpl.draw_node_circles

calfem.vis_mpl.draw_node_circles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Purpose:

    Draws wire mesh of model in 2D or 3D. Returns the Mesh object that represents the mesh.

:Syntax:

.. code-block:: python

    cfv.draw_node_circles(ex, ey, title='', color=(0, 0, 0), face_color=(0.8, 0.8, 0.8), filled=False, marker_type='o')

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
        filled : bool, optional
            Faces will be drawn if True. Otherwise only the wire is drawn. Default False.
        marker_type : str, optional
            Marker type for drawing. Default "o".
