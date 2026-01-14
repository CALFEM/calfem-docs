exs_beam2
^^^^^^^^^

.. index:: exs_beam2

:Purpose:

    Analysis of a plane frame.

:Description:

    A frame consists of one horizontal and two vertical beams according to the figure.

    .. only:: html
        
        .. figure:: images/exs6_1.svg
            :align: center
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/exs6_1.svg
            :align: center
            :width: 70%

    **Material and geometric properties:**

    .. list-table::
       :widths: 20 10 30
       :header-rows: 0

       * - :math:`E`
         - :math:`=`
         - :math:`200` GPa
       * - :math:`A_1`
         - :math:`=`
         - :math:`2.0 \times 10^{-3}` m²
       * - :math:`I_1`
         - :math:`=`
         - :math:`1.6 \times 10^{-5}` m⁴
       * - :math:`A_2`
         - :math:`=`
         - :math:`6.0 \times 10^{-3}` m²
       * - :math:`I_2`
         - :math:`=`
         - :math:`5.4 \times 10^{-5}` m⁴
       * - :math:`P`
         - :math:`=`
         - :math:`2.0` kN
       * - :math:`q_0`
         - :math:`=`
         - :math:`10.0` kN/m

    The corresponding finite element model consists of three beam elements and twelve degrees of freedom.

    .. only:: html
        
        .. figure:: images/exs6_2.svg
            :align: center
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/exs6_2.svg
            :align: center
            :width: 70%

