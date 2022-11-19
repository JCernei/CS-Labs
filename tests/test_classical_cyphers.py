import unittest
from src.cyphers.classical_cyphers.caesar import Caesar
from src.cyphers.classical_cyphers.caesar_with_keyword import CaesarWithKeyword
from src.cyphers.classical_cyphers.polybius_with_keyword import PolybiusWithKeyword
from src.cyphers.classical_cyphers.vigenere import Vigenere


class TestClassicalCyphers(unittest.TestCase):
    def test_caesar(self):
        cypher = Caesar(5)
        assert cypher.encrypt("anothersecretmessage") == "fstymjwxjhwjyrjxxflj"
        assert cypher.decrypt("fstymjwxjhwjyrjxxflj") == "anothersecretmessage"

    def test_caesar_with_keyword(self):
        cypher = CaesarWithKeyword(5, 'lemon')
        assert cypher.encrypt("letmein") == "abycbrf"
        assert cypher.decrypt("abycbrf") == "letmein"

    def test_polybius_with_keyword(self):
        cypher = PolybiusWithKeyword('lemon')
        assert cypher.encrypt(
            "whyareyourunning") == "52325421421254144542451515331531"
        assert cypher.decrypt(
            "52325421421254144542451515331531") == "whyareyourunning"

    def test_vigenere(self):
        cypher = Vigenere('super')
        assert cypher.encrypt("perasperaadastra") == "hygejhygervuhxis"
        assert cypher.decrypt("hygejhygervuhxis") == "perasperaadastra"


if __name__ == '__main__':
    unittest.main()
