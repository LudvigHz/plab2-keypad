# TDT4113 project 5 - Keypad [![Actions Status](https://github.com/LudvigHz/plab2-keypad/workflows/.github/workflows/keypad/badge.svg)](https://github.com/ludvighz/plab2-keypad/actions)
> Repo for TDT4113 keypad assignment 2019

## Development
- ### Setup environment
  You need the `venv` python package installed
  ```sh
  python3 -m venv venv
  source venc/bin/activate
  pip install -r requirements.txt
  ```
- ### Codestyle
  We use pylint, and require a score of 8.0 or higher. Test with `pylint keypad`
  Formatting uses `black`. Format with `black keypad`

- ### Testing
  The project uses `unittest`. Test with `python -m unittest discover -v` to run all tests.
