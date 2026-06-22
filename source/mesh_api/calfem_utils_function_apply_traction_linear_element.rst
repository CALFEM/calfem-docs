.. _calfem-utils-function-apply-traction-linear-element:
.. index::
   single: apply_traction_linear_element
   single: calfem.utils.apply_traction_linear_element

calfem.utils.apply_traction_linear_element
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Purpose:

    Apply traction on part of boundary with marker.

:Syntax:

.. code-block:: python

    cfu.apply_traction_linear_element(boundaryElements, coords, dofs, F, marker, q)

:Description:

    Source docstring::

        Apply traction on part of boundary with marker.
        
        q is added to all boundaryDofs defined by marker. Applicable
        to 2D problems with 2 dofs per node. The function works with linear
        line elements. (elm-type 1 in GMSH).
        
        Parameters
        ----------
        boundaryElements : dict
            Dictionary with boundary elements, the key is a marker and the values are lists of elements.
        coords : array_like
            Coordinates matrix
        dofs : array_like
            Dofs matrix
        F : array_like
            force matrix.
        marker : int
            Boundary marker to assign boundary condition.
        q : array_like
            Value to assign boundary condition.
            shape = [qx qy] in global coordinates
