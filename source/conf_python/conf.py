# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------# Fix field list 

import sys
import os
import shutil
import subprocess
from docutils import nodes

project = 'CALFEM - A Finite Element Package for Python'
copyright = '2025, ...'
author = 'Per-Erik Austrell, Ola Dahlblom, Henrik Danielsson, Jonas Lindemann, Anders Olsson, Karl-Gunnar Olsson, Kent Persson, Hans Petersson, Matti Ristinmaa, Göran Sandberg, Per-Anders Wernberg'
release = '0.1'

target_lang = "python"

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
    'sphinxcontrib.rsvgconverter',
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

_rsvg_bin = shutil.which('rsvg-convert')
if not _rsvg_bin and os.path.exists('/usr/bin/rsvg-convert'):
    _rsvg_bin = '/usr/bin/rsvg-convert'

if _rsvg_bin:
    rsvg_converter_bin = _rsvg_bin
    rsvg_converter_args = ['--format=pdf']
    # Enable SVG to PDF conversion for LaTeX
    svg_converter = 'rsvg'
else:
    # Avoid noisy warnings when rsvg-convert isn't available
    if 'sphinxcontrib.rsvgconverter' in extensions:
        extensions.remove('sphinxcontrib.rsvgconverter')


_IMAGES_DIR = os.path.join(source_dir, 'images')


def _collect_latex_image_paths() -> list[str]:
    if not os.path.isdir(_IMAGES_DIR):
        return []

    image_files: list[str] = []
    for entry in os.listdir(_IMAGES_DIR):
        lower = entry.lower()
        if lower.endswith((".png", ".pdf", ".jpg", ".jpeg")):
            image_files.append(os.path.join("images", entry))
    return image_files
def _rewrite_image_nodes(app, doctree):
    if not getattr(app, "builder", None) or app.builder.name not in {"latex", "latexpdf"}:
        return

    for node in doctree.traverse(nodes.image):
        uri = node.get("uri", "")
        if not uri.startswith("images/"):
            continue
        prefix, filename = uri.split("/", 1)
        base, ext = os.path.splitext(filename)
        if ext.lower() == ".svg":
            pdf_path = os.path.join(_IMAGES_DIR, f"{base}.pdf")
            png_path = os.path.join(_IMAGES_DIR, f"{base}.png")
            if os.path.exists(pdf_path):
                filename = f"{base}.pdf"
            elif os.path.exists(png_path):
                filename = f"{base}.png"
        node["uri"] = f"{prefix}/{filename}"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_immaterial'

html_static_path = [os.path.join(source_dir, '_static')]
html_css_files = ['custom.css']

# Set the HTML title explicitly
html_title = 'CALFEM - A Finite Element Package for Python'

# Optional: Set a shorter title for the browser tab
html_short_title = 'CALFEM for Python'

html_theme_options = {

    # Set the name of the project to appear in the navigation.


    # Set the repo location to get a badge with stats
    'repo_url': 'https://github.com/CALFEM/calfem-python/',
    'repo_name': 'CALFEM for Python',

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

latex_additional_files = _collect_latex_image_paths()

\makeatletter
\renewcommand{\sphinxcode}[1]{{\footnotesize\texttt{#1}}}
\makeatother

\usepackage{graphicx}
\usepackage{amsmath}

% Allow equations to break at binary operators and relations
\allowdisplaybreaks

% Use smaller math font globally - proper way
\DeclareMathSizes{10}{8}{6}{5}   % for 10pt text: 8pt math, 6pt script, 5pt scriptscript

\usepackage{fontspec}
\usepackage{sectsty}

\allsectionsfont{\sffamily}

% — Main text (serif): TeX Gyre Pagella (Palatino-like, included in TeX Live)
\setmainfont{TeX Gyre Pagella}

% — Headings (sans-serif): TeX Gyre Heros (Helvetica-like, included in TeX Live)
\setsansfont{TeX Gyre Heros}

% — Code (monospace): TeX Gyre Cursor (included in TeX Live)
\setmonofont{TeX Gyre Cursor}


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
    'sphinxsetup': 'verbatimwithframe=false',
    'extraclassoptions': 'openany,oneside'
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


def _convert_svgs_for_latex(app):
    if app.builder.name not in {"latex", "latexpdf"}:
        return

    if not _rsvg_bin:
        return

    app.builder.supported_image_types = [
        "image/pdf",
        "image/png",
        "image/jpeg",
    ]

    for entry in os.listdir(_IMAGES_DIR):
        if not entry.lower().endswith(".svg"):
            continue
        svg_path = os.path.join(_IMAGES_DIR, entry)
        base, _ = os.path.splitext(entry)
        pdf_path = os.path.join(_IMAGES_DIR, f"{base}.pdf")
        if os.path.exists(pdf_path):
            continue
        try:
            result = subprocess.run(
                [_rsvg_bin, "--format=pdf", "-o", pdf_path, svg_path],
                check=False,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            if result.returncode != 0 or not os.path.exists(pdf_path):
                png_path = os.path.join(_IMAGES_DIR, f"{base}.png")
                subprocess.run(
                    [_rsvg_bin, "--format=png", "-o", png_path, svg_path],
                    check=False,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
        except Exception:
            pass

    extra_files = set(app.config.latex_additional_files or [])
    extra_files.update(_collect_latex_image_paths())
    app.config.latex_additional_files = sorted(extra_files)



def setup(app):
    app.connect("builder-inited", _convert_svgs_for_latex)
    app.connect("doctree-read", _rewrite_image_nodes)
