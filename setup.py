import fnmatch
import os
import platform

import setuptools

target = platform.system().lower()
PLATFORMS = {"windows", "linux", "darwin", "cygwin"}
for known in PLATFORMS:
    if target.startswith(known):
        target = known


def run_setup():
    extra_compile_args = {
        "windows": ["/DANTLR4CPP_STATIC", "/Zc:__cplusplus"],
        "linux": ["-std=c++11"],
        "darwin": ["-std=c++11"],
        "cygwin": ["-std=c++11"],
    }

    # Define an Extension object that describes the Antlr accelerator
    parser_ext = setuptools.Extension(
        # Extension name shall be at the same level as the sa_tsql_parser.py module
        name="speedy_tsql.grammar.sa_tsql_cpp_parser",
        # Add the Antlr runtime source directory to the include search path
        include_dirs=["src/speedy_tsql/grammar/cpp_src/antlr4-cpp-runtime"],
        # Rather than listing each C++ file (Antlr has a lot!), discover them automatically
        sources=get_files("src/speedy_tsql/grammar/cpp_src", "*.cpp"),
        depends=get_files("src/speedy_tsql/grammar/cpp_src", "*.h"),
        extra_compile_args=extra_compile_args.get(target, []),
    )
    ext_modules = [parser_ext]

    # Define a package
    setuptools.setup(  # TODO: Remove redundant data already defined in other config files
        name="speedy_antlr_cookiecutter",
        version="1.0.0",
        description="Speedy pytsql dummy project",
        packages=setuptools.find_packages("src"),
        package_dir={"": "src"},
        include_package_data=True,
        install_requires=[
            "antlr4-python3-runtime == 4.9.3",
        ],
        ext_modules=ext_modules,
    )


def get_files(path, pattern):
    matches = []
    for root, _, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, pattern):
            matches.append(os.path.join(root, filename))
    return matches


run_setup()
