.. _calfem-mesh-function-trimesh2d:
.. index::
   single: trimesh2d
   single: calfem.mesh.trimesh2d

calfem.mesh.trimesh2d
^^^^^^^^^^^^^^^^^^^^^

:Purpose:

    Triangulates an area described by a number vertices (vertices) and a set of segments that describes a closed polygon.

:Syntax:

.. code-block:: python

    cfm.trimesh2d(vertices, segments=None, holes=None, maxArea=None, quality=True, dofs_per_node=1, logFilename='tri.log', triangleExecutablePath=None)

:Description:

    Source docstring::

        Triangulates an area described by a number vertices (vertices) and a set
        of segments that describes a closed polygon.
        
        Parameters:
        
            vertices            array [nVertices x 2] with vertices describing the geometry.
        
                                [[v0_x, v0_y],
                                 [   ...    ],
                                 [vn_x, vn_y]]
        
            segments            array [nSegments x 3] with segments describing the geometry.
        
                                [[s0_v0, s0_v1,marker],
                                 [        ...        ],
                                 [sn_v0, sn_v1,marker]]
        
            holes               [Not currently used]
        
            maxArea             Maximum area for triangle. (None)
        
            quality             If true, triangles are prevented having angles < 30 degrees. (True)
        
            dofs_per_node         Number of degrees of freedom per node.
        
            logFilename         Filename for triangle output ("tri.log")
        
        Returns:
        
            coords              Node coordinates
        
                                [[n0_x, n0_y],
                                 [   ...    ],
                                 [nn_x, nn_y]]
        
            edof                Element topology
        
                                [[el0_dof1, ..., el0_dofn],
                                 [          ...          ],
                                 [eln_dof1, ..., eln_dofn]]
        
            dofs                Node dofs
        
                                [[n0_dof1, ..., n0_dofn],
                                 [         ...         ],
                                 [nn_dof1, ..., nn_dofn]]
        
            bdofs               Boundary dofs. Dictionary containing lists of dofs for
                                each boundary marker. Dictionary key = marker id.
