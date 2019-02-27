from setuptools import setup, find_packages
setup(
    name="docxLinks2Bibtex",
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    packages=find_packages(exclude=["^\."]),
    exclude_package_data={'': ["Readme.md"]},
    install_requires=["python-docx>=0.8.6"],
    python_requires=">=2.7",
    dependency_links=["git+https://github.com/wachtlerlab/btmorph_v2.git",
                      "git+https://github.com/dEvasEnApati/pyVaa3d.git"]


    )