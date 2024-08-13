import unittest

from phonebook import Phonebook


class PhonebookTest(unittest.TestCase):
    def setUp(self) -> None:
        self.phonebook = Phonebook()

    def teardown(self) -> None:
        pass

    def test_lookup_by_name(self):
        self.phonebook.add("Bob", "12345")

        number = self.phonebook.lookup("Bob")

        self.assertEqual("12345", number)

    def test_missing_name(self):
        self.phonebook = Phonebook()

        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    def test_empty_phonebook_is_consistent(self):
        self.phonebook = Phonebook()
        is_consistent = self.phonebook.is_consistent()
        self.assertTrue(is_consistent)