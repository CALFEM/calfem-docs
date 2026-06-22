.. _calfem-vis-mpl-function-draw-geometry:
.. index::
   single: draw_geometry
   single: calfem.vis_mpl.draw_geometry

calfem.vis_mpl.draw_geometry
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Purpose:

    Draws the geometry (points and curves) in geoData.

:Syntax:

.. code-block:: python

    cfv.draw_geometry(geometry, draw_points=True, label_points=True, label_curves=True, title=None, font_size=11, N=20, rel_margin=0.05, draw_axis=False, axes=None)

:Description:

    Source docstring::

        Draws the geometry (points and curves) in geoData.
        
        Parameters
        ----------
        geometry : object
            GeoData object. Geodata contains geometric information of the model.
        draw_points : bool, optional
            If True points will be drawn. Default True.
        label_points : bool, optional
            If True Points will be labeled. The format is: ID[marker]. If a point has marker==0 only the ID is written. Default True.
        label_curves : bool, optional
            If True Curves will be labeled. The format is: ID(elementsOnCurve)[marker]. Default True.
        title : str, optional
            Title for the plot. Default None.
        font_size : int, optional
            Size of the text in the text labels. Default 11.
        N : int, optional
            The number of discrete points per curve segment. Default 20. Increase for smoother curves. Decrease for better performance.
        rel_margin : float, optional
            Extra spacing between geometry and axis. Default 0.05.
        draw_axis : bool, optional
            Whether to draw the axis frame. Default False.
        axes : matplotlib.axes.Axes, optional
            Matplotlib Axes. The Axes where the model will be drawn. If unspecified the current Axes will be used, or a new Axes will be created if none exist. Default None.
