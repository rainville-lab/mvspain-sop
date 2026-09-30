# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

from sphinx_gallery.sorting import FileNameSortKey

sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), os.path.pardir, os.path.pardir)))
from docs import __version__


# -- Project information -----------------------------------------------------

project = "MVS Pain SOP"
copyright = "2026, LaNeP3"
author = "LaNeP3"


# The short X.Y version
version = __version__
# The full version, including alpha/beta/rc tags
release = __version__
package = "MVS Pain SOP"
gh_url = "https://github.com/rainville-lab/mvspain-sop"

# -- General configuration ---------------------------------------------------

needs_sphinx = "2.0"  # based on setup.cfg requirements

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.import sphinx_rtd_theme  # noqa

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "myst_parser",
    "numpydoc",
    "sphinxarg.ext",
    "sphinxcontrib.bibtex",
    "sphinxcontrib.apidoc",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_gallery.gen_gallery",
    "sphinx_issues",
]


numpydoc_show_class_members = False
autoclass_content = "class"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]

# Sphinx will warn about all references where the target cannot be found.
nitpicky = True
nitpick_ignore = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = "furo"
html_show_sourcelink = False
html_show_sphinx = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named 'default.css' will overwrite the builtin 'default.css'.
html_static_path = ["_static"]
html_css_files = [
    "css/style.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css",
]

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "mvspain-sop"

# -- intersphinx -------------------------------------------------------------
intersphinx_mapping = {
    "nibabel": ("https://nipy.org/nibabel/", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "python": ("https://docs.python.org/3", None),
}
intersphinx_timeout = 5

# -- sphinx-issues -----------------------------------------------------------
issues_github_path = gh_url.split("https://github.com/")[-1]

# -- autosectionlabels -------------------------------------------------------
autosectionlabel_prefix_document = True

# -- Options for myst_parser -------------------------------------------------
myst_enable_extensions = ["colon_fence"]

# -- sphinxcontrib-bibtex ----------------------------------------------------
bibtex_bibfiles = []

# -- numpydoc ----------------------------------------------------------------
numpydoc_class_members_toctree = False
numpydoc_attributes_as_param_list = False

# x-ref
numpydoc_xref_param_type = True
numpydoc_xref_aliases = {
    # Matplotlib
    "Axes": "matplotlib.axes.Axes",
    "Figure": "matplotlib.figure.Figure",
    # Nibabel
    "Nifti1Image": "nibabel.nifti1.Nifti1Image",
    # Numpy
    "array": "numpy.ndarray",
    # Python
    "bool": ":class:`python:bool`",
    "Path": "pathlib.Path",
    "TextIO": "io.TextIOBase",
}
numpydoc_xref_ignore = {
    "of",
    "optional",
    "or",
    "shape",
}

# validation
# https://numpydoc.readthedocs.io/en/latest/validation.html#validation-checks
error_ignores = {
    "GL01",  # docstring should start in the line immediately after the quotes
    "EX01",  # section 'Examples' not found
    "ES01",  # no extended summary found
    "SA01",  # section 'See Also' not found
    "RT02",  # The first line of the Returns section should contain only the type, unless multiple values are being returned  # noqa
}
numpydoc_validate = True
numpydoc_validation_checks = {"all"} | set(error_ignores)
numpydoc_validation_exclude = {  # regex to ignore during docstring check
    r"\.__getitem__",
    r"\.__contains__",
    r"\.__hash__",
    r"\.__mul__",
    r"\.__sub__",
    r"\.__add__",
    r"\.__iter__",
    r"\.__div__",
    r"\.__neg__",
}

# -- sphinx-gallery ----------------------------------------------------------
sphinx_gallery_conf = {
    "backreferences_dir": "generated/backreferences",
    "doc_module": (f"{package}",),
    "examples_dirs": [],  # ["../tutorials"],
    "exclude_implicit_doc": {},  # set
    "filename_pattern": r"\d{2}_",
    "gallery_dirs": [],  # ["generated/tutorials"],
    "line_numbers": False,
    "plot_gallery": True,
    "reference_url": {f"{package}": None},
    "remove_config_comments": True,
    "show_memory": True,
    "within_subsection_order": FileNameSortKey,
}

# -- Final Setup -------------------------------------------------------------


# https://github.com/rtfd/sphinx_rtd_theme/issues/117
# launch setup
def setup(app):  # noqa
    app.add_css_file("theme_overrides.css")
    app.add_js_file("https://cdn.rawgit.com/chrisfilo/zenodo.js/v0.1/zenodo.js")