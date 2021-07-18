# Automated tests repository
Created with Python & Selenium by Ania Wójtowicz for task no.5 by Testuj.pl 

Repository contains Tests, Methods and xpaths folders:

**Tests**: automated tests contains code executing tasks

**Xpaths**: contains files with xpaths used for locating website elements


## Installation

To install and execute tests you need to create local venv, install dependencies, and then run Pytest.

> Please remember to run all commands from this README in the same path, where you checked out the project.

To create local venv please execute the following command: 
```
python -m venv .\venv
.\venv\Scripts\activate
```

After, please install all dependencies using the following command:
```
pip install -r .\requirements.txt 
```

Now, you are ready to execute tests. Please run command `pytest`

### Disclaimer

The repository covers all tests with Chrome browser only.
