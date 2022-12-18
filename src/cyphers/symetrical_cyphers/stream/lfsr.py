from src.cyphers.cypher import Cypher
from functools import reduce
from operator import xor


class Lfsr(Cypher):
    def __init__(self, register, taps):
        self.register = [int(x) for x in register.split(',')]
        self.origin = [int(x) for x in register.split(',')].copy()
        self.taps = [int(x) for x in taps.split(',')]

    def _generate_key_bit(self):
        new_bit = reduce(xor, [self.register[(len(self.register)-1)-t]
                         for t in self.taps])
        key_bit = self.register[0]
        del self.register[0]
        self.register.append(new_bit)
        return key_bit
