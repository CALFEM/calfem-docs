# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------# Fix field list 

import sys
import os

project = 'CALFEM - A Finite Element Toolbox for MATLAB'
copyright = '2025, ...'
author = 'Per-Erik Austrell, Ola Dahlblom, Henrik Danielsson, Jonas Lindemann, Anders Olsson, Karl-Gunnar Olsson, Kent Persson, Hans Petersson, Matti Ristinmaa, Göran Sandberg, Per-Anders Wernberg'
release = '0.1'

target_lang = "matlab"

if target_lang == 'matlab':
    tags.add('matlab')
else:
    tags.add('python')

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx_copybutton',
    'sphinx_design',
    'sphinx_tabs.tabs',
    'sphinxcontrib.inkscapeconverter',
    'sphinx_immaterial',  # For Material Design theme
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon'
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

# Set the source directory relative to conf.py location
import os
conf_dir = os.path.dirname(__file__)
source_dir = os.path.abspath(os.path.join(conf_dir, '..'))
sys.path.insert(0, source_dir)

templates_path = [os.path.join(source_dir, '_templates')]
exclude_patterns = []

# Suppress duplicate label warnings
suppress_warnings = ['ref.duplicate']

inkscape_converter_bin = ""

if sys.platform.startswith('win'):
    # On Windows, we need to use the full path to the Inkscape executable
    # Uncomment and set the correct path if you have Inkscape installed
    inkscape_converter_bin = 'C:\\Program Files\\Inkscape\\bin\\inkscape.exe'
else:
    # On other platforms, we can use just 'inkscape' if it's in the PATH
    inkscape_converter_bin = 'inkscape'

inkscape_converter_args = ['--export-area-drawing']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_immaterial'

html_static_path = ['_static']

# Set the HTML title explicitly
html_title = 'CALFEM - A Finite Element Toolbox for MATLAB'

# Optional: Set a shorter title for the browser tab
html_short_title = 'CALFEM for MATLAB'

html_theme_options = {

    # Set the name of the project to appear in the navigation.


    # Set the repo location to get a badge with stats
    'repo_url': 'https://github.com/CALFEM/calfem-matlab/',
    'repo_name': 'CALFEM for MATLAB',

    "features": [
        # "navigation.expand",
        # "navigation.tabs",
        # "navigation.tabs.sticky",
        "navigation.sections",
        # "navigation.instant",
        # "header.autohide",
        "navigation.top",
        "navigation.footer",
        # "navigation.tracking",
        # "search.highlight",
        "search.share",
        "search.suggest",
        "toc.integrate",
        "toc.follow",
        "toc.sticky",
        "content.tabs.link",
        "content.code.copy",
        "content.action.edit",
        "content.action.view",
        "content.tooltips",
        "announce.dismiss",
    ],    

    # If False, expand all TOC entries
    
    # 'globaltoc_collapse': True,
    
    # If True, show hidden TOC entries
    
    # 'globaltoc_includehidden': False,
    
    #'logo_icon': "&#xe913;"
    
    # 'toc_title': 'Contents',

    'icon': {
        'repo': 'fontawesome/brands/github',
        'edit': 'material/file-edit-outline',
    }   
}

# Only keep search - Material theme handles navigation
html_sidebars = {
    "**": ["searchbox.html"]
}

#html_logo = 'images/calfem.logo.bw.svg'

#html_theme = 'alabaster'
#html_static_path = ['_static']

html_use_index = True

# Enable index generation for LaTeX
latex_use_index = True

# Force use of makeindex instead of xindy (which has Windows issues)
latex_use_xindy = False

# -- Options for LaTeX output ------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output

latex_engine = 'xelatex'

latex_documents = [
    ('index', 'calfem-python.tex', 'CALFEM for Python', author, 'manual'),
]

#     'makeindex': r'\usepackage{makeidx}\makeindex',    


