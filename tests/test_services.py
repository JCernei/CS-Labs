import unittest
from src.services.user_management_service import UserManagementService
from src.services.digital_signature_service import DigitalSignatureService


class TestServices(unittest.TestCase):
    def test_user_management(self):
        database = {}
        user_manager = UserManagementService(database)
        user_manager.create_user(
            username='70m_470', password='5up3r_s3cRe7_p422w0rd')

        assert user_manager.validate_user(
            '70m_470', '5up3r_s3cRe7_p422w0rd') == True

    def test_digital_signature(self):
        message_signer = DigitalSignatureService()
        message = 'This message is certainly mine'
        signed_message, signature = message_signer.sign(message)

        assert message_signer.validate(signed_message, signature) == True


if __name__ == '__main__':
    unittest.main()
