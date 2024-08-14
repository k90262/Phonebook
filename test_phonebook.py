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

    def test_lookup_by_missing_name(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    def test_is_consistent_with_empty_phonebook(self):
        is_consistent = self.phonebook.is_consistent()
        self.assertTrue(is_consistent)

    def test_is_consistent(self):
        self.phonebook.add("Bob", "12345")
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add("Anna", "012345")
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add("Sue", "12345") # identical to Bob
        self.assertFalse(self.phonebook.is_consistent())
        self.phonebook.add("Sue", "123") # prefix of Bob
        self.assertFalse(self.phonebook.is_consistent())
