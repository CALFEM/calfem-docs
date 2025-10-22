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

    A topology matrix :code:`Edof`, a global stiffness matrix :code:`K` and load vector :code:`f` are defined. The element matrices :code:`Ke` and :code:`fe` are computed by the function :code:`beam2e`. These matrices are then assembled in the global matrices using the function :code:`assem`:

    .. code-block:: matlab

        >>  Edof=[1  4  5  6  1  2  3;
                  2  7  8  9 10 11 12;
                  3  4  5  6  7  8  9];

        >> K=zeros(12);  f=zeros(12,1);  f(4)=2e+3;

        >> E=200e9;
        >> A1=2e-3;    A2=6e-3;
        >> I1=1.6e-5;  I2=5.4e-5;
        >> ep1=[E A1 I1];  ep3=[E A2 I2];

        >> ex1=[0 0];  ex2=[6 6];  ex3=[0 6];
        >> ey1=[0 4];  ey2=[0 4];  ey3=[4 4];
        >> eq1=[0 0];  eq2=[0 0];  eq3=[0 -10e+3];

        >> Ke1=beam2e(ex1,ey1,ep1);
        >> Ke2=beam2e(ex2,ey2,ep1);
        >> [Ke3,fe3]=beam2e(ex3,ey3,ep3,eq3);

        >> K=assem(Edof(1,:),K,Ke1);
        >> K=assem(Edof(2,:),K,Ke2);
        >> [K,f]=assem(Edof(3,:),K,Ke3,f,fe3);

    The system of equations are solved considering the boundary conditions in :code:`bc`:

    .. code-block:: matlab

        >> bc=[1 0; 2 0; 3 0; 10 0; 11 0];
        >> [a,r]=solveq(K,f,bc)

        a =                         r =

                 0                    1.0e+004 *
                 0
                 0                      0.1927
            0.0075                      2.8741
           -0.0003                      0.0445
           -0.0054                           0
            0.0075                      0.0000
           -0.0003                     -0.0000
            0.0047                     -0.0000
                 0                           0
                 0                      0.0000
           -0.0052                     -0.3927
                                        3.1259
                                             0

    The element displacements are obtained from the function :code:`extract`, and the function :code:`beam2s` computes the section forces and the displacements along the element:

    .. code-block:: matlab

        >> Ed=extract_ed(Edof,a);
        >> [es1,edi1]=beam2s(ex1,ey1,ep1,Ed(1,:),eq1,21)

        es1 =                           edi1 =

          1.0e+004 *                        0.0003    0.0075
                                            0.0003    0.0065
           -2.8741    0.1927    0.8152        .         .
           -2.8741    0.1927    0.7767      0.0000    0.0000
              .         .         .
           -2.8741    0.1927    0.0445

        >> [es2,edi2]=beam2s(ex2,ey2,ep1,Ed(2,:),eq2,21)

        es2 =                           edi2 =

          1.0e+004 *                        0.0003    0.0075
                                            0.0003    0.0084
           -3.1259   -0.3927   -1.5707        .         .    
           -3.1259   -0.3927   -1.4922      0.0000    0.0000
              .         .         .
           -3.1259   -0.3927   -0.0000

        >> [es3,edi3]=beam2s(ex3,ey3,ep3,Ed(3,:),eq3,21)

        es3 =                           edi3 =

          1.0e+004 *                        0.0075   -0.0003
                                            0.0075   -0.0019
           -0.3927   -2.8741   -0.8152        .         .
           -0.3927   -2.5741    0.0020      0.0075   -0.0003
              .         .         .
           -0.3927    3.1259   -1.5707

    A displacement diagram is displayed using the function :code:`dispbeam2` and section force diagrams using the function :code:`secforce2`:

    .. code-block:: matlab

        >> figure(1)
        >> plotpar=[2 1 0];
        >> eldraw2(ex1,ey1,plotpar);
        >> eldraw2(ex2,ey2,plotpar);
        >> eldraw2(ex3,ey3,plotpar);
        >> sfac=scalfact2(ex3,ey3,Ed(3,:),0.1);
        >> plotpar=[1 2 1];
        >> dispbeam2(ex1,ey1,edi1,plotpar,sfac);
        >> dispbeam2(ex2,ey2,edi2,plotpar,sfac);
        >> dispbeam2(ex3,ey3,edi3,plotpar,sfac);
        >> axis([-1.5 7.5 -0.5 5.5]);
        >> scalgraph2(sfac,[1e-2 0.5 0]);
        >> title('Displacements')

        >> figure(2)
        >> plotpar=[2 1];
        >> sfac=scalfact2(ex1,ey1,es1(:,1),0.2);
        >> secforce2(ex1,ey1,es1(:,1),plotpar,sfac);
        >> secforce2(ex2,ey2,es2(:,1),plotpar,sfac);
        >> secforce2(ex3,ey3,es3(:,1),plotpar,sfac);
        >> axis([-1.5 7.5 -0.5 5.5]);
        >> scalgraph2(sfac,[3e4 1.5 0]);
        >> title('Normal force')

        >> figure(3)
        >> plotpar=[2 1];
        >> sfac=scalfact2(ex3,ey3,es3(:,2),0.2);
        >> secforce2(ex1,ey1,es1(:,2),plotpar,sfac);
        >> secforce2(ex2,ey2,es2(:,2),plotpar,sfac);
        >> secforce2(ex3,ey3,es3(:,2),plotpar,sfac);
        >> axis([-1.5 7.5 -0.5 5.5]);
        >> scalgraph2(sfac,[3e4 0.5 0]);
        >> title('Shear force')

        >> figure(4)
        >> plotpar=[2 1];
        >> sfac=scalfact2(ex3,ey3,es3(:,3),0.2);
        >> secforce2(ex1,ey1,es1(:,3),plotpar,sfac);
        >> secforce2(ex2,ey2,es2(:,3),plotpar,sfac);
        >> secforce2(ex3,ey3,es3(:,3),plotpar,sfac);
        >> axis([-1.5 7.5 -0.5 5.5]);
        >> scalgraph2(sfac,[3e4 0.5 0]);
        >> title('Moment')

    .. only:: html
        
        .. figure:: images/exs6_3.svg
            :align: center
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/exs6_3.svg
            :align: center
            :width: 70%
        
        Displacement diagram

    .. only:: html
        
        .. figure:: images/exs6_4.svg
            :align: center
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/exs6_4.svg
            :align: center
            :width: 70%
        
        Normal force diagram

    .. only:: html
        
        .. figure:: images/exs6_5.svg
            :align: center
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/exs6_5.svg
            :align: center
            :width: 70%
        
        Shear force diagram

    .. only:: html
        
        .. figure:: images/exs6_6.svg
            :align: center
            :width: 400px
    
    .. only:: latex
        
        .. figure:: images/exs6_6.svg
            :align: center
            :width: 70%
        
        Moment diagram
