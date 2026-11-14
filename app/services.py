from . import pricing as pr
from .payments import charge


def checkout(cart, code):
    total = pr.apply_discount(sum(cart), code)
    return charge(total)
