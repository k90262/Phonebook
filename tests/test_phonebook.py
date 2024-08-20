import pytest

from phonebook import Phonebook


@pytest.fixture
def phonebook(tmpdir):
    "Provides an empty phonebook"
    phonebook = Phonebook(tmpdir)
    yield phonebook
    phonebook.clear()


def test_lookup_by_name(phonebook):
    phonebook.add("Bob", "12345")
    number = phonebook.lookup("Bob")
    assert "12345" == number


def test_lookup_by_missing_name(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("missing")


def test_is_consistent_with_empty_phonebook(phonebook):
    is_consistent = phonebook.is_consistent()
    assert is_consistent


def test_is_consistent_with_different_entries(phonebook):
    phonebook.add("Bob", "12345")
    phonebook.add("Anna", "012345")
    assert phonebook.is_consistent()


def test_is_consistent_with_duplicate_entries(phonebook):
    phonebook.add("Bob", "12345")
    phonebook.add("Sue", "12345")
    assert not phonebook.is_consistent()


def test_is_consistent_with_duplicate_prefix(phonebook):
    phonebook.add("Bob", "12345")
    phonebook.add("Sue", "123")
    assert not phonebook.is_consistent()

def test_is_consistent_all_names(phonebook):
    phonebook.add("Bob", "12345")
    assert phonebook.all_names() == {"Bob"}