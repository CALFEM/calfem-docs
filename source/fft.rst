fft
^^^

:Purpose:

    Transform functions in time domain to frequency domain.

:Syntax:

    .. code-block:: matlab

        p = fft(g)
        p = fft(g, N)

:Description:

    The ``fft`` function transforms a time dependent function to the frequency domain.

    The function to be transformed is stored in the vector ``g``.
    Each row in ``g`` contains the value of the function at equal time intervals.
    The function represents a span :math:`-\infty \leq t \leq +\infty`; however, only the values within a typical period are specified by ``g``.

    The ``fft`` command can be used with one or two input arguments.
    If ``N`` is not specified, the number of frequencies used in the transformation is equal to the number of points in the time domain (i.e., the length of the variable ``g``), and the output will be a vector of the same size containing complex values representing the frequency content of the input signal.

    The scalar variable ``N`` can be used to specify the number of frequencies used in the Fourier transform. The size of the output vector in this case will be equal to ``N``. It should be remembered that the highest harmonic component in the time signal that can be identified by the Fourier transform corresponds to half the sampling frequency. The sampling frequency is equal to :math:`1/dt`, where :math:`dt` is the time increment of the time signal.

    The complex Fourier coefficients :math:`p(k)` are stored in the vector ``p``, and are computed according to

    .. math::

        p(k) = \sum_{j=1}^N x(j) \omega_N^{(j-1)(k-1)},

    where

    .. math::

        \omega_N = e^{-2 \pi i / N}.

    .. note::

        This is a MATLAB built-in function.
