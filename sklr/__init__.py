"""
Machine Learning module for Label Rankings problems in Python
=============================================================

scikit-lr is a Python module integrating Machine Learning algorithms for
Label Ranking problems in the tightly-knit world of Scientific Python
packages (NumPy and SciPy).

It aims is to provide simple and efficient solutions to Label Ranking
problems that are accessible to everybody and reusable in all contexts.
"""


# =============================================================================
# Constants
# =============================================================================

# scikit-lr package version

# PEP0440 compatible formatted version, see:
# https://www.python.org/dev/peps/pep-0440/
#
# Generic release markers:
#   - X.Y
#   - X.Y.Z   # For bugfix releases
#
# Admissible pre-release markers:
#   - X.YaN   # Alpha release
#   - X.YbN   # Beta release
#   - X.YrcN  # Release Candidate
#   - X.Y     # Final release
#
# Dev branch marker is: "X.Y.dev" or "X.Y.devN" where N is an integer.
# "X.Y.dev0" is the canonical version of "X.Y.dev".
__version__ = "0.3.dev0"


# =============================================================================
# Module public objects
# =============================================================================
__all__ = [
    "consensus",
    "datasets",
    "dummy",
    "ensemble",
    "exceptions",
    "metrics",
    "miss",
    "neighbors",
    "tree",
    "utils"
]
