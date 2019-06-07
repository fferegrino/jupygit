# jupygit 

Clean git version control forr Jupyter Notebooks

Thanks to [this tutorial](https://jupyterlab.readthedocs.io/en/stable/developer/xkcd_extension_tutorial.html)


## Prerequisites

* JupyterLab

## Installation

```bash
jupyter labextension install jupygit-lab
```

## Development

For a development install (requires npm version 4 or later), do the following in the repository directory:

```bash
npm install
npm run build
jupyter labextension link .
```

To rebuild the package and the JupyterLab app:

```bash
npm run build
jupyter lab build
```

