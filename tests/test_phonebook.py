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

def test_is_consistent_all_names(phonebook):
    phonebook.add("Bob", "12345")
    assert phonebook.all_names() == {"Bob"}

@pytest.mark.parametrize(
    "entry1, entry2, is_consistent", [
        (("Bob", "12345"), ("Anna", "012345"), True),
        (("Bob", "12345"), ("Sue", "12345"), False),
        (("Bob", "12345"), ("Sue", "123"), False),
    ]
)
def test_is_consistent(phonebook, entry1, entry2, is_consistent):
    phonebook.add(*entry1)
    phonebook.add(*entry2)
    assert phonebook.is_consistent() == is_consistent