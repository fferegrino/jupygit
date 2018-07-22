run: install
	jupyter notebook
install: clean
	pip install -e .
	jupyter serverextension enable --py jupygit --sys-prefix
	jupyter nbextension install --py jupygit --sys-prefix
	jupyter nbextension enable --py jupygit --sys-prefix
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +