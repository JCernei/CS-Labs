import unittest
from src.asymmetrical_cyphers.rsa import Rsa


class TestAsymmetricalCyphers(unittest.TestCase):
    def test_rsa(self):
        cypher = Rsa(421, 691)
        message = ('you shall not pass')
        encrypted_message = cypher.encrypt(message)
        decrypted_message = cypher.decrypt(encrypted_message)

        assert ''.join(map(str, encrypted_message)
                       ) == '2692731310411839959091149250251753598978115781159091208927131041102822909121039135989149250149250'

        assert ''.join(map(str, decrypted_message)) == 'you shall not pass'


if __name__ == '__main__':
    unittest.main()
