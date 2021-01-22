from setuptools import setup, find_packages


base_packages = [
    "rasa>=2.2.0",
    "fasttext>=0.9.2",
    "bpemb>=0.3.2",
    "gensim>=3.8.3",
    "rich>=9.2.0",
    "pandas>=1.0.5",
]

dev_packages = [
    "flake8>=3.6.0",
    "black>=19.10b0",
    "pre-commit>=2.5.1",
    "pytype>=2020.0.0",
    "pytest==4.0.2",
    "pytest-xdist==1.32.0",
    "mkdocs>=1.1",
    "mkdocs-material>=4.6.3",
    "pymdown-extensions>=7.1",
]

stanza_deps = [
    "stanza>=1.1.1",
]

thai_deps = [
    "pythainlp>=2.2.3",
]

setup(
    name="rasa_nlu_examples",
    version="0.2.1",
    packages=find_packages(exclude=["notebooks"]),
    install_requires=base_packages,
    extras_require={
        "dev": dev_packages,
        "all": dev_packages + stanza_deps + thai_deps,
        "thai": base_packages + thai_deps,
        "stanza": base_packages + stanza_deps,
    },
)
