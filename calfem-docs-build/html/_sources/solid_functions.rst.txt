Solid elements functions
========================

Solid elements are available for two dimensional analysis in plane stress (panels) and plane strain, and for general three dimensional analysis. In the two dimensional case there are a triangular three node element, a quadrilateral four node element, two rectangular four node elements, and quadrilateral isoparametric four and eight node elements. For three dimensional analysis there is an eight node isoparametric element.

The elements are able to deal with both isotropic and anisotropic materials. The triangular element
and the three isoparametric elements can also be used together with a nonlinear material model.

The material properties are specified by supplying the constitutive matrix
:math:`\mathbf{D}` as an input variable to the element functions. This matrix can
be formed by the functions described in Section :ref:`material_functions`.

.. list-table:: **Solid elements**
    :widths: 50 50
    :header-rows: 0

    * - .. image:: images/PLANT.png
             :width: 70%

        .. centered:: ``plante``
      - .. image:: images/PLANQ.png
             :width: 70%

        .. centered:: ``planqe``
    * - .. image:: images/PLANTR.png
             :width: 70%
             
        .. centered:: ``planre``  
              ``plantce``
      - .. image:: images/PLANI4.png
             :width: 70%

        .. centered:: ``plani4e``
    * - .. image:: images/PLANI8.png
             :width: 70%

        .. centered:: ``plani8e``
      - .. image:: images/SOLI8.png
             :width: 70%

        .. centered:: ``soli8e``

2D Solid Functions
------------------

.. include:: plante.rst
.. include:: plants.rst
.. include:: plantf.rst
.. include:: planqe.rst
.. include:: planqs.rst
.. include:: planre.rst
.. include:: planrs.rst
.. include:: plantce.rst
.. include:: plantcs.rst
.. include:: plani4e.rst
.. include:: plani4s.rst
.. include:: plani4f.rst
.. include:: plani8e.rst
.. include:: plani8s.rst
.. include:: plani8f.rst

3D Solid Functions
------------------

.. include:: soli8e.rst
.. include:: soli8s.rst
.. include:: soli8f.rst
