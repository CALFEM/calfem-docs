.. _calfem-mesh-function-create-mesh:
.. index::
   single: create_mesh
   single: calfem.mesh.create_mesh

calfem.mesh.create_mesh
^^^^^^^^^^^^^^^^^^^^^^^

:Purpose:

    Create a mesh for the given geometry using GMSH. This function serves as a convenient wrapper around the GmshMeshGenerator class to generate finite element meshes from geometric definitions.

:Syntax:

.. code-block:: python

    cfm.create_mesh(geometry, el_type=2, el_size_factor=1, dofs_per_node=1, gmsh_exec_path=None, clcurv=False, min_size=None, max_size=None, meshing_algorithm=None, additional_options='')

:Description:

    Source docstring::

        Create a mesh for the given geometry using GMSH.
        This function serves as a convenient wrapper around the GmshMeshGenerator class
        to generate finite element meshes from geometric definitions.
        Parameters
        ----------
        geometry : object
            The geometry object defining the domain to be meshed.
        el_type : int, optional
            Element type identifier. Default is 2.
        el_size_factor : float, optional
            Factor controlling the element size. Default is 1.
        dofs_per_node : int, optional
            Number of degrees of freedom per node. Default is 1.
        gmsh_exec_path : str, optional
            Path to the GMSH executable. If None, uses system default. Default is None.
        clcurv : bool, optional
            Enable/disable curved element generation. Default is False.
        min_size : float, optional
            Minimum element size constraint. Default is None.
        max_size : float, optional
            Maximum element size constraint. Default is None.
        meshing_algorithm : int, optional
            GMSH meshing algorithm identifier. Default is None.
        additional_options : str, optional
            Additional GMSH options as a string. Default is ''.
        Returns
        -------
        mesh : object
            The generated mesh object containing nodes, elements, and connectivity information.
        Examples
        --------
        >>> mesh = create_mesh(geometry, el_type=3, el_size_factor=0.5)
        >>> mesh = create_mesh(geometry, min_size=0.1, max_size=1.0)
