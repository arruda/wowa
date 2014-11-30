============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/arruda/wowa/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "feature"
is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

wowa could always use more documentation, whether as part of the
official wowa docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/arruda/wowa/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `wowa` for local development.

1. Fork the `wowa` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/wowa.git

3. Since `wowa` uses PostgreSQL in local development and in production, you'll need to install at least `libpq` and `Python` header files. On ubuntu this can be done by::

    $ sudo apt-get install libpq-dev python-dev

4. Install your local copy into a `virtualenv <http://virtualenv.readthedocs.org/en/latest/>`_. Assuming you have `virtualenvwrapper <http://virtualenvwrapper.readthedocs.org/en/latest/>`_ installed, this is how you set up your fork for local development::

    $ mkvirtualenv wowa
    $ cd wowa/
    $ pip install -r requirements/local.txt

5. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

6. When you're done making changes, check that your changes pass flake8 and the tests. But first you'll need to create a new virtualenv::

    $ mkvirtualenv wowa_test
    $ pip install -r requirements/test.txt
    $ make lint
    $ make coverage

7. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

8. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. Check https://travis-ci.org/arruda/wowa/pull_requests and make sure that the tests pass.
