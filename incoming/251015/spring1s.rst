spring1s
^^^^^^^^

:Purpose:
    Compute spring force in a spring element.

    .. figure:: images/SPRING3.png
        :width: 70%
        :align: center

:Syntax:
.. only:: matlab

    .. code-block:: matlab

        es = spring1s(ep, ed)

.. only:: python

    .. code-block:: python

        es = cfc.spring1s(ep, ed)

:Description:
    :code:`spring1s` computes the spring force in the spring element :code:`spring1e`.

    The input variable :code:`ep` is defined in :code:`spring1e` and the
    element nodal displacements :code:`ed` are obtained by the function :code:`extract_ed`.

    .. The output variable 
        
    ..    :code:`es = [`:math:`N` :code:`]` 
        
    .. contains the spring force, or the analog quantity. 

    The output variable 
        
    :code:`es`:math:`= [N]` 
        
    contains the spring force, or the analog quantity. 

:Theory:
    The spring force :math:`N`, or analog quantity, is computed according to

    .. math::

        N = k \left(u_2 - u_1\right)
