import unittest
from encoder import (
    convert_message_to_dec,
    rotate_message,
    convert_message_to_str
)


class TestEncoder(unittest.TestCase):
    def test_convert_message_to_dec(self):
        plain_text = "Ensinamos e aprendemos constantemente"
        exp_result = [
            69, 110, 115, 105, 110, 97, 109, 111, 115, 32, 101, 32,
            97, 112, 114, 101, 110, 100, 101, 109, 111, 115, 32,
            99, 111, 110, 115, 116, 97, 110, 116, 101, 109, 101, 110, 116, 101
        ]
        self.assertEqual(convert_message_to_dec(plain_text), exp_result)

    def test_rotate_message(self):
        rot = 3
        message_in_dec = [
            69, 110, 115, 105, 110, 97, 109, 111, 115, 32, 101, 32,
            97, 112, 114, 101, 110, 100, 101, 109, 111, 115, 32,
            99, 111, 110, 115, 116, 97, 110, 116, 101, 109, 101, 110, 116, 101
        ]
        exp_result = [
            72, 113, 118, 108, 113, 100, 112, 114, 118, 35, 104, 35,
            100, 115, 117, 104, 113, 103, 104, 112, 114, 118, 35,
            102, 114, 113, 118, 119, 100, 113, 119, 104, 112, 104, 113, 119, 104
        ]
        self.assertEqual(rotate_message(message_in_dec, rot), exp_result)

    def test_convert_message_to_str(self):
        encoded_message_in_dec = [
            72, 113, 118, 108, 113, 100, 112, 114, 118, 35, 104, 35,
            100, 115, 117, 104, 113, 103, 104, 112, 114, 118, 35,
            102, 114, 113, 118, 119, 100, 113, 119, 104, 112, 104, 113, 119, 104
        ]
        exp_result = "Hqvlqdprv#h#dsuhqghprv#frqvwdqwhphqwh"
        self.assertEqual(convert_message_to_str(encoded_message_in_dec), exp_result)


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
