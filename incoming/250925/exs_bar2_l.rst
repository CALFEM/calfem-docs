exs_bar2_l
^^^^^^^^^^

.. index:: exs_bar2_l

:Purpose:

    Analysis of a plane truss.

:Description:

    Consider a plane truss, loaded by a single force :math:`P=0.5` MN.

    .. figure:: images/exs4_1.png
        :align: center

    The corresponding finite element model consists of ten elements and twelve degrees of freedom.

    .. figure:: images/exs4_2.png
        :align: center

    **Material properties:**
    
    - Cross-sectional area: :math:`A=25.0 \times 10^{-4}` m²
    - Young's modulus: :math:`E=2.10 \times 10^{5}` MPa

:Example:

    The topology is defined by the matrix:

    .. code-block:: matlab

        >> Edof=[1   1  2  5  6;
                 2   3  4  7  8;
                 3   5  6  9 10;
                 4   7  8 11 12;
                 5   7  8  5  6;
                 6  11 12  9 10;
                 7   3  4  5  6;
                 8   7  8  9 10;
                 9   1  2  7  8;
                10   5  6 11 12];

    A global stiffness matrix :code:`K` and a load vector :code:`f` are defined. The load :math:`P` is divided into x and y components and inserted in the load vector :code:`f`:

    .. code-block:: matlab

        >> K=zeros(12);
        >> f=zeros(12,1);  f(11)=0.5e6*sin(pi/6);  f(12)=-0.5e6*cos(pi/6);

    The element matrices :code:`Ke` are computed by the function :code:`bar2e`. These matrices are then assembled in the global stiffness matrix using the function :code:`assem`:

    .. code-block:: matlab

        >> A=25.0e-4;    E=2.1e11;   ep=[E A];

        >> Ex=[0 2;
               0 2;
               2 4;
               2 4;
               2 2;
               4 4;
               0 2;
               2 4;
               0 2;
               2 4];

        >> Ey=[2 2;
               0 0;
               2 2;
               0 0;
               0 2;
               0 2;
               0 2;
               0 2;
               2 0;
               2 0];

    All the element matrices are computed and assembled in the loop:

    .. code-block:: matlab

        >> for i=1:10
              Ke=bar2e(Ex(i,:),Ey(i,:),ep);
              K=assem(Edof(i,:),K,Ke);
           end;

    The displacements in :code:`a` and the support forces in :code:`r` are computed by solving the system of equations considering the boundary conditions in :code:`bc`:

    .. code-block:: matlab

        >> bc=[1 0;2 0;3 0;4 0];
        >> [a,r]=solveq(K,f,bc)

        a =

                 0
                 0
                 0
                 0
            0.0024
           -0.0045
           -0.0016
           -0.0042
            0.0030
           -0.0107
           -0.0017
           -0.0113

        r =

          1.0e+005 *

           -8.6603
            2.4009
            6.1603
            1.9293
            0.0000
           -0.0000
           -0.0000
           -0.0000
            0.0000
            0.0000
            0.0000
            0.0000

    The displacement at the point of loading is :math:`-1.7 \times 10^{-3}` m in the x-direction and :math:`-11.3 \times 10^{-3}` m in the y-direction. At the upper support the horizontal force is :math:`-0.866` MN and the vertical :math:`0.240` MN. At the lower support the forces are :math:`0.616` MN and :math:`0.193` MN, respectively.

    Normal forces are evaluated from element displacements. These are obtained from the global displacements :code:`a` using the function :code:`extract_ed`. The normal forces are evaluated using the function :code:`bar2s`:

    .. code-block:: matlab

        ed=extract_ed(Edof,a);

        >> for i=1:10
              es=bar2s(Ex(i,:),Ey(i,:),ep,ed(i,:));
              N(i,:)=es(1);
           end

    The obtained normal forces are:

    .. code-block:: matlab

        >> N

        N =

          1.0e+005 *

            6.2594
           -4.2310
            1.7064
           -0.1237
           -0.6945
            1.7064
           -2.7284
           -2.4132
            3.3953
            3.7105

    The largest normal force :math:`N=0.626` MN is obtained in element 1 and is equivalent to a normal stress :math:`\sigma=250` MPa.

    To reduce the quantity of input data, the element coordinate matrices :code:`Ex` and :code:`Ey` can alternatively be created from a global coordinate matrix :code:`Coord` and a global topology matrix :code:`Dof` using the function :code:`coordxtr`:

    .. code-block:: matlab

        >> Coord=[0 2;
                  0 0;
                  2 2;
                  2 0;
                  4 2;
                  4 0];

        >> Dof=[ 1  2;
                 3  4;
                 5  6;
                 7  8;
                 9 10;
                11 12];

        >> [ex,ey]=coordxtr(Edof,Coord,Dof,2);
