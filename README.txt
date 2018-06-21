===============================
beyondskins.plonesymposium.site
===============================

.. contents:: Table of Contents
   :depth: 2


Introduction
============

**Plone Symposium South America** 2012 edition Theme is an installable Plone Theme developed 
by `Simples Consultoria`_ using the **theming** and **packaging** features available 
in `plone.app.theming`_ and `plone.app.themingplugins`_ packages.


Requirements
============

- From the Plone 4.2.x To the Plone 4.3 latest versión (https://plone.org/download)
- The ``plone.app.theming`` and ``plone.app.themingplugins`` packages (*will be installed as a dependency of this package*)


Screenshots
===========

Layout of the site when viewed in a computer resolution:

.. image:: https://github.com/plonegovbr/beyondskins.plonesymposium.site/raw/master/src/beyondskins/plonesymposium/site/themes/beyondskins.plonesymposium.site/preview.png


Features
========

- It's an installable Plone Theme package.
- After installation from Add-ons controlpanel, this theme is enabled automatically.
- It's have support clean uninstallation.
- It's uses ``plone.app.themingplugins`` package to override templates.
- Also it's a simple Diazo package (Zip file).


Installation
============

For install and enables this product, please, read the installation guide from ``docs/INSTALL.txt`` file in this package.


Usage
=====

A theme intended for use with mobile theming control panel (``zettwerk.mobiletheming``).

You probably want to use the theme like this:

- Install ``beyondskins.plonesymposium.site`` package

- Or, of course it is possible to enable the theme in diazo theme control panel and use it as a regular theme


When you want to edit the theme, you should do this on the file system.
If you duplicate it TTW, the overridden templates will not be used.


plone.app.themingplugins integration
------------------------------------

The theme uses ``plone.app.themingplugins`` package to override templates just for this theme.
These templates will not work if you duplicate the theme TTW (``plone.app.themingplugins`` package do not work for that).


Contribute
==========

- Issue Tracker: https://github.com/plonegovbr/beyondskins.plonesymposium.site/issues
- Source Code: https://github.com/plonegovbr/beyondskins.plonesymposium.site


License
=======

The project is licensed under the GPLv2.


Credits
-------

- Andre Nogueira (agnogueira at gmail dot com).


- Érico Andrei (ericof at gmail dot com).


Amazing contributions
---------------------

- Leonardo J. Caballero G. aka macagua (leonardocaballero at gmail dot com).

.. _`Simples Consultoria`: http://www.simplesconsultoria.com.br/
.. _`plone.app.theming`: https://pypi.org/project/plone.app.theming/
.. _`plone.app.themingplugins`: https://pypi.org/project/plone.app.themingplugins/
