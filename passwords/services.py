import base64


class PasswordManager:
    """
        A utility class for encoding and decoding passwords using base64.
    """

    @staticmethod
    def encode_password(password):
        encoded_password = base64.b64encode(password.encode())
        return encoded_password

    @staticmethod
    def decode_password(encrypted_password):
        decoded_password = base64.b64decode(encrypted_password).decode()
        return decoded_password

