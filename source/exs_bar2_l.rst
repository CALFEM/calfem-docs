exs_bar2_l
^^^^^^^^^^

.. index:: exs_bar2_l

:Purpose:

    Analysis of a plane truss.

:Description:

    Consider a plane truss, loaded by a single force :math:`P=0.5` MN.

    .. only:: html
        
        .. figure:: images/exs4_1.svg
            :align: center
            :width: 500px
    
    .. only:: latex
        
        .. figure:: images/exs4_1.svg
            :align: center
            :width: 70%

    The corresponding finite element model consists of ten elements and twelve degrees of freedom.

    .. only:: html
        
        .. figure:: images/exs4_2.svg
            :align: center
            :width: 500px
    
    .. only:: latex
        
        .. figure:: images/exs4_2.svg
            :align: center
            :width: 70%

    **Material properties:**
    
    - Cross-sectional area: :math:`A=25.0 \times 10^{-4}` m²
    - Young's modulus: :math:`E=2.10 \times 10^{5}` MPa

:Example:

    The computation is initialized by importing CALFEM and NumPy. The element topology matrix contains only the degrees of freedom for each element:

    .. code-block:: python

        import numpy as np
        import calfem.core as cfc
        import calfem.utils as cfu

        edof = np.array([
            [1, 2, 5, 6],
            [3, 4, 7, 8],
            [5, 6, 9, 10],
            [7, 8, 11, 12],
            [7, 8, 5, 6],
            [11, 12, 9, 10],
            [3, 4, 5, 6],
            [7, 8, 9, 10],
            [1, 2, 7, 8],
            [5, 6, 11, 12],
        ])

    The global stiffness matrix :code:`K` and load vector :code:`f` are initialized. The load :math:`P=0.5` MN is divided into x and y components:

    .. code-block:: python

        K = np.zeros([12, 12])
        f = np.zeros([12, 1])
        f[10] = 0.5e6 * np.sin(np.pi / 6)
        f[11] = -0.5e6 * np.cos(np.pi / 6)

    The material and geometric properties are defined, along with element coordinate matrices:

    .. code-block:: python

        A = 25.0e-4
        E = 2.1e11
        ep = [E, A]

        ex = np.array([
            [0.0, 2.0],
            [0.0, 2.0],
            [2.0, 4.0],
            [2.0, 4.0],
            [2.0, 2.0],
            [4.0, 4.0],
            [0.0, 2.0],
            [2.0, 4.0],
            [0.0, 2.0],
            [2.0, 4.0],
        ])

        ey = np.array([
            [2.0, 2.0],
            [0.0, 0.0],
            [2.0, 2.0],
            [0.0, 0.0],
            [0.0, 2.0],
            [0.0, 2.0],
            [0.0, 2.0],
            [0.0, 2.0],
            [2.0, 0.0],
            [2.0, 0.0],
        ])

    The element stiffness matrices are computed and assembled in a loop:

    .. code-block:: python

        for elx, ely, eltopo in zip(ex, ey, edof):
            Ke = cfc.bar2e(elx, ely, ep)
            cfc.assem(eltopo, K, Ke)


    The system of equations is solved by specifying boundary conditions and using :func:`solveq`:

    .. tabs::

        .. tab:: Code

            .. code:: python

                bc_dofs = np.array([1, 2, 3, 4])
                bc_vals = np.array([0.0, 0.0, 0.0, 0.0])
                a, r = cfc.solveq(K, f, bc_dofs, bc_vals)

                cfu.disp_h2("Displacements a:")
                cfu.disp_array(a, tablefmt='plain')

                cfu.disp_h2("Reaction forces r:")
                cfu.disp_array(r, tablefmt='plain')

        .. tab:: Output

            .. code:: 

                ## Displacements a:

                 0.0000e+00
                 0.0000e+00
                 0.0000e+00
                 0.0000e+00
                 2.3845e-03
                -4.4633e-03
                -1.6118e-03
                -4.1987e-03
                 3.0346e-03
                -1.0684e-02
                -1.6589e-03
                -1.1334e-02

                ## Reaction forces r:

                -8.6603e+05
                 2.4009e+05
                 6.1603e+05
                 1.9293e+05
                 0.0000e+00
                -1.4552e-10
                -1.1642e-10
                 5.8208e-11
                -1.1642e-10
                 2.3283e-10
                 2.9104e-11
                 2.9104e-10                
        

    The displacement at the point of loading is :math:`-1.7 \times 10^{-3}` m in the x-direction and :math:`-11.3 \times 10^{-3}` m in the y-direction. At the upper support the horizontal force is :math:`-0.866` MN and the vertical :math:`0.240` MN. At the lower support the forces are :math:`0.616` MN and :math:`0.193` MN, respectively.

    Normal forces are evaluated from element displacements. These are obtained from the global displacements using :func:`extract_ed` and the forces are calculated using :func:`bar2s`:

    .. tabs::

        .. tab:: Code

            .. code-block:: python

                ed = cfc.extract_ed(edof, a)
                N = np.zeros([edof.shape[0]])

                cfu.disp_h2("Element forces:")

                i = 0
                for elx, ely, eld in zip(ex, ey, ed):
                    es = cfc.bar2s(elx, ely, ep, eld)
                    N[i] = es[0][0]
                    print("N%d = %g" % (i + 1, N[i]))
                    i += 1

        .. tab:: Output

            .. code:: 

                ## Element forces:

                N1 = 625938
                N2 = -423100
                N3 = 170640
                N4 = -12372.8
                N5 = -69447
                N6 = 170640
                N7 = -272838
                N8 = -241321
                N9 = 339534
                N10 = 371051                

    The largest normal force :math:`N=0.626` MN is obtained in element 1 and is equivalent to a normal stress :math:`\sigma=250` MPa.

    To reduce the quantity of input data, the element coordinate matrices :code:`ex` and :code:`ey` can alternatively be created from a global coordinate matrix :code:`coord` and a global topology matrix :code:`dof` using :func:`coord_extract`:

    .. code-block:: python

        coord = np.array([
            [0, 2], 
            [0, 0], 
            [2, 2], 
            [2, 0], 
            [4, 2], 
            [4, 0]
        ])

        dof = np.array([
            [1, 2], 
            [3, 4], 
            [5, 6], 
            [7, 8], 
            [9, 10], 
            [11, 12]
        ])

        ex, ey = cfc.coord_extract(edof, coord, dof, 2)