:Example:

    The computation is initialized by importing CALFEM and NumPy. The element topology matrix contains only the degrees of freedom for each element:

    .. code-block:: python

        import numpy as np
        import calfem.core as cfc
        import calfem.utils as cfu
        import calfem.vis_mpl as cfv

        edof = np.array([
            [4, 5, 6, 1, 2, 3], 
            [7, 8, 9, 10, 11, 12], 
            [4, 5, 6, 7, 8, 9]
        ])        

    The global stiffness matrix :code:`K` and load vector :code:`f` are initialized. The point load P = 2000 N is applied at DOF 4:

    .. tabs::

        .. tab:: Code

            .. code-block:: python

                K = np.array(np.zeros((12, 12)))
                f = np.array(np.zeros((12, 1)))
                f[3] = 2.0e3

        .. tab:: Output

            .. code:: 

                # Load vector f

                +------------+
                |          f |
                |------------|
                | 0.0000e+00 |
                | 0.0000e+00 |
                | 0.0000e+00 |
                | 2.0000e+03 |
                | 0.0000e+00 |
                | 0.0000e+00 |
                | 0.0000e+00 |
                | 0.0000e+00 |
                | 0.0000e+00 |
                | 0.0000e+00 |
                | 0.0000e+00 |
                | 0.0000e+00 |
                +------------+                

    The material and geometric properties are defined for each element type:

    .. code-block:: python

        E = 200.0e9
        A1 = 2.0e-3
        A2 = 6.0e-3
        I1 = 1.6e-5
        I2 = 5.4e-5

        ep1 = [E, A1, I1]
        ep3 = [E, A2, I2]

        ex1 = np.array([0, 0])
        ex2 = np.array([6, 6])
        ex3 = np.array([0, 6])

        ey1 = np.array([4, 0])
        ey2 = np.array([4, 0])
        ey3 = np.array([4, 4])

        eq1 = np.array([0, 0])
        eq2 = np.array([0, 0])
        eq3 = np.array([0, -10e3])

    The element stiffness matrices and load vectors are computed and assembled:

    .. code-block:: python

        Ke1 = cfc.beam2e(ex1, ey1, ep1)
        Ke2 = cfc.beam2e(ex2, ey2, ep1)
        Ke3, fe3 = cfc.beam2e(ex3, ey3, ep3, eq3)   

        K = cfc.assem(edof[0, :], K, Ke1)
        K = cfc.assem(edof[1, :], K, Ke2)
        K, f = cfc.assem(edof[2, :], K, Ke3, f, fe3)

    The system of equations is solved by specifying boundary conditions and using :func:`solveq`:

    .. tabs::

        .. tab:: Code

            .. code-block:: python

                bc_dofs = np.array([1, 2, 3, 10, 11])
                bc_vals = np.array([0.0, 0.0, 0.0, 0.0, 0.0])

                a, r = cfc.solveq(K, f, bc_dofs, bc_vals)

                cfu.disp_array(a, ["a"])
                cfu.disp_array(r, ["r"])

        .. tab:: Output

            .. code::

                +-------------+
                |           a |
                |-------------|
                |  0.0000e+00 |
                |  0.0000e+00 |
                |  0.0000e+00 |
                |  7.5357e-03 |
                | -2.8741e-04 |
                | -5.3735e-03 |
                |  7.5161e-03 |
                | -3.1259e-04 |
                |  4.6656e-03 |
                |  0.0000e+00 |
                |  0.0000e+00 |
                | -5.1513e-03 |
                +-------------+
                +-------------+
                |           r |
                |-------------|
                |  1.9268e+03 |
                |  2.8741e+04 |
                |  4.4527e+02 |
                |  0.0000e+00 |
                |  3.6380e-12 |
                | -7.2760e-12 |
                | -2.3283e-10 |
                |  3.6380e-12 |
                |  0.0000e+00 |
                | -3.9268e+03 |
                |  3.1259e+04 |
                |  0.0000e+00 |
                +-------------+                

        


    The element displacements are extracted and section forces are computed along each element:

    .. tabs::

        .. tab:: Code

            .. code-block:: python

                ed = cfc.extract_ed(edof, a)

                es1, edi1, ec1 = cfc.beam2s(ex1, ey1, ep1, ed[0, :], eq1, nep=21)
                es2, edi2, ec2 = cfc.beam2s(ex2, ey2, ep1, ed[1, :], eq2, nep=21)
                es3, edi3, ec3 = cfc.beam2s(ex3, ey3, ep3, ed[2, :], eq3, nep=21)

                cfu.disp_h2("es1")
                cfu.disp_array(es1, ["N", "Vy", "Mz"])
                cfu.disp_h2("edi1")
                cfu.disp_array(edi1, ["u1", "v1"])
                cfu.disp_h2("es2")
                cfu.disp_array(es2, ["N", "Vy", "Mz"])
                cfu.disp_h2("edi2")
                cfu.disp_array(edi2, ["u1", "v1"])
                cfu.disp_h2("es3")
                cfu.disp_array(es3, ["N", "Vy", "Mz"])
                cfu.disp_h2("edi3")
                cfu.disp_array(edi3, ["u1", "v1"])

        .. tab:: Output

            .. code::

                ## es1

                +-------------+------------+------------+
                |           N |         Vy |         Mz |
                |-------------+------------+------------|
                | -2.8741e+04 | 1.9268e+03 | 8.1523e+03 |
                | -2.8741e+04 | 1.9268e+03 | 7.7670e+03 |
                | -2.8741e+04 | 1.9268e+03 | 7.3816e+03 |
                | -2.8741e+04 | 1.9268e+03 | 6.9963e+03 |
                | -2.8741e+04 | 1.9268e+03 | 6.6109e+03 |
                | -2.8741e+04 | 1.9268e+03 | 6.2256e+03 |
                | -2.8741e+04 | 1.9268e+03 | 5.8402e+03 |
                | -2.8741e+04 | 1.9268e+03 | 5.4548e+03 |
                | -2.8741e+04 | 1.9268e+03 | 5.0695e+03 |
                | -2.8741e+04 | 1.9268e+03 | 4.6841e+03 |
                | -2.8741e+04 | 1.9268e+03 | 4.2988e+03 |
                | -2.8741e+04 | 1.9268e+03 | 3.9134e+03 |
                | -2.8741e+04 | 1.9268e+03 | 3.5281e+03 |
                | -2.8741e+04 | 1.9268e+03 | 3.1427e+03 |
                | -2.8741e+04 | 1.9268e+03 | 2.7574e+03 |
                | -2.8741e+04 | 1.9268e+03 | 2.3720e+03 |
                | -2.8741e+04 | 1.9268e+03 | 1.9867e+03 |
                | -2.8741e+04 | 1.9268e+03 | 1.6013e+03 |
                | -2.8741e+04 | 1.9268e+03 | 1.2160e+03 |
                | -2.8741e+04 | 1.9268e+03 | 8.3062e+02 |
                | -2.8741e+04 | 1.9268e+03 | 4.4527e+02 |
                +-------------+------------+------------+

                ## edi1

                +------------+------------+
                |         u1 |         v1 |
                |------------+------------|
                | 2.8741e-04 | 7.5357e-03 |
                | 2.7304e-04 | 6.5112e-03 |
                | 2.5867e-04 | 5.5837e-03 |
                | 2.4430e-04 | 4.7485e-03 |
                | 2.2993e-04 | 4.0008e-03 |
                | 2.1556e-04 | 3.3357e-03 |
                | 2.0119e-04 | 2.7484e-03 |
                | 1.8682e-04 | 2.2341e-03 |
                | 1.7245e-04 | 1.7880e-03 |
                | 1.5807e-04 | 1.4053e-03 |
                | 1.4370e-04 | 1.0811e-03 |
                | 1.2933e-04 | 8.1067e-04 |
                | 1.1496e-04 | 5.8915e-04 |
                | 1.0059e-04 | 4.1173e-04 |
                | 8.6223e-05 | 2.7359e-04 |
                | 7.1852e-05 | 1.6993e-04 |
                | 5.7482e-05 | 9.5907e-05 |
                | 4.3111e-05 | 4.6722e-05 |
                | 2.8741e-05 | 1.7554e-05 |
                | 1.4370e-05 | 3.5858e-06 |
                | 0.0000e+00 | 1.7347e-18 |
                +------------+------------+

                ## es2

                +-------------+-------------+-------------+
                |           N |          Vy |          Mz |
                |-------------+-------------+-------------|
                | -3.1259e+04 | -3.9268e+03 | -1.5707e+04 |
                | -3.1259e+04 | -3.9268e+03 | -1.4922e+04 |
                | -3.1259e+04 | -3.9268e+03 | -1.4136e+04 |
                | -3.1259e+04 | -3.9268e+03 | -1.3351e+04 |
                | -3.1259e+04 | -3.9268e+03 | -1.2566e+04 |
                | -3.1259e+04 | -3.9268e+03 | -1.1780e+04 |
                | -3.1259e+04 | -3.9268e+03 | -1.0995e+04 |
                | -3.1259e+04 | -3.9268e+03 | -1.0210e+04 |
                | -3.1259e+04 | -3.9268e+03 | -9.4242e+03 |
                | -3.1259e+04 | -3.9268e+03 | -8.6389e+03 |
                | -3.1259e+04 | -3.9268e+03 | -7.8535e+03 |
                | -3.1259e+04 | -3.9268e+03 | -7.0682e+03 |
                | -3.1259e+04 | -3.9268e+03 | -6.2828e+03 |
                | -3.1259e+04 | -3.9268e+03 | -5.4975e+03 |
                | -3.1259e+04 | -3.9268e+03 | -4.7121e+03 |
                | -3.1259e+04 | -3.9268e+03 | -3.9268e+03 |
                | -3.1259e+04 | -3.9268e+03 | -3.1414e+03 |
                | -3.1259e+04 | -3.9268e+03 | -2.3561e+03 |
                | -3.1259e+04 | -3.9268e+03 | -1.5707e+03 |
                | -3.1259e+04 | -3.9268e+03 | -7.8535e+02 |
                | -3.1259e+04 | -3.9268e+03 |  5.5511e-12 |
                +-------------+-------------+-------------+

                ## edi2

                +------------+------------+
                |         u1 |         v1 |
                |------------+------------|
                | 3.1259e-04 | 7.5161e-03 |
                | 2.9696e-04 | 8.3527e-03 |
                | 2.8133e-04 | 9.0027e-03 |
                | 2.6570e-04 | 9.4761e-03 |
                | 2.5007e-04 | 9.7825e-03 |
                | 2.3444e-04 | 9.9319e-03 |
                | 2.1881e-04 | 9.9341e-03 |
                | 2.0318e-04 | 9.7988e-03 |
                | 1.8755e-04 | 9.5359e-03 |
                | 1.7193e-04 | 9.1552e-03 |
                | 1.5630e-04 | 8.6665e-03 |
                | 1.4067e-04 | 8.0796e-03 |
                | 1.2504e-04 | 7.4044e-03 |
                | 1.0941e-04 | 6.6506e-03 |
                | 9.3777e-05 | 5.8282e-03 |
                | 7.8148e-05 | 4.9468e-03 |
                | 6.2518e-05 | 4.0163e-03 |
                | 4.6889e-05 | 3.0466e-03 |
                | 3.1259e-05 | 2.0474e-03 |
                | 1.5630e-05 | 1.0286e-03 |
                | 0.0000e+00 | 3.4694e-18 |
                +------------+------------+

                ## es3

                +-------------+-------------+-------------+
                |           N |          Vy |          Mz |
                |-------------+-------------+-------------|
                | -3.9268e+03 | -2.8741e+04 | -8.1523e+03 |
                | -3.9268e+03 | -2.5741e+04 |  1.9953e+01 |
                | -3.9268e+03 | -2.2741e+04 |  7.2922e+03 |
                | -3.9268e+03 | -1.9741e+04 |  1.3664e+04 |
                | -3.9268e+03 | -1.6741e+04 |  1.9137e+04 |
                | -3.9268e+03 | -1.3741e+04 |  2.3709e+04 |
                | -3.9268e+03 | -1.0741e+04 |  2.7381e+04 |
                | -3.9268e+03 | -7.7409e+03 |  3.0154e+04 |
                | -3.9268e+03 | -4.7409e+03 |  3.2026e+04 |
                | -3.9268e+03 | -1.7409e+03 |  3.2998e+04 |
                | -3.9268e+03 |  1.2591e+03 |  3.3070e+04 |
                | -3.9268e+03 |  4.2591e+03 |  3.2243e+04 |
                | -3.9268e+03 |  7.2591e+03 |  3.0515e+04 |
                | -3.9268e+03 |  1.0259e+04 |  2.7887e+04 |
                | -3.9268e+03 |  1.3259e+04 |  2.4359e+04 |
                | -3.9268e+03 |  1.6259e+04 |  1.9932e+04 |
                | -3.9268e+03 |  1.9259e+04 |  1.4604e+04 |
                | -3.9268e+03 |  2.2259e+04 |  8.3762e+03 |
                | -3.9268e+03 |  2.5259e+04 |  1.2484e+03 |
                | -3.9268e+03 |  2.8259e+04 | -6.7793e+03 |
                | -3.9268e+03 |  3.1259e+04 | -1.5707e+04 |
                +-------------+-------------+-------------+

                ## edi3

                +------------+-------------+
                |         u1 |          v1 |
                |------------+-------------|
                | 7.5357e-03 | -2.8741e-04 |
                | 7.5347e-03 | -1.9218e-03 |
                | 7.5337e-03 | -3.5566e-03 |
                | 7.5328e-03 | -5.1312e-03 |
                | 7.5318e-03 | -6.5927e-03 |
                | 7.5308e-03 | -7.8952e-03 |
                | 7.5298e-03 | -9.0009e-03 |
                | 7.5288e-03 | -9.8789e-03 |
                | 7.5279e-03 | -1.0506e-02 |
                | 7.5269e-03 | -1.0868e-02 |
                | 7.5259e-03 | -1.0954e-02 |
                | 7.5249e-03 | -1.0766e-02 |
                | 7.5239e-03 | -1.0310e-02 |
                | 7.5229e-03 | -9.6000e-03 |
                | 7.5220e-03 | -8.6584e-03 |
                | 7.5210e-03 | -7.5143e-03 |
                | 7.5200e-03 | -6.2048e-03 |
                | 7.5190e-03 | -4.7743e-03 |
                | 7.5180e-03 | -3.2745e-03 |
                | 7.5171e-03 | -1.7650e-03 |
                | 7.5161e-03 | -3.1259e-04 |
                +------------+-------------+            


    Visualization of the frame analysis results using CALFEM's visualization functions:

    .. code-block:: python

        plotpar = [2, 1, 0]
        sfac = cfv.scalfact2(ex3, ey3, edi3, 0.1)
        print("sfac=")
        print(sfac)

        cfv.figure(1)
        cfv.eldraw2(ex1, ey1, plotpar)
        cfv.eldraw2(ex2, ey2, plotpar)
        cfv.eldraw2(ex3, ey3, plotpar)

        plotpar = [1, 2, 1]
        cfv.dispbeam2(ex1, ey1, edi1, plotpar, sfac)
        cfv.dispbeam2(ex2, ey2, edi2, plotpar, sfac)
        cfv.dispbeam2(ex3, ey3, edi3, plotpar, sfac)
        cfv.axis([-1.5, 7.5, -0.5, 5.5])
        plotpar1 = 2
        cfv.scalgraph2(sfac, [1e-2, 0.5, 0], plotpar1)
        cfv.title("Displacements")

        # ----- Draw normal force diagram --------------------------------

        plotpar = [2, 1]
        sfac = cfv.scalfact2(ex1, ey1, es1[:, 0], 0.2)
        cfv.figure(2)
        cfv.secforce2(ex1, ey1, es1[:, 0], plotpar, sfac)
        cfv.secforce2(ex2, ey2, es2[:, 0], plotpar, sfac)
        cfv.secforce2(ex3, ey3, es3[:, 0], plotpar, sfac)
        cfv.axis([-1.5, 7.5, -0.5, 5.5])
        cfv.scalgraph2(sfac, [3e4, 1.5, 0], plotpar1)
        cfv.title("Normal force")

        # ----- Draw shear force diagram ---------------------------------

        plotpar = [2, 1]
        sfac = cfv.scalfact2(ex3, ey3, es3[:, 1], 0.2)
        cfv.figure(3)
        cfv.secforce2(ex1, ey1, es1[:, 1], plotpar, sfac)
        cfv.secforce2(ex2, ey2, es2[:, 1], plotpar, sfac)
        cfv.secforce2(ex3, ey3, es3[:, 1], plotpar, sfac)
        cfv.axis([-1.5, 7.5, -0.5, 5.5])
        cfv.scalgraph2(sfac, [3e4, 0.5, 0], plotpar1)
        cfv.title("Shear force")

        # ----- Draw moment diagram --------------------------------------

        plotpar = [2, 1]
        sfac = cfv.scalfact2(ex3, ey3, es3[:, 2], 0.2)
        print("sfac=")
        print(sfac)

        cfv.figure(4)
        cfv.secforce2(ex1, ey1, es1[:, 2], plotpar, sfac)
        cfv.secforce2(ex2, ey2, es2[:, 2], plotpar, sfac)
        cfv.secforce2(ex3, ey3, es3[:, 2], plotpar, sfac)
        cfv.axis([-1.5, 7.5, -0.5, 5.5])
        cfv.scalgraph2(sfac, [3e4, 0.5, 0], plotpar1)
        cfv.title("Moment")

        cfv.show_and_wait()

    .. only:: html
        
        .. figure:: images/exs6_3.svg
            :align: center
            :width: 600px
    
    .. only:: latex
        
        .. figure:: images/exs6_3.svg
            :align: center
            :width: 70%
        
        Displacement diagram

    .. only:: html
        
        .. figure:: images/exs6_4.svg
            :align: center
            :width: 600px
    
    .. only:: latex
        
        .. figure:: images/exs6_4.svg
            :align: center
            :width: 70%
        
        Normal force diagram

    .. only:: html
        
        .. figure:: images/exs6_5.svg
            :align: center
            :width: 600px
    
    .. only:: latex
        
        .. figure:: images/exs6_5.svg
            :align: center
            :width: 70%
        
        Shear force diagram

    .. only:: html
        
        .. figure:: images/exs6_6.svg
            :align: center
            :width: 600px
    
    .. only:: latex
        
        .. figure:: images/exs6_6.svg
            :align: center
            :width: 70%
        
        Moment diagram
