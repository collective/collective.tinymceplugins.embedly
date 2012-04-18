=================================
collective.tinymceplugins.embedly
=================================

Introduction
============

This package adds the Embedly TinyMCE plugin to Plone.

Currently based on version 2.0.9 of the source available in the
`WordPress.org subversion repository
<http://plugins.svn.wordpress.org/embedly/tags/2.0.9/>`_.

This product was developed by `Netsight Internet Solutions Limited
<http://www.netsight.co.uk>`_. Its official repository and bug tracker
is at
`http://github.com/collective/collective.tinymceplugins.embedly`.

Installation
============

Add the collective.tinymceplugins.embedly egg to your buildout.cfg and
install using the QuickInstaller.

Configuration
=============

To use the Embedly plugin on your site, you need to provide an API key
(available from `embed.ly <http://embed.ly/>`_). You can set the API
key by going to Site Setup -> Configuration Registry and setting the
api_key value.

Alternatives
============

This product can be used alongside `collective.embedly
<http://github.com/collective/collective.embedly>`_ and
`collective.oembed <http://github.com/collective/collective.oembed>`_.
This is the only Plone add-on product of the 3 to include full TinyMCE
integration.

Dependencies
============

collective.tinymceplugins.embedly currently depends on version 1.3dev
or higher of `Products.TinyMCE
<http://github.com/plone/Products.TinyMCE>`_. This is because the
embed.ly TinyMCE plugin designed for WordPress is aimed at TinyMCE
version 3.4.5 or higher.