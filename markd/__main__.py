"""
DO NOT REMOVE THIS
"""

import sys
import os

PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), './main'))
if not PATH in sys.path:
    sys.path.insert(1, PATH)
    from .main.markd import Markdown
del PATH



if __name__ == '__main__':
    sys.exit(Markdown())
