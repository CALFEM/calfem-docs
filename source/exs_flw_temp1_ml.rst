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
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/exs2_1.svg
            :align: center
            :width: 70%

    .. only:: html
        
        .. figure:: images/exs2_2.svg
            :align: center
            :width: 400px
    
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

    A global system matrix :code:`K` and a heat flow vector :code:`f` are defined. The heat source inside the wall is considered by setting :math:`f_4=10`. The element matrices :code:`Ke` are computed using :code:`spring1e`, and the function :code:`assem` assembles the global stiffness matrix.

    The system of equations is solved using :code:`solveq` with considerations to the boundary conditions in :code:`bc`. The prescribed temperatures are :math:`a_1=-17°\text{C}` and :math:`a_6=20°\text{C}`.

    .. code-block:: matlab

        >> Edof=[1  1 2
                 2  2 3;
                 3  3 4;
                 4  4 5;
                 5  5 6];

        >> K=zeros(6);
        >> f=zeros(6,1);  f(4)=10

        f =

             0
             0
             0
            10
             0
             0

        >> ep1=[25];  ep2=[24.3];
        >> ep3=[0.4];  ep4=[17];
        >> ep5=[7.7];

        >> Ke1=spring1e(ep1);       Ke2=spring1e(ep2);
        >> Ke3=spring1e(ep3);       Ke4=spring1e(ep4);
        >> Ke5=spring1e(ep5);

        >> K=assem(Edof(1,:),K,Ke1);   K=assem(Edof(2,:),K,Ke2);
        >> K=assem(Edof(3,:),K,Ke3);   K=assem(Edof(4,:),K,Ke4);
        >> K=assem(Edof(5,:),K,Ke5);

        >> bc=[1 -17; 6 20];

        >> [a,r]=solveq(K,f,bc)

        a =

          -17.0000
          -16.4384
          -15.8607
           19.2378
           19.4754
           20.0000

        r =

          -14.0394
            0.0000
           -0.0000
           -0.0000
                 0
            0.0000
            4.0394

    The temperature values :math:`a_i` in the node points are given in the vector :code:`a` and the boundary flows in the vector :code:`r`.

    After solving the system of equations, the heat flow through the wall is computed using :code:`extract` and :code:`spring1s`:

    .. code-block:: matlab

        >> ed1=extract_ed(Edof(1,:),a);
        >> ed2=extract_ed(Edof(2,:),a);
        >> ed3=extract_ed(Edof(3,:),a);
        >> ed4=extract_ed(Edof(4,:),a);
        >> ed5=extract_ed(Edof(5,:),a);

        >> q1=spring1s(ep1,ed1)

        q1 =

           14.0394

        >> q2=spring1s(ep2,ed2)

        q2 =

           14.0394

        >> q3=spring1s(ep3,ed3)

        q3 =

           14.0394

        >> q4=spring1s(ep4,ed4)

        q4 =

            4.0394

        >> q5=spring1s(ep5,ed5)

        q5 =

            4.0394

    The heat flow through the wall is :math:`q=14.0` W/m² in the part of the wall to the left of the heat source, and :math:`q=4.0` W/m² in the part to the right of the heat source.
