"""Mapping from device-specific logical arrangements -> physical LEDs"""

from __future__ import division, absolute_import, print_function

from collections import namedtuple
from itertools import chain

from mindorb.scenetypes import LedColor


class HeroOrbMapping(object):
    """Mapping for the Hero Orbs"""
    LED_STRIP_LEN = 41

    def __init__(self, leds):
        self.leds = leds


class MemoryRackOrb(object):
    """Represents a single logical orb on the memory rack"""

    def __init__(self, shelf, section, orb, leds, led_ids):
        self.shelf = shelf
        self.section = section
        self.orb = orb
        self.leds = leds
        self.led_ids = led_ids
        self.colors = None

    def set_colors(self, color_a, color_b):
        if isinstance(color_a, LedColor):
            color_a = color_a.value
        if isinstance(color_b, LedColor):
            color_b = color_b.value

        for a_led in self.led_ids[:len(self.led_ids) // 2]:
            self.leds[a_led] = color_a
        for b_led in self.led_ids[len(self.led_ids) // 2:]:
            self.leds[b_led] = color_b

        self.colors = (color_a, color_b)


class MemoryRackMapping(object):
    """Maps the logical concept of orbs in a 2-dimension plane -> LED strips

    Origin is at the lower-right corner of the rack
    Coordinate system is: (shelf#, section#, orb#)
    Shelf -> bottom -> top
    Section -> right -> left
    Orb -> right -> left
    """
    LED_STRIP_LEN = 690

    def __init__(self, leds):
        self.leds = leds

        self.shelf_section_orb_map, self.all_orbs = self._get_orb_mappings()

    def _get_orb_mappings(self):
        # For now: do the simplistic thing and evenly cut up each section
        # Shove orbs to the right
        # Assume: 7 orbs will fit in each secion (40" / 14cm -> 7.25)
        # Group this by section -> within each section spacing should be pretty
        # consistent

        SecParams = namedtuple('SecParams',
                               ('n_orbs', 'r_offst', 'n_on', 'n_off'))

        # LEDs occupied = r_offst + n_orbs * n_on + (n_orbs - 1) * n_off
        sec_full = SecParams(7, 0, 5, 4)  # 59 LEDs
        sec_half = SecParams(3, 0, 5, 4)  # 23 LEDs

        def rrange(start, stop):
            """Helper for range-reversal since ranges are left -> right"""
            return list(reversed(range(start, stop)))

        led_idxs = [
            [rrange(630, 690), rrange(120, 180), rrange(60, 120)],
            [rrange(570, 630), rrange(180, 240), rrange(0, 60)],
            [rrange(510, 570), rrange(240, 300)],
            [rrange(450, 510), rrange(300, 330)],
            [rrange(390, 450)],
            [rrange(330, 390)],
        ]

        params = [
            [sec_full, sec_full, sec_full],
            [sec_full, sec_full, sec_full],
            [sec_full, sec_full],
            [sec_full, sec_half],
            [sec_full],
            [sec_full],
        ]

        shelf_sec_orb = []
        for shelf_n, shelf in enumerate(params):
            sections = []
            for sec_n, sec in enumerate(shelf):
                orbs = []
                for orb_n in range(0, sec.n_orbs):
                    start = sec.r_offst + orb_n * (sec.n_on + sec.n_off)
                    end = start + sec.n_on
                    orb = MemoryRackOrb(
                        shelf_n, sec_n, orb_n,
                        self.leds, led_idxs[shelf_n][sec_n][start:end])
                    orbs.append(orb)
                sections.append(orbs)
            shelf_sec_orb.append(sections)

        # At this point: the base map has been created
        # Here is where you'd go adjust the individual LED indices for
        # particular orbs if necessary.
        def shift_orbs(orbs, shift_right):
            for orb in orbs:
                orb.led_ids = [idx + shift_right for idx in orb.led_ids]

        # Correct alignment on the right-most sections
        for shelf in shelf_sec_orb:
            shift_orbs(shelf[0][0:2], -2)
            shift_orbs(shelf[0][2:4], -1)
            shift_orbs(shelf[0][6:7], 1)

        # Correct alignment on the middle sections (lower / full bits)
        for shelf in shelf_sec_orb[0:3]:
            shift_orbs(shelf[1][1:3], 1)
            shift_orbs(shelf[1][3:5], 2)
            shift_orbs(shelf[1][5:7], 3)
        shift_orbs(shelf_sec_orb[3][1][1:3], 1)

        all_orbs = list(
            chain.from_iterable(chain.from_iterable(shelf_sec_orb)))
        return shelf_sec_orb, all_orbs
