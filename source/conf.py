# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CALFEM - A Finite Element Toolbox'
copyright = '2025, ...'
author = '...'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.mathjax',   # For rendering LaTeX equations
    'sphinx.ext.autodoc',   # For auto-documentation from Python code
    'sphinx.ext.viewcode',  # For linking to source code
    'sphinx.ext.napoleon',  # For NumPy/Google style docstrings
]

# Configure MathJax settings
mathjax_path = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js'

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_material'

html_theme_options = {

    # Set the name of the project to appear in the navigation.
    'nav_title': 'CALFEM - A Finite Element Toolbox',

    # Set the color and the accent color
    'color_primary': 'blue',
    'color_accent': 'light-blue',

    # Set the repo location to get a badge with stats
    'repo_url': 'https://github.com/CALFEM/calfem-python/',
    'repo_name': 'CALFEM for Python',

    # Visible levels of the global TOC; -1 means unlimited
    'globaltoc_depth': 3,
    # If False, expand all TOC entries
    'globaltoc_collapse': True,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': False,
    #'logo_icon': "&#xe913;"
}

html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

#html_logo = 'images/calfem.logo.bw.svg'

#html_theme = 'alabaster'
#html_static_path = ['_static']
