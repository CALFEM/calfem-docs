.. _material_functions:

Material functions
==================

The group of material functions comprises functions for constitutive models. The available models can treat linear elastic and isotropic hardening von Mises material. These material models are defined by the functions:

.. list-table:: Material property functions
    :widths: 20 120 
    :header-rows: 0

    * - hooke
      - Form linear elastic constitutive matrix
    * - mises
      - Compute stresses and plastic strains for isotropic hardening von Mises material 
    * - dmises
      - Form elasto-plastic continuum matrix for isotropic hardening von Mises material 
      
.. include:: hooke.rst
.. include:: mises.rst
.. include:: dmises.rst

