Introduction
============

What is BIGREST?
----------------

| F5 BIG-IP and BIG-IQ devices have an API called iControl REST.
| BIGREST is a SDK with multiple methods and functions that simplifies the use of the iControl REST API.

BIGREST functionalities
-----------------------

- Supports partition
- Supports route domain
- Implements all HTTP methods used in the iControl REST API
- Implements HTTP path /stats
- Implements HTTP path /example
- Implements command
- Implements task
- Implements transaction

Documentation
-------------

link

Source code
-------------

https://github.com/leonardobdes/BIGREST

Author
------

| **Name:** 
| Leonardo Souza

| **LinkedIn:** 
| https://uk.linkedin.com/in/leonardobdes

How to install?
---------------

**Requires Python version 3.7**

Install BIGREST using Python **pip**

.. code-block:: python

   pip install bigrest

How to use?
---------------

**In the following example:**

:192.168.1.245:
    IP or name of the F5 device.
:admin:
    Username to be used to connect to the device.
:password:
    Password to be used to connect to the device.

**First, import the SDK:**

.. code-block:: python

   from bigrest import BIGIP

**Next, create a device object:**

.. code-block:: python

   device = BIGIP("192.168.1.245", "admin", "password")

**Lastily, load all virtual servers and print their names:**

.. code-block:: python

   virtuals = device.load("/mgmt/tm/ltm/virtual")
   for virtual in virtuals:
       print(virtual.properties["name"])

| This is just a simple example, to give a first view about the SDK.
| Detailed information about how to use the SDK will be provide in the next sections of this documentation.

How to get help?
----------------

If you have problems to use this SDK, or to understand how the F5 iControl REST API works, use `DevCentral <https://devcentral.f5.com/>`_ website to get help.

How to report bugs?
-------------------

| Use `GitHub <https://github.com/leonardobdes/BIGREST/issues>`_ issues to report bugs.
| For any bug, please provide the following information.

**BIGREST version:**

Run the following command to find the version you are using.

.. code-block:: python

   pip show bigrest

**F5 device type:**

BIG-IP or BIG-IQ

**F5 device version:**

Run the following command to find the version you are using.

.. code-block:: python

   tmsh show sys version

**Python code to replicate the bug.**

**Output generated when bug is triggered.**

How to request new functionalities?
-----------------------------------

| Use `GitHub <https://github.com/leonardobdes/BIGREST/issues>`_ issues to request new functionalities.
| Use the following format in the title **RFE - Title**.