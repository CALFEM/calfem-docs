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
    'sphinx_immaterial',  # For Material Design theme
    'myst_parser'
]

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
    "fieldlist",
]

# Configure MathJax settings
mathjax_path = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js'

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_immaterial'

html_theme_options = {

    # Set the name of the project to appear in the navigation.


    # Set the repo location to get a badge with stats
    'repo_url': 'https://github.com/CALFEM/calfem-python/',
    'repo_name': 'CALFEM for Python',

    # If False, expand all TOC entries
    'globaltoc_collapse': True,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': False,
    #'logo_icon': "&#xe913;"
    'toc_title': 'Contents',

    'icon': {
        'repo': 'fontawesome/brands/github',
        'edit': 'material/file-edit-outline',
    }   
}

html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

#html_logo = 'images/calfem.logo.bw.svg'

#html_theme = 'alabaster'
#html_static_path = ['_static']

# -- Options for LaTeX output ------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a5paper',

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    'preamble': '',

    # Latex figure (float) alignment
    'figure_align': 'htbp',

    'sphinxsetup': r'''
        hmargin=1.5cm, 
        vmargin=2cm,
    ''',
}

# latex_logo = 'images/calfem.logo.bw.svg'
