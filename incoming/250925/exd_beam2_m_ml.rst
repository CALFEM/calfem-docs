exd_beam2_m
^^^^^^^^^^^

:Purpose: Set up the finite element model and perform eigenvalue analysis for a simple frame structure.

:Description: Consider the two dimensional frame shown below. A vertical beam is fixed at its lower end, and connected to a horizontal beam at its upper end. The horizontal beam is simply supported at the right end. The length of the vertical beam is 3 m and of the horizontal beam 2 m.

The following data apply to the beams:

.. list-table::
   :header-rows: 1
   :widths: 40 30 30

   * - 
     - vertical beam
     - horizontal beam
   * - Young's modulus (N/m²)
     - :math:`3 \times 10^{10}`
     - :math:`3 \times 10^{10}`
   * - Cross section area (m²)
     - :math:`0.1030 \times 10^{-2}`
     - :math:`0.0764 \times 10^{-2}`
   * - Moment of inertia (m⁴)
     - :math:`0.171 \times 10^{-5}`
     - :math:`0.0801 \times 10^{-5}`
   * - Density (kg/m³)
     - 2500
     - 2500

.. figure:: images/EXD1fBIG.png
   :align: center


a) Frame structure                          b) Element and DOF numbering

The structure is divided into 4 elements. The numbering of elements and degrees-of-freedom are apparent from the figure. The following ``.m``-file defines the finite element model:

:Example: Material data:

.. code-block:: matlab

   % --- material data ------------------------------------------
   E=3e10;                rho=2500;
   Av=0.1030e-2;          Iv=0.0171e-4;                 % IPE100
   Ah=0.0764e-2;          Ih=0.00801e-4;                % IPE80
   epv=[E Av Iv rho*Av];  eph=[E Ah Ih rho*Ah];

.. code-block:: matlab

   % ---  topology ----------------------------------------------
   Edof=[1    1  2  3  4  5  6
         2    4  5  6  7  8  9
         3    7  8  9 10 11 12
         4   10 11 12 13 14 15];
   % --- list of coordinates  -----------------------------------
   Coord=[0 0; 0 1.5; 0 3; 1 3; 2 3];
   % --- list of degrees-of-freedom  ----------------------------
   Dof=[1 2 3;  4 5 6;  7 8 9;  10 11 12;  13 14 15];
   % --- generate element matrices, assemble in global matrices -
   K=zeros(15);   M=zeros(15);
   [Ex,Ey]=coordxtr(Edof,Coord,Dof,2);
   for i=1:2
     [k,m,c]=beam2de(Ex(i,:),Ey(i,:),epv);
     K=assem(Edof(i,:),K,k);    M=assem(Edof(i,:),M,m);
   end
   for i=3:4
     [k,m,c]=beam2de(Ex(i,:),Ey(i,:),eph);
     K=assem(Edof(i,:),K,k);    M=assem(Edof(i,:),M,m);
   end

The finite element mesh is plotted, using the following commands:

.. code-block:: matlab

   clf;
   eldraw2(Ex,Ey,[1 2 2],Edof);
   grid; title('2D Frame Structure');
   pause;

.. figure:: images/exd1f2.png
   :align: center

   Finite element mesh

A standard procedure in dynamic analysis is eigenvalue analysis. This is accomplished by the following set of commands:

.. code-block:: matlab

   b=[1 2 3 14]';
   [La,Egv]=eigen(K,M,b);
   Freq=sqrt(La)/(2*pi);

Note that the boundary condition matrix, ``b``, only lists the degrees-of-freedom that are zero. The results of these commands are the eigenvalues, stored in ``La``, and the eigenvectors, stored in ``Egv``. The corresponding frequencies in Hz are calculated and stored in the column matrix ``Freq``:

.. math::

   \text{Freq} = \begin{bmatrix}
   6.9826 \\
   43.0756 \\
   66.5772 \\
   162.7453 \\
   230.2709 \\
   295.6136 \\
   426.2271 \\
   697.7628 \\
   877.2765 \\
   955.9809 \\
   1751.3
   \end{bmatrix}^T

The eigenvectors can be plotted by entering the commands below:

.. code-block:: matlab

   figure(1),    clf,     grid,    title('The first eigenmode'),
   eldraw2(Ex,Ey,[2 3 1]);
   Edb=extract_ed(Edof,Egv(:,1));     eldisp2(Ex,Ey,Edb,[1 2 2]);
   FreqText=num2str(Freq(1));      text(.5,1.75,FreqText);
   pause;

.. figure:: images/exd1f3.png
   :align: center

   The first eigenmode, 6.98 Hz

An attractive way of displaying the eigenmodes is shown in the figure below. The result is accomplished by translating the different eigenmodes in the x-direction, see the ``Ext``-matrix defined below, and in the y-direction, see the ``Eyt``-matrix:

.. code-block:: matlab

   clf, axis('equal'), hold on, axis off
   sfac=0.5;
   title('The first eight eigenmodes (Hz)' )
   for i=1:4;
     Ext=Ex+(i-1)*3;             eldraw2(Ext,Ey,[2 3 1]);
     Edb=extract_ed(Edof,Egv(:,i));
     eldisp2(Ext,Ey,Edb,[1 2 2],sfac);
     FreqText=num2str(Freq(i));  text(3*(i-1)+.5,1.5,FreqText);
   end;
   Eyt=Ey-4;
   for i=5:8;
     Ext=Ex+(i-5)*3;             eldraw2(Ext,Eyt,[2 3 1]);
     Edb=extract_ed(Edof,Egv(:,i));
     eldisp2(Ext,Eyt,Edb,[1 2 2],sfac);
     FreqText=num2str(Freq(i));  text(3*(i-5)+.5,-2.5,FreqText);
   end

.. figure:: images/exd1f4.png
   :align: center

   The first eight eigenmodes. Frequencies are given in Hz.
