exs_flw_temp1
^^^^^^^^^^^^^

.. index:: exs_flw_temp1

:Purpose:

    Analysis of one-dimensional heat flow.

:Description:

    Consider a wall built up of concrete and thermal insulation. The outdoor temperature is :math:`-17°\text{C}` and the temperature inside is :math:`20°\text{C}`. At the inside of the thermal insulation there is a heat source yielding :math:`10` W/m².

    .. only:: html
        
        .. figure:: images/exs2_1.svg
            :align: center
            :width: 40em
    
    .. only:: latex
        
        .. figure:: images/exs2_1.svg
            :align: center
            :width: 70%

    .. only:: html
        
        .. figure:: images/exs2_2.svg
            :align: center
            :width: 40em
    
    .. only:: latex
        
        .. figure:: images/exs2_2.svg
            :align: center
            :width: 70%

    The wall is subdivided into five elements and the one-dimensional spring (analogy) element :code:`spring1e` is used. Equivalent spring stiffnesses are :math:`k_i=\lambda A/L` for thermal conductivity and :math:`k_i=A/R` for thermal surface resistance. Corresponding spring stiffnesses per m² of the wall are:

    .. list-table::
       :widths: 20 30 10 20 20
       :header-rows: 0

       * - :math:`k_1 =`
         - :math:`1/0.04`
         - :math:`=`
         - :math:`25.0`
         - W/K
       * - :math:`k_2 =`
         - :math:`1.7/0.070`
         - :math:`=`
         - :math:`24.3`
         - W/K
       * - :math:`k_3 =`
         - :math:`0.040/0.100`
         - :math:`=`
         - :math:`0.4`
         - W/K
       * - :math:`k_4 =`
         - :math:`1.7/0.100`
         - :math:`=`
         - :math:`17.0`
         - W/K
       * - :math:`k_5 =`
         - :math:`1/0.13`
         - :math:`=`
         - :math:`7.7`
         - W/K

:Example:

    The computation is initialized by importing CALFEM and NumPy. A global system matrix :code:`K` and a heat flow vector :code:`f` are defined. The heat source inside the wall is considered by setting :math:`f_4=10`. The element matrices :code:`Ke` are computed using :code:`cfc.spring1e`, and the function :code:`cfc.assem` assembles the global stiffness matrix. The system of equations is solved using :code:`cfc.solveq` with boundary conditions. The prescribed temperatures are :math:`T_1=-17°\text{C}` and :math:`T_6=20°\text{C}`:

    .. tabs::

        .. tab:: Code

            .. code-block:: python

                import numpy as np
                import calfem.core as cfc
                import calfem.utils as cfu

                # ----- Topology -------------------------------------------------

                edof = np.array([
                    [1, 2],
                    [2, 3],
                    [3, 4],
                    [4, 5],
                    [5, 6]
                ])

                # ----- Stiffness matrix K and load vector f ---------------------

                K = np.array(np.zeros((6, 6)))
                f = np.array(np.zeros((6, 1)))
                f[3] = 10.0

                # ----- Element stiffness and element load matrices  -------------

                ep1 = 25
                ep2 = 24.3
                ep3 = 0.4
                ep4 = 17
                ep5 = 7.7

                Ke1 = cfc.spring1e(ep1)
                Ke2 = cfc.spring1e(ep2)
                Ke3 = cfc.spring1e(ep3)
                Ke4 = cfc.spring1e(ep4)
                Ke5 = cfc.spring1e(ep5)

                # ----- Assemble Ke into K ---------------------------------------

                cfc.assem(edof[0, :], K, Ke1)
                cfc.assem(edof[1, :], K, Ke2)
                cfc.assem(edof[2, :], K, Ke3)
                cfc.assem(edof[3, :], K, Ke4)
                cfc.assem(edof[4, :], K, Ke5)

                # ----- Solve the system of equations ----------------------------

                bc = np.array([1, 6])
                bcVal = np.array([-17, 20])
                a, r = cfc.solveq(K, f, bc, bcVal) 

                cfu.disp_h2("Temperatures a:")
                cfu.disp_array(a, tablefmt="plain")

                cfu.disp_h2("Reaction flows r:")
                cfu.disp_array(r, tablefmt="plain")

        .. tab:: Output

            .. code::

                ## Temperatures a:

                -1.7000e+01
                -1.6438e+01
                -1.5861e+01
                 1.9238e+01
                 1.9475e+01
                 2.0000e+01

                ## Reaction flows r:

                -1.4039e+01
                -5.6843e-14
                -1.1546e-14
                 0.0000e+00
                 5.6843e-14
                 4.0394e+00            

    The temperature values :math:`a_i` at the node points are given in the vector :code:`a` and the boundary heat flows in the vector :code:`r`.

    After solving the system of equations, the heat flow through each element is computed using :code:`cfc.extract_ed` and :code:`cfc.spring1s`:

    .. tabs::

        .. tab:: Code

            .. code-block:: python

                ed1 = cfc.extract_ed(edof[0, :], a)
                ed2 = cfc.extract_ed(edof[1, :], a)
                ed3 = cfc.extract_ed(edof[2, :], a)
                ed4 = cfc.extract_ed(edof[3, :], a)
                ed5 = cfc.extract_ed(edof[4, :], a)

                q1 = cfc.spring1s(ep1, ed1)
                q2 = cfc.spring1s(ep2, ed2)
                q3 = cfc.spring1s(ep3, ed3)
                q4 = cfc.spring1s(ep4, ed4)
                q5 = cfc.spring1s(ep5, ed5)

                cfu.disp_h2("Element flows:")

                print("q1 = ")
                print(q1)
                print("q2 = ")
                print(q2)
                print("q3 = ")
                print(q3)
                print("q4 = ")
                print(q4)
                print("q5 = ")
                print(q5)

        .. tab:: Output

            .. code:: 
                
                ## Element flows:

                q1 =
                14.039386189223357
                q2 =
                14.039386189223451
                q3 =
                14.039386189223485
                q4 =
                4.039386189223492
                q5 =
                4.03938618922342                

    The heat flow through the wall is :math:`q=14.0` W/m² in the part of the wall to the left of the heat source (elements 1-3), and :math:`q=4.0` W/m² in the part to the right of the heat source (elements 4-5). This demonstrates how the internal heat source affects the heat flow distribution through the wall.
