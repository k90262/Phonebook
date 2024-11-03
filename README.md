# Phonebook
Practice code for python tdd
- Lesson: https://app.pluralsight.com/library/courses/python-3-testing/table-of-contents

## Restore Packages form Requirement.txt
```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ deactivate
```

## Upate Requirement.txt
```bash
$ source .venv/bin/activate
$ pip freeze > requirements.txt
```