.. -*- mode: rst -*-

|PyPI| |PythonVersion| |License| |Build| |CodeStyle|

.. |PyPI| image:: https://img.shields.io/pypi/v/webgenie
   :target: https://pypi.org/project/webgenie/

.. |PythonVersion| image:: https://img.shields.io/pypi/pyversions/webgenie
   :target: https://pypi.org/project/webgenie/

.. |License| image:: https://img.shields.io/pypi/l/webgenie
   :target: https://github.com/thenitinsharma/WebGenie/blob/main/LICENSE

.. |Build| image:: https://img.shields.io/github/actions/workflow/status/thenitinsharma/WebGenie/python-package.yml
   :target: https://github.com/thenitinsharma/WebGenie/actions

.. |CodeStyle| image:: https://img.shields.io/badge/code%20style-pep8-blue
   :target: https://peps.python.org/pep-0008/

.. image:: https://raw.githubusercontent.com/thenitinsharma/WebGenie/main/assets/webgenie-logo.png
   :target: https://github.com/thenitinsharma/WebGenie

**WebGenie** is a lightweight Python CLI tool that instantly generates a
complete, production-ready web development project structure with
pre-configured boilerplate code.

It is designed for **students, developers, freelancers, and hackathon teams**
who want to save time and focus on building features rather than setting up files.

The project is distributed under the **MIT License**.

Website / Repository:
https://github.com/thenitinsharma/WebGenie


Project Overview
----------------

WebGenie automates the creation of essential web development files such as:

- ``index.html``
- CSS and JavaScript files
- Backend starter files
- Database connection templates
- Organized folder structure
- Pre-written boilerplate code

Each generated project includes a watermark:

::

    Created by Nitin Kumar Sharma


Installation
------------

Dependencies
~~~~~~~~~~~~

WebGenie requires:

- Python >= 3.8

No additional dependencies are required.


User Installation
~~~~~~~~~~~~~~~~~

The easiest way to install WebGenie is using ``pip``::

    pip install webgenie


Usage
-----

After installation, create a new project by running::

    webgenie create my_project

This will generate a structured web project directory with ready-to-use files.


Generated Project Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Example output::

    my_project/
    ├── index.html
    ├── css/
    │   └── style.css
    ├── js/
    │   └── script.js
    ├── backend/
    │   └── server.py
    ├── database/
    │   └── db_config.py
    └── README.md


Features
--------

- 🚀 Instant project scaffolding
- 📁 Clean and organized folder structure
- 🧩 Ready-to-edit boilerplate code
- 🖥️ Command-line interface
- 🧠 Beginner-friendly
- 🏷️ Auto watermark for creator credit


Changelog
---------

See the `GitHub Releases <https://github.com/thenitinsharma/WebGenie/releases>`__
page for version history and updates.


Development
-----------

WebGenie is actively developed and maintained by **Nitin Kumar Sharma**.

Contributions, feature requests, and suggestions are welcome.


Important Links
~~~~~~~~~~~~~~~

- Source code: https://github.com/thenitinsharma/WebGenie
- Issue tracker: https://github.com/thenitinsharma/WebGenie/issues
- PyPI package: https://pypi.org/project/webgenie/


Source Code
~~~~~~~~~~~

Clone the repository::

    git clone https://github.com/thenitinsharma/WebGenie.git


Contributing
~~~~~~~~~~~~

To contribute:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

Please ensure your code follows PEP8 standards.


Testing
~~~~~~~

After cloning the project, tests (if available) can be run using::

    pytest


Roadmap
-------

Planned enhancements include:

- GUI-based project generator
- Framework-specific templates (React, Django, Flask)
- Database selection support
- PyPI upload assistant
- Plugin system for custom templates


Help and Support
----------------

If you encounter any issues or have feature requests, please open an issue on GitHub:

https://github.com/thenitinsharma/WebGenie/issues


Author
------

**Nitin Kumar Sharma**

- GitHub: https://github.com/thenitinsharma
- Python Developer | Web Developer | AI & ML Enthusiast


Citation
--------

If you use WebGenie in your project or research, attribution is appreciated:

::

    WebGenie – Created by Nitin Kumar Sharma
