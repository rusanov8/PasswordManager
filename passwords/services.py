import base64


class PasswordManager:
    """
        A utility class for encoding and decoding passwords using base64.
    """

    @staticmethod
    def encode_password(password):
        return base64.b64encode(password.encode()).decode()

    @staticmethod
    def decode_password(encrypted_password):
        return base64.b64decode(encrypted_password).decode()
