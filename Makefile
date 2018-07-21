run: install
	jupyter notebook
install: install_server install_nb
install_server: clean
	pip install -e .
install_nb: clean
	jupyter nbextension install jupygit
	jupyter nbextension enable jupygit/index
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +