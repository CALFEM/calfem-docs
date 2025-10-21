.. _freqresp:
.. index:: 
   single: freqresp
   single: frequency response
   single: frequency domain
   single: transfer function
   single: vibration analysis
   pair: frequency; response
   pair: vibration; analysis
   pair: transfer; function
   pair: frequency; domain
   pair: dynamic; response

freqresp
^^^^^^^^

:Purpose:  

    Compute frequency response of a known discrete time response.

:Syntax:  

    .. code:: matlab

        [Freq, Resp] = freqresp(D, dt)

:Description:  

    ``freqresp`` computes the frequency response of a discrete dynamic system.

    - ``D`` is the time history function.
    - ``dt`` is the sampling time increment, i.e., the time increment used in the time integration procedure.
    - ``Resp`` contains the computed response as a function of frequency.
    - ``Freq`` contains the corresponding frequencies.

:Example:

    The result can be visualized by::

        plot(Freq, Resp)
        xlabel('frequency (Hz)')

    or::

        semilogy(Freq, Resp)
        xlabel('frequency (Hz)')

    The dimension of ``Resp`` is the same as that of the original time history function.

    .. note:: 

        The time history function of a discrete system computed by direct integration often behaves in an unstructured manner. The reason for this is that the time history is a mixture of several participating eigenmodes at different eigenfrequencies. By using a Fourier transform, however, the response as a function of frequency can be computed efficiently. In particular, it is possible to identify the participating frequencies.
