# CALFEM Documentation

Documentation sources for the CALFEM Python and MATLAB manuals.

The documentation is built with Sphinx from the files in `source/`. Separate
Sphinx configurations are used for the Python and MATLAB manuals:

- Python: `source/conf_python/conf.py`
- MATLAB: `source/conf_matlab/conf.py`

Build output is written below `build/`.

## Prerequisites

Install Conda or Mamba first. The examples below use Conda, but the same
commands work with Mamba by replacing `conda` with `mamba`.

For PDF/LaTeX builds you also need:

- A LaTeX distribution with `xelatex` and `latexmk`, for example MiKTeX on
  Windows or TeX Live on Linux/macOS.
- The fonts used by the LaTeX configuration: Crimson Text, PT Sans, and
  Fira Code.
- `rsvg-convert` for converting SVG figures to PDF during LaTeX builds. The
  environment below installs this through the conda-forge `librsvg` package.

## Create the Sphinx Environment

Create a conda-forge environment named `sphinx-env`:

```powershell
conda create -n sphinx-env -c conda-forge python=3.11 pip make librsvg
conda activate sphinx-env
```

Install the Python documentation dependencies:

```powershell
pip install -r requirements.txt
```

Check that Sphinx is available:

```powershell
sphinx-build --version
```

## Check Out the Repository

Clone the repository and enter the checkout:

```powershell
git clone <repository-url> calfem-docs
cd calfem-docs
conda activate sphinx-env
```

If you already have the repository, update your checkout instead:

```powershell
git pull
conda activate sphinx-env
```

## Build HTML Documentation

On Windows, use the provided batch files:

```powershell
.\make-python.bat html
.\make-matlab.bat html
```

Or build both manuals:

```powershell
.\make-all.bat html
```

The generated HTML entry points are:

- `build/python/html/index.html`
- `build/matlab/html/index.html`

## Build LaTeX and PDF Documentation

Build the PDF manuals with:

```powershell
.\make-python.bat latexpdf
.\make-matlab.bat latexpdf
```

Or build both PDF manuals:

```powershell
.\make-all.bat latexpdf
```

The generated PDF files are written below:

- `build/python/latex/`
- `build/matlab/latex/`

To generate only the LaTeX source files, use the `latex` target:

```powershell
.\make-python.bat latex
.\make-matlab.bat latex
```

## Direct Sphinx Commands

The batch files are thin wrappers around `sphinx-build`. These direct commands
are useful on Linux/macOS or when debugging a build:

```bash
sphinx-build -M html source build/python -c source/conf_python -t python
sphinx-build -M html source build/matlab -c source/conf_matlab -t matlab
```

For PDF builds:

```bash
sphinx-build -M latexpdf source build/python -c source/conf_python -t python
sphinx-build -M latexpdf source build/matlab -c source/conf_matlab -t matlab
```

## Useful Build Targets

List available Sphinx targets:

```powershell
.\make-python.bat
.\make-matlab.bat
```

Common targets include:

- `html` - build HTML documentation.
- `latex` - generate LaTeX source files.
- `latexpdf` - generate LaTeX source files and compile PDFs.
- `clean` - remove generated files for that manual.

## Troubleshooting

If `sphinx-build` is not found, activate the environment and reinstall the
requirements:

```powershell
conda activate sphinx-env
pip install -r requirements.txt
```

If PDF builds fail because `xelatex` or `latexmk` is missing, install or repair
your LaTeX distribution and make sure its binaries are on `PATH`.

If SVG conversion fails during a PDF build, check that `rsvg-convert` is
available:

```powershell
rsvg-convert --version
```
