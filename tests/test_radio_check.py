import unittest

from homeguard_system import respond_to_radio_check


class RadioCheckTests(unittest.TestCase):
    def test_expected_phrase_returns_ack(self):
        self.assertEqual(respond_to_radio_check("прием. слышно меня?"), "Да, слышно.")

    def test_other_message_returns_generic_response(self):
        self.assertEqual(respond_to_radio_check("hello"), "Сообщение получено.")


if __name__ == "__main__":
    unittest.main()
