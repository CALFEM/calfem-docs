ifft
^^^^

:Purpose:

    Transform function in frequency domain to time domain.

:Syntax:

    .. code-block:: matlab

        x = ifft(y)
        x = ifft(y, N)

:Description:

    ``ifft`` transforms a function in the frequency domain to a function in the time domain.

    The function to be transformed is given in the vector ``y``. Each row in ``y`` contains Fourier terms in the interval :math:`-\infty \leq \omega \leq +\infty`.

    The ``ifft`` command can be used with one or two input arguments. The scalar variable ``N`` can be used to specify the number of frequencies used in the Fourier transform. The size of the output vector in this case will be equal to ``N``. See also the description of the command ``fft``.

    The inverse Fourier coefficients :math:`x(j)`, stored in the variable ``x``, are computed according to

    .. math::

        x(j) = \frac{1}{N} \sum_{k=1}^N y(k) \omega_N^{-(j-1)(k-1)},

    where

    .. math::

        \omega_N = e^{-2 \pi i / N}.


    .. note:: 

        This is a MATLAB built-in function.

:See also:

    :ref:`fft`