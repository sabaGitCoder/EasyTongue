from setuptools import setup, Extension
import pybind11

cpp_module = Extension(
    'lexicon_engine',
    sources = ['lexicon/cpp_src/raList.cpp'],
    include_dirs = [pybind11.get_include()],
    language = 'c++',
    extra_compile_args = ['-std=c++11'],
)

setup(
    name = 'lexicon_engine',
    vers = '1.0',
    desc = 'C++ Backend for lexicon maintenance',
    ext_modules = [cpp_module], 
)