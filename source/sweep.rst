.. _sweep:

sweep - Complex frequency response function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Purpose**

Compute complex frequency response functions.

**Syntax**

.. code-block:: matlab

    Y = sweep(K, C, M, p, w)

**Description**

``sweep`` computes the complex frequency response function for a system of the form:

.. math::

    [\mathbf{K} + i\omega\mathbf{C} - \omega^2 \mathbf{M} ]\mathbf{y}(\omega) = \mathbf{p}

Here, ``K``, ``C``, and ``M`` represent the *m*-by-*m* stiffness, damping, and mass matrices, respectively. The vector ``p`` defines the amplitude of the force. The frequency response function is computed for the values of :math:`\omega` given by the vector ``w``.

The complex frequency response function is stored in the matrix ``Y`` with dimension *m*-by-*n*, where *n* is equal to the number of circular frequencies defined in ``w``.

**Example**

The steady-state response can be computed by:

.. code-block:: matlab

    X = real(Y * exp(i * w * t));

and the amplitude by:

.. code-block:: matlab

    Z = abs(Y)
