# hexadecimal string to binary conversion
def hex_to_bin(input):
    input_len = len(input) * 4
    input = int(input, 16)
    return f'{input:0{input_len}b}'

# binary to hexadecimal conversion


def bin_to_hex(input):
    input_len = len(input)//4
    input = int(input, 2)
    return f'{input:0{input_len}x}'

# xor 2 hexadecimal strings


def xor(a, b):
    input_len = max(len(a), len(b))
    input = int(a, 16) ^ int(b, 16)
    return f'{input:0{input_len}x}'

# string to bits


def to_bits(s):
    return list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in s])))

# bits to sting


def from_bits(bits):
    return "".join(chr(int("".join(map(str, bits[i:i+8])), 2)) for i in range(0, len(bits), 8))