latex_elements = {
    'papersize': '',
    'makeindex': r'\usepackage{makeidx}\makeindex',
    'printindex': r'\printindex',
    'pointsize': '10pt',
    'preamble': r"""
\geometry{
  paperwidth=170mm,
  paperheight=240mm,
  left=31mm,
  right=26mm,
  top=20mm,
  bottom=20mm
}

\makeatletter
\renewcommand{\sphinxcode}[1]{{\footnotesize\texttt{#1}}}
\makeatother


\usepackage{fontspec}
\usepackage{sectsty}

\allsectionsfont{\sffamily}

% — Main text (serif): Crimson Text (installed system-wide)
\setmainfont[
  BoldFont       = {Crimson Text Bold},
  ItalicFont     = {Crimson Text Italic},
  BoldItalicFont = {Crimson Text Bold Italic},
  Script         = Latin
]{Crimson Text}

% — Headings (sans-serif): PT Sans
\setsansfont[
  BoldFont       = {PT Sans Bold},
  ItalicFont     = {PT Sans Italic},
  BoldItalicFont = {PT Sans Bold Italic},
  Script         = Latin
]{PT Sans}

% — Code (monospace): Noto Sans Mono
%\setmonofont[
%  BoldFont   = {Noto Sans Mono},
%  Script     = Latin
%]{Noto Sans Mono}

\setmonofont{Fira Code}


% — Force all headings into PT Sans:
\chapterfont   {\sffamily\fontsize{18}{22}\selectfont}
\sectionfont   {\sffamily\fontsize{14}{16}\selectfont}
\subsectionfont{\sffamily\fontsize{12}{14}\selectfont}

\usepackage{xcolor}
\definecolor{codebg}{rgb}{0.95,0.95,0.95}

\usepackage{fancyvrb}
\usepackage{fvextra}
\usepackage{tcolorbox}
\tcbuselibrary{skins,breakable}

\makeatletter
\renewenvironment{sphinxVerbatim}[1][]{%
  \VerbatimEnvironment
  % Start the shaded, rounded box:
  \begin{tcolorbox}[
      enhanced,
      breakable,
      colback=codebg,      % fill
      colframe=codebg,     % invisible border
      boxrule=0pt,
      arc=4pt,             % rounded corners
      outer arc=4pt,
      left=0pt,right=0pt,
      top=1mm,bottom=1mm
    ]%
  % Now the actual FV code with all your options:
  \begin{Verbatim}[%
    commandchars=\\\{\},%
    framesep=4pt,%
    framerule=0pt,%
    breaklines=true,%
    breakanywhere=true,%    
    xleftmargin=4pt,%
    xrightmargin=4pt,%
    fontsize=\scriptsize,%
    #1% preserve any per‐block overrides
  ]%
}{%
  \end{Verbatim}
  \end{tcolorbox}
}
\makeatother

\usepackage{fancyhdr}

% Define custom page style
\fancypagestyle{normal}{
    \fancyhf{}
    % Headers: Chapter on left even, Section on right odd
    \fancyhead[LE]{\small\nouppercase{\leftmark}}
    \fancyhead[RO]{\small\nouppercase{\rightmark}}
    
    % Footers: Page numbers on outer edges
    \fancyfoot[LE,RO]{\thepage}
    \fancyfoot[LO,RE]{\sffamily \tiny \copyright\ Structural Mechanics and Solid Mechanics}
    
    \renewcommand{\headrulewidth}{0.4pt}
    \renewcommand{\footrulewidth}{0pt}
}

% Apply the style
\pagestyle{normal}

% Override the plain style used by chapter pages
\fancypagestyle{plain}{
    \fancyhf{}
    \fancyfoot[LE,RO]{\thepage}
    \fancyfoot[LO,RE]{\sffamily \tiny \copyright\ FÖRFATTAREN OCH STUDENTLITTERATUR}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0pt}
}

% Ensure proper chapter and section marking
\renewcommand{\chaptermark}[1]{\markboth{\chaptername\ \thechapter.\ #1}{}}
% \renewcommand{\sectionmark}[1]{\markright{\thesection.\ #1}}
\renewcommand{\sectionmark}[1]{\markright{#1}}

% Force the page style after Sphinx sets its own
\AtBeginDocument{\pagestyle{normal}}

% Fix field list alignment - remove quote indentation and add spacing between field name and description
\renewenvironment{quote}
  {\list{}{\leftmargin0pt \rightmargin0pt}\item\relax}
  {\endlist}

\makeatletter
% Redefine field list formatting
\def\sphinxfieldlistitem#1#2{%
  \item[{\sffamily\bfseries #1}] {\sffamily #2}%
}
\makeatother

\makeatletter
\renewenvironment{description}%
{\list{}{\labelwidth\z@ \itemindent-\leftmargin
         \let\makelabel\descriptionlabel}}%
{\endlist}
\renewcommand*\descriptionlabel[1]{\hspace\labelsep
                                   \sffamily\bfseries\fontsize{9}{11}\selectfont #1}

% \sffamily\bfseries #1                                   
                                   
\makeatother

""",
    #'fvset': r"""\fvset{frame=none, framerule=0pt, framesep=20pt, xleftmargin=0pt, xrightmargin=0pt, fontsize=\scriptsize}""",
    'figure_align': 'htbp',
    'sphinxsetup': 'verbatimwithframe=false'
}


# latex_elements = {
#     # The paper size ('letterpaper' or 'a4paper').
#     'papersize': 'a5paper',

#     # The font size ('10pt', '11pt' or '12pt').
#     'pointsize': '10pt',

#     # Additional stuff for the LaTeX preamble.
#     'preamble': '',

#     # Latex figure (float) alignment
#     'figure_align': 'htbp',

#     'sphinxsetup': r'''
#         hmargin=1.5cm, 
#         vmargin=2cm,
#     ''',
# }

# latex_logo = 'images/calfem.logo.bw.svg'
