exs_beambar2
^^^^^^^^^^^^

.. index:: exs_beambar2

:Purpose:

    Analysis of a combined beam and bar structure.

:Description:

    Consider a structure consisting of a beam with :math:`A_1=4.0 \times 10^{-3}` m² and :math:`I_1=5.4 \times 10^{-5}` m⁴ supported by two bars with :math:`A_2=1.0 \times 10^{-3}` m². The beam as well as the bars have :math:`E=200` GPa. The structure is loaded by a distributed load :math:`q=10` kN/m. The corresponding finite element model consists of three beam elements and two bar elements and has 14 degrees of freedom.

    .. only:: html
        
        .. figure:: images/exs7_1.svg
            :align: center
            :width: 600px
    
    .. only:: latex
        
        .. figure:: images/exs7_1.svg
            :align: center
            :width: 70%

    .. only:: html
        
        .. figure:: images/exs7_2.svg
            :align: center
            :width: 600px
    
    .. only:: latex
        
        .. figure:: images/exs7_2.svg
            :align: center
            :width: 70%

:Example:

    The computation is initialized by importing CALFEM and NumPy. The topology matrices are defined separately for beam and bar elements, containing only the degrees of freedom:

    .. code-block:: python

        import numpy as np
        import calfem.core as cfc
        import calfem.utils as cfu
        import calfem.vis_mpl as cfv
        edof1 = np.array([
            [1,  2,  3,  4,  5,  6],
            [4,  5,  6,  7,  8,  9],
            [7,  8,  9, 10, 11, 12]    
        ])

        edof2 = np.array([
            [13, 14,  4,  5],
            [13, 14,  7,  8]    
        ])

        K = np.array(np.zeros((14, 14)))
        f = np.array(np.zeros((14, 1)))

    The material and geometric properties are defined for beam and bar elements:

    .. code-block:: python

        E = 200.e9
        A1 = 4.e-3
        I1 = 5.4e-5
        A2 = 1.e-3

        ep1 = [E, A1, I1]
        ep4 = [E, A2]

        eq1 = [0, 0]
        eq2 = [0, -10e+3]

        ex1 = np.array([0, 2])
        ex2 = np.array([2, 4])
        ex3 = np.array([4, 6])
        ex4 = np.array([0, 2])
        ex5 = np.array([0, 4])
        ey1 = np.array([2, 2])
        ey2 = np.array([2, 2])
        ey3 = np.array([2, 2])
        ey4 = np.array([0, 2])
        ey5 = np.array([0, 2])

    The element stiffness matrices are computed using :func:`beam2e` for beam elements and :func:`bar2e` for bar elements. Element load vectors from distributed loads are also computed:

    .. code-block:: python

        Ke1 = cfc.beam2e(ex1, ey1, ep1)
        Ke2, fe2 = cfc.beam2e(ex2, ey2, ep1, eq2)
        Ke3, fe3 = cfc.beam2e(ex3, ey3, ep1, eq2)

        Ke4 = cfc.bar2e(ex4, ey4, ep4)
        Ke5 = cfc.bar2e(ex5, ey5, ep4)

    The global stiffness matrix and load vector are assembled using :func:`assem`:

    .. code-block:: python

        K = cfc.assem(edof1[0, :], K, Ke1)
        K, f = cfc.assem(edof1[1, :], K, Ke2, f, fe2)
        K, f = cfc.assem(edof1[2, :], K, Ke3, f, fe3)
        K = cfc.assem(edof2[0, :], K, Ke4)
        K = cfc.assem(edof2[1, :], K, Ke5)

    The system of equations is solved by specifying boundary conditions and using :func:`solveq`. The vertical displacement at the end of the beam is 13.0 mm:

    .. tabs::

        .. tab:: Code

            .. code-block:: python

                bc_dofs = np.array([1, 2, 3, 13, 14])
                bc_vals = np.array([0.0, 0.0, 0.0, 0.0, 0.0])

                a, r = cfc.solveq(K, f, bc_dofs, bc_vals)
                cfu.disp_h2("Displacements a:")
                cfu.disp_array(a)

                cfu.disp_h2("Reaction forces r:")
                cfu.disp_array(r)

        .. tab:: Output

            .. code::

                ## Displacements a:

                +-------------+
                |  0.0000e+00 |
                |  0.0000e+00 |
                |  0.0000e+00 |
                |  2.0175e-04 |
                | -5.5551e-04 |
                | -9.6319e-04 |
                |  3.7224e-04 |
                | -4.5567e-03 |
                | -3.2909e-03 |
                |  3.7224e-04 |
                | -1.2990e-02 |
                | -4.5254e-03 |
                |  0.0000e+00 |
                |  0.0000e+00 |
                +-------------+

                ## Reaction forces r:

                +-------------+
                | -8.0702e+04 |
                | -6.6044e+03 |
                | -1.4032e+03 |
                |  0.0000e+00 |
                |  1.4552e-11 |
                |  5.0022e-12 |
                |  0.0000e+00 |
                |  0.0000e+00 |
                |  2.1828e-11 |
                |  0.0000e+00 |
                | -2.9104e-11 |
                |  3.8654e-11 |
                |  8.0702e+04 |
                |  4.6604e+04 |
                +-------------+                
        
    Maximum vertical displacement: 0.009 m = 9.5 mm

    The section forces are calculated using :func:`beam2s` and :func:`bar2s` from element displacements. This yields normal forces of -35.4 kN and -152.5 kN in the bars and maximum moment of 20.0 kNm in the beam:

    .. tabs::

        .. tab:: Code

            .. code-block:: python

                ed1 = cfc.extract_ed(edof1, a)
                ed2 = cfc.extract_ed(edof2, a)

                es1, _, _ = cfc.beam2s(ex1, ey1, ep1, ed1[0, :], eq1, nep=11)
                es2, _, _ = cfc.beam2s(ex2, ey2, ep1, ed1[1, :], eq2, nep=11)
                es3, _, _ = cfc.beam2s(ex3, ey3, ep1, ed1[2, :], eq2, nep=11)
                es4 = cfc.bar2s(ex4, ey4, ep4, ed2[0, :])
                es5 = cfc.bar2s(ex5, ey5, ep4, ed2[1, :])

                cfu.disp_h2("es1 = ")
                cfu.disp_array(es1, headers=["N", "Q", "M"])
                cfu.disp_h2("es2 = ")
                cfu.disp_array(es2, headers=["N", "Q", "M"])
                cfu.disp_h2("es3 = ")
                cfu.disp_array(es3, headers=["N", "Q", "M"])
                cfu.disp_h2("es4 = ")
                cfu.disp_array(es4, headers=["N"])
                cfu.disp_h2("es5 = ")
                cfu.disp_array(es5, headers=["N"])   

        .. tab:: Output

            .. code::

                ## es1 =

                +------------+------------+-------------+
                |          N |          Q |           M |
                |------------+------------+-------------|
                | 8.0702e+04 | 6.6044e+03 |  1.4032e+03 |
                | 8.0702e+04 | 6.6044e+03 |  8.2292e+01 |
                | 8.0702e+04 | 6.6044e+03 | -1.2386e+03 |
                | 8.0702e+04 | 6.6044e+03 | -2.5595e+03 |
                | 8.0702e+04 | 6.6044e+03 | -3.8803e+03 |
                | 8.0702e+04 | 6.6044e+03 | -5.2012e+03 |
                | 8.0702e+04 | 6.6044e+03 | -6.5221e+03 |
                | 8.0702e+04 | 6.6044e+03 | -7.8430e+03 |
                | 8.0702e+04 | 6.6044e+03 | -9.1639e+03 |
                | 8.0702e+04 | 6.6044e+03 | -1.0485e+04 |
                | 8.0702e+04 | 6.6044e+03 | -1.1806e+04 |
                +------------+------------+-------------+

                ## es2 =

                +------------+-------------+-------------+
                |          N |           Q |           M |
                |------------+-------------+-------------|
                | 6.8194e+04 | -5.9028e+03 | -1.1806e+04 |
                | 6.8194e+04 | -3.9028e+03 | -1.0825e+04 |
                | 6.8194e+04 | -1.9028e+03 | -1.0245e+04 |
                | 6.8194e+04 |  9.7186e+01 | -1.0064e+04 |
                | 6.8194e+04 |  2.0972e+03 | -1.0283e+04 |
                | 6.8194e+04 |  4.0972e+03 | -1.0903e+04 |
                | 6.8194e+04 |  6.0972e+03 | -1.1922e+04 |
                | 6.8194e+04 |  8.0972e+03 | -1.3342e+04 |
                | 6.8194e+04 |  1.0097e+04 | -1.5161e+04 |
                | 6.8194e+04 |  1.2097e+04 | -1.7381e+04 |
                | 6.8194e+04 |  1.4097e+04 | -2.0000e+04 |
                +------------+-------------+-------------+

                ## es3 =

                +------------+-------------+-------------+
                |          N |           Q |           M |
                |------------+-------------+-------------|
                | 2.1684e-11 | -2.0000e+04 | -2.0000e+04 |
                | 2.1684e-11 | -1.8000e+04 | -1.6200e+04 |
                | 2.1684e-11 | -1.6000e+04 | -1.2800e+04 |
                | 2.1684e-11 | -1.4000e+04 | -9.8000e+03 |
                | 2.1684e-11 | -1.2000e+04 | -7.2000e+03 |
                | 2.1684e-11 | -1.0000e+04 | -5.0000e+03 |
                | 2.1684e-11 | -8.0000e+03 | -3.2000e+03 |
                | 2.1684e-11 | -6.0000e+03 | -1.8000e+03 |
                | 2.1684e-11 | -4.0000e+03 | -8.0000e+02 |
                | 2.1684e-11 | -2.0000e+03 | -2.0000e+02 |
                | 2.1684e-11 |  9.3675e-12 | -7.6111e-12 |
                +------------+-------------+-------------+

                ## es4 =

                +-------------+
                |           N |
                |-------------|
                | -1.7688e+04 |
                | -1.7688e+04 |
                +-------------+

                ## es5 =

                +-------------+
                |           N |
                |-------------|
                | -7.6244e+04 |
                | -7.6244e+04 |
                +-------------+                
