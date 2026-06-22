.. _calfem-vis-mpl-function-draw-ordered-polys:
.. index::
   single: draw_ordered_polys
   single: calfem.vis_mpl.draw_ordered_polys

calfem.vis_mpl.draw_ordered_polys
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Purpose:

    Draw ordered polygons on the current matplotlib axes.

:Syntax:

.. code-block:: python

    cfv.draw_ordered_polys(o_polys)

:Description:

    Source docstring::

        Draw ordered polygons on the current matplotlib axes.
        
        This function takes a collection of ordered polygons and renders them as patches
        on the current matplotlib axes. Each polygon is drawn with an orange face color
        and a line width of 1.
        
        Parameters
        ----------
        o_polys : array-like
            A collection of polygons where each polygon is represented as a numpy array
            with shape (n_vertices, 2) or (n_vertices, 3+). Only the first two columns
            (x, y coordinates) are used for drawing.
        
        Notes
        -----
        - The function uses the current matplotlib axes (plt.gca())
        - All polygons are drawn with orange face color and line width of 1
        - Only the first two columns of each polygon array are used for coordinates
        - The function requires matplotlib.pyplot, matplotlib.path, and matplotlib.patches
          to be imported as plt, mpp, and patches respectively
        
        Examples
        --------
        >>> import numpy as np
        >>> import matplotlib.pyplot as plt
        >>> # Create a simple triangle
        >>> triangle = np.array([[0, 0], [1, 0], [0.5, 1], [0, 0]])
        >>> draw_ordered_polys([triangle])
        >>> plt.show()
