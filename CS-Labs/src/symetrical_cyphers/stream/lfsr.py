from src.cypher import Cypher
from functools import reduce
from operator import xor


class Lfsr(Cypher):
    def __init__(self, register, taps):
        self.register = register
        self.origin = register.copy()
        self.taps = taps

    def _generate_key_bit(self):
        new_bit = reduce(xor, [self.register[(len(self.register)-1)-t]
                         for t in self.taps])
        key_bit = self.register[0]
        del self.register[0]
        self.register.append(new_bit)
        return key_bit
