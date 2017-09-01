Malta Public Holidays Scarper
=============================

This is a quick solution to scrape holidays of a website and
produce an ICS file.

Currently it's hard-coded to snag holidays for the
3 next years from https://publicholidays.com.mt/

Running
-------

Checkout this git repository, and execute the script:

.. code-block:: bash

   # python 3.6 is required, get it with pyenv
   # pyenv shell 3.6.2

   pip install --user pipenv
   pipenv install
   pipenv run python main.py
