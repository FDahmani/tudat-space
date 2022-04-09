#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# tudat.space documentation build configuration file, created by
# sphinx-quickstart on Sat Jul 18 15:13:31 2020.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.doctest',
              'sphinx.ext.intersphinx',
              'sphinx.ext.todo',
              'sphinx.ext.coverage',
              'sphinx.ext.mathjax',
              'sphinx.ext.viewcode',
              'sphinx.ext.autosectionlabel',
              'sphinx_panels',  # for gridded panels
              'nbsphinx',  # to embed Jupyter notebooks
              'IPython.sphinxext.ipython_console_highlighting',  # to have pygments in rendered notebooks
              'sphinx_gallery.load_style',  # to show notebooks as galleries
              # theme
              'sphinx_rtd_theme',
              'sphinx_tabs.tabs',
              'sphinx_copybutton',
              'sphinxcontrib.contentui'
              ]

sphinx_tabs_valid_builders = ['linkcheck']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Prolog/epilog to Jupyter notebooks

nbsphinx_prolog = """
.. note::
    Generated by nbsphinx_ from a Jupyter_ notebook. All the examples as Jupyter notebooks are available in the 
    tudatpy-examples repo_.
    
    .. _nbsphinx: https://nbsphinx.readthedocs.io/
    .. _Jupyter: https://jupyter.org/
    .. _repo: https://github.com/tudat-team/tudatpy-examples
"""
# This option prevents from re-executing the notebooks. The content stored from the latest execution will be displayed.
nbsphinx_execute = 'never'
# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'tudat.space'
copyright = '2022, Tudat Space'
author = 'Tudat Space'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = '0.3.1.dev0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
import sphinx_rtd_theme

html_theme = 'sphinx_rtd_theme'

# import rtcat_sphinx_theme

# html_theme = 'rtcat_sphinx_theme'
# html_theme_path = [rtcat_sphinx_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {'collapse_navigation': False,
                      'sticky_navigation': True,
                      'navigation_depth': 6,
                      'includehidden': True,
                      'titles_only': True}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "custom.css" will overwrite the builtin "custom.css".
html_static_path = ['_static']

#

# Load stylesheet to set maximum width in html pages
html_css_files = [
    'custom.css',
]
#
# def setup(app):
#     app.add_css_file('custom.css')

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}
html_logo = "_static/cover.png"

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'tudatspacedoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'tudatspace.tex', 'tudat.space Documentation',
     'ggarrett13', 'manual'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'tudatspace', 'tudat.space Documentation',
     [author], 1)
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'tudatspace', 'tudat.space Documentation',
     author, 'tudatspace', 'One line description of project.',
     'Miscellaneous'),
]

# Example configuration for intersphinx: refer to the Python standard library.
# test / view content of inventory file at url via $ python -msphinx.ext.intersphinx <url>
intersphinx_mapping = {'tudatpy': ('https://tudatpy.readthedocs.io/en/latest/', None),
                       'python': ('https://docs.python.org/', None)}
