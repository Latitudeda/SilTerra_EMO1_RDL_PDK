# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'SilTerra EMO1 RDL PDK Documentation'
copyright = '2025, Latitudeds.com'
author = 'www.latitudeds.com'

release = '11.0'
version = '11.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

latex_elements = {
  'extraclassoptions': 'openany,oneside'
}

# -- Options for EPUB output
epub_show_urls = 'footnote'

html_theme_options = {
    'navigation_depth': 5,
    'collapse_navigation': False,
}
