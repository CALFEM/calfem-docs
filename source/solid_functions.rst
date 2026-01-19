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

    * - .. image:: images/plant.png
             :width: 70%

        .. centered:: ``plante``
      - .. image:: images/planq.png
             :width: 70%

        .. centered:: ``planqe``
    * - .. image:: images/plantr.png
             :width: 70%
             
        .. centered:: ``planre``  
              ``plantce``
      - .. image:: images/plani4.png
             :width: 70%

        .. centered:: ``plani4e``
    * - .. image:: images/plani8.png
             :width: 70%

        .. centered:: ``plani8e``
      - .. image:: images/soli8.png
             :width: 70%

        .. centered:: ``soli8e``


.. list-table:: 2D solid functions
    :widths: 20 120 
    :header-rows: 0

    * - plante
      - Compute element matrices for a triangular element 
    * - plants
      - Compute stresses and strains 
    * - plantf
      - Compute internal element forces 
    * - planqe
      - Compute element matrices for a quadrilateral element 
    * - planqs
      - Compute stresses and strains
    * - planre
      - Compute element matrices for a rectangular Melosh element 
    * - planrs
      - Compute stresses and strains
    * - plantce 
      - Compute element matrices for a rectangular Turner-Clough element 
    * - plantcs
      - Compute stresses and strains  
    * - plani4e
      - Compute element matrices, 4 node isoparametric element 
    * - plani4s
      - Compute stresses and strains 
    * - plani4f
      - Compute internal element forces 
    * - plani8e
      - Compute element matrices, 8 node isoparametric element 
    * - plani8s
      - Compute stresses and strains 
    * - plani8f
      - Compute internal element forces 


.. list-table:: 3D solid functions
    :widths: 20 120 
    :header-rows: 0
    
    * - soli8e
      - Compute element matrices, 8 node isoparametric element 
    * - soli8s
      - Compute stresses and strains 
    * - soli8f
      - Compute internal element forces 


.. 2D Solid Functions
.. ------------------

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

.. 3D Solid Functions
.. ------------------

.. include:: soli8e.rst
.. include:: soli8s.rst
.. include:: soli8f.rst
