from src.services.hash import hash
from src.cyphers.asymmetrical_cyphers.rsa import Rsa


class DigitalSignatureService:
    def __init__(self):
        self.cypher = Rsa(421, 691)

    def sign(self, message):
        signature = hash(message)
        encrypted_signature = self.cypher.sign_encrypt(signature)
        encrypted_message = self.cypher.sign_encrypt(message)
        return (encrypted_message, encrypted_signature)

    def validate(self, encrypted_message, encrypted_signature):
        recieved_message = ''.join(self.cypher.sign_decrypt(encrypted_message))
        recieved_signature = ''.join(
            self.cypher.sign_decrypt(encrypted_signature))
        if recieved_signature == hash(recieved_message):
            return True
        return False


if __name__ == "__main__":
    message_signer = DigitalSignatureService()

    message = 'This message is certainly mine'
    signed_message, signature = message_signer.sign(message)
    is_valid = message_signer.validate(signed_message, signature)

    if is_valid:
        print('Valid')
    else:
        print('Invalid')
