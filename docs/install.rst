Install
=========

Very simple, just follow this steps:

1. Clone `wowa` locally::

    $ git clone https://github.com/arruda/wowa.git

2. Since `wowa` uses PostgreSQL in local development and in production, you'll need to install at least `libpq` and `Python` header files. On ubuntu this can be done by::

    $ sudo apt-get install libpq-dev python-dev


3. Install your local copy into a `virtualenv <http://virtualenv.readthedocs.org/en/latest/>`_. Assuming you have `virtualenvwrapper <http://virtualenvwrapper.readthedocs.org/en/latest/>`_ installed, this is how you set up your fork for local development::

    $ mkvirtualenv wowa
    $ cd wowa/
    $ pip install -r requirements/local.txt

4. Run the migrations::

    $ python wowa/manage.py migrate

5. Create a super-user for you::

    $ python wowa/manage.py createsuperuser

6. Run the server::

    $ python wowa/manage.py runserver


That's all.
