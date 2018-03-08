# -*- coding: utf-8 -*-
"""
    pygments.plugin
    ~~~~~~~~~~~~~~~

    Pygments setuptools plugin interface. The methods defined
    here also work if setuptools isn't installed but they just
    return nothing.

    lexer plugins::

        [pygments.lexers]
        yourlexer = yourmodule:YourLexer

    formatter plugins::

        [pygments.formatters]
        yourformatter = yourformatter:YourFormatter
        /.ext = yourformatter:YourFormatter

    As you can see, you can define extensions for the formatter
    with a leading slash.

    syntax plugins::

        [pygments.styles]
        yourstyle = yourstyle:YourStyle

    filter plugin::

        [pygments.filter]
        yourfilter = yourfilter:YourFilter


    :copyright: Copyright 2006-2017 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
    
    Changed by Michael Butscher 2018-03-08: Changed to no-op as it could lead
        to errors if a plugin is installed which in turn expects a regular
        pygments installation to be available (and it isn't)
"""

def find_plugin_lexers():
    return ()

def find_plugin_formatters():
    return ()

def find_plugin_styles():
    return ()

def find_plugin_filters():
    return ()
