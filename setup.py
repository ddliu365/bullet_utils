#!/usr/bin/env python

import sys
from os import path, walk
from setuptools import setup, find_packages


def print_error(*args, **kwargs):
    """ Print in stderr. """
    print(*args, file=sys.stderr, **kwargs)


def find_resources(package_name):
    """ Find the relative path of files under the resource folder. """
    resources = []
    package_dir = path.join("src", package_name)
    resources_dir = path.join(package_dir, "resources")

    for (root, _, files) in walk(resources_dir):
        for afile in files:
            if (
                afile != package_name
                and not afile.endswith(".DS_Store")
                and not afile.endswith(".py")
            ):
                rel_dir = path.relpath(root, package_dir)
                src = path.join(rel_dir, afile)
                resources.append(src)
    return resources


# provide old names for compatiblity
package_name = "bullet_utils"
package_names = [package_name, "pinocchio_bullet", "py_pinocchio_bullet"]

with open(path.join(path.dirname(path.realpath(__file__)), "readme.md"), "r") as fh:
    long_description = fh.read()

# Find the resource files.
resources = find_resources(package_name)

# Install nodes and demos.
scripts_list = []
for (root, _, files) in walk(path.join("demos")):
    for demo_file in files:
        scripts_list.append(path.join(root, demo_file))

setup(
    name=package_name,
    version="1.0.0",
    package_dir={name: path.join("src", name) for name in package_names},
    packages=package_names,
    package_data={package_name: resources},
    scripts=scripts_list,
    install_requires=["setuptools", "pybullet", "pinocchio", "importlib_resources"],
    zip_safe=True,
    maintainer="mnaveau",
    maintainer_email="mnaveau@tuebingen.mpg.de",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    description="Wrapper around the pybullet interface using pinocchio.",
    license="BSD-3-clause",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD-3-clause",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
