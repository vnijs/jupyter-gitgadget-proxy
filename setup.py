import setuptools
from os import path


# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setuptools.setup(
    name="jupyter-gitgadget-proxy",
    version="0.1.0",
    url="https://github.com/vnijs/jupyter-gitgadget-proxy",
    author="Vincent Nijs",
    description="vnijs@ucsd.edu",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=[
        "jupyter notebook",
        "gitgadget",
        "jupyterhub",
        "jupyterlab",
        "jupyter-server-proxy",
    ],
    classifiers=["Framework :: Jupyter"],
    install_requires=["jupyter-server-proxy>=1.5.0"],
    entry_points={
        "jupyter_serverproxy_servers": [
            "gitgadget = jupyter_gitgadget_proxy:setup_gitgadget",
        ]
    },
    package_data={
        "jupyter_gitgadget_proxy": ["icons/gitgadget.svg"],
    },
)
