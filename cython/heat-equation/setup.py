from distutils.core import setup, Extension
from Cython.Build import cythonize

setup(
     ext_modules=cythonize("heat.pyx"),
     compiler_directives={'language_level' : "3"},
)
