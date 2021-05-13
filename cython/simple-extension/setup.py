from distutils.core import setup
from Cython.Build import cythonize

# useImportHeuristic
setup(
    ext_modules=cythonize("cyt_module.pyx"),
)
