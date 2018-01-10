"""Effect helper functions
"""

from __future__ import division, absolute_import, print_function

from math import e, exp, pi, sin


def breathe(ts, color, amp=0.60, period=5.0, phase=0.0):
    """Apply a "breathing" effect to the LED color

    Args:
        ts (float): Timestamp of the frame in seconds
        color (tuple): Size 3 tuple desscriging the color value
        amp (float, optional): Amplitude of the cycle.  Constant offset is
            applied to make the peaks match the input color val.
        period (float, optional): Period of the cycle in seconds
        phase (float, optional): Phase offset in seconds

    Returns:
        TYPE: Description
    """
    t = 2 * pi * (ts - phase) / period

    return tuple(int(
        (exp(sin(t)) - 1 / e) * (val * amp) / (e - 1 / e) + val * (1 - amp))
        for val in color)
