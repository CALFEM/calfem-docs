exd_beam2_tr
^^^^^^^^^^^^

.. index:: exd_beam2_tr

:Purpose:

    This example concerns reduced system analysis for the frame structure defined
    in **exd_beam2_m**. Transient analysis on modal coordinates is performed for the
    reduced system.

:Description:

    In the previous example the transient analysis was based on the original
    finite element model.
    Transient analysis can also be employed on some type of reduced system,
    commonly a subset of the eigenvectors.
    The commands below pick out the first two eigenvectors for a subsequent
    time integration, see constant **nev**.
    The result in the figure below
    shall be compared to the result in **exd2**.

    .. figure:: images/exd31.png
        :align: center

        Time history at DOF 4 and DOF 11 using two eigenvectors.

:Example Code:

.. code-block:: matlab

    dt=0.002;    T=1;    nev=2;
    % --- the load -----------------------------------------------
    G=[0 0; 0.15 1; 0.25 0; T 0];       [t,g]=gfunc(G,dt);
    f=zeros(15, length(g));             f(4,:)=9000*g;
    fr=sparse([[1:1:nev]' Egv(:,1:nev)'*f]);
    % --- reduced system matrices --------------------------------
    kr=sparse(diag(diag(Egv(:,1:nev)'*K*Egv(:,1:nev))));
    mr=sparse(diag(diag(Egv(:,1:nev)'*M*Egv(:,1:nev))));
    % --- initial condition --------------------------------------
    ar0=zeros(nev,1);                   dar0=zeros(nev,1);
    % --- output parameters --------------------------------------
    times=[0.1:0.1:1];        dofsr=[1:1:nev];       dofs=[4 11];
    % --- time integration parameters ----------------------------
    ip=[dt T 0.25 0.5];
    % --- time integration ---------------------------------------
    [ar,dar,d2ar,arhist,darhist,d2arhist]...
    =step2(kr,[],mr,fr,ar0,dar0,[],ip,times,dofsr);
    % --- mapping back to original coordinate system -------------
    aR=Egv(:,1:nev)*ar;         aRhist=Egv(dofs,1:nev)*arhist;
    % --- plot time history for two DOF:s ------------------------
    figure(1), plot(t,aRhist(1,:),'-',t,aRhist(2,:),'--')
    axis([0    1.0000   -0.0100    0.0200])
    grid, xlabel('time (sec)'), ylabel('displacement (m)')
    title('Displacement(time) at the 4th and 11th'...
          ' degree-of-freedom')
    text(0.3,0.017,'solid line = impact point, x-direction')
    text(0.3,0.012,'dashed line = center, horizontal beam,'...
                   ' y-direction')
    text(0.3,-0.007,'2 EIGENVECTORS ARE USED')
