#!/usr/bin/env python3
"""Module demonstrating mixins with a Dragon class."""


class SwimMixin:
    """Mixin providing swimming capability."""

    def swim(self):
        """Print swimming action."""
        print("The creature swims!")


class FlyMixin:
    """Mixin providing flying capability."""

    def fly(self):
        """Print flying action."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class combining swimming and flying abilities."""

    def roar(self):
        """Print roaring action."""
        print("The dragon roars!")
