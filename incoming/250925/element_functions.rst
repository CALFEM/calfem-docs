*****************
Element functions
*****************

The group of element functions contains functions for computation of element
matrices and element forces for different element types. The element functions
have been divided into the following groups:

* Spring element
* Bar elements
* Heat flow elements
* Solid elements
* Beam elements
* Plate element

For each element type, there is a function for computation of the element stiffness matrix :math:`K^e`. For most of the elements, an element load vector :math:`f^e` can also be computed. These functions are identified by their last letter `-e`.

Using the function `assem()`, the element stiffness matrices and element load vectors are assembled into a global stiffness matrix :math:`K` and a load vector :math:`f`. Unknown nodal values of temperatures or displacements :math:`a` are computed by solving the system of equations :math:`Ka = f` using the function `solveq()`. A vector of nodal values of temperatures or displacements for a specific element is formed by the function `extract_ed()`.

When the element nodal values have been computed, the element flux or element stresses can be calculated using functions specific to the element type concerned. These functions are identified by their last letter `-s`.

For some elements, a function for computing the internal force vector is also available. These functions are identified by their last letter `-f`.

.. include:: spring_functions.rst
.. include:: bar_functions.rst
.. include:: heat_functions.rst
.. include:: solid_functions.rst
.. include:: beam_functions.rst
.. include:: plate_functions.rst
