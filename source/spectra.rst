spectra - Seismic Response Spectra
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Compute seismic response spectra for elastic design.

**Syntax**

.. code-block:: matlab

    s = spectra(a, xi, dt, f)

**Description**

The ``spectra`` function computes the seismic response spectrum for a known acceleration history function.

- The computation is based on the vector ``a``, which contains an acceleration time history function defined at equal time steps.
- The time step is specified by the variable ``dt``.
- The value of the damping ratio is given by the variable ``xi``.
- Output from the computation, stored in the vector ``s``, is achieved at frequencies specified by the column vector ``f``.

**Example**

The following procedure can be used to produce a seismic response spectrum for a damping ratio :math:`\xi = 0.05`, defined at 34 logarithmically spaced frequency points. The acceleration time history ``a`` has been sampled at a frequency of 50 Hz, corresponding to a time increment ``dt = 0.02`` between collected points:

.. code-block:: matlab

    freq = logspace(0, log10(2^(33/6)), 34);
    xi = 0.05;
    dt = 0.02;
    s = spectra(a, xi, dt, freq');

The resulting spectrum can be plotted by the command:

.. code-block:: matlab

    loglog(freq, s, '*')
