from notebook.utils import url_path_join

from .GitHandlers import GitCleanHandler

def load_jupyter_server_extension(nb_server_app):
    web_app = nb_server_app.web_app
    host_pattern = '.*$'
    web_app.add_handlers(host_pattern, [
        (url_path_join(web_app.settings['base_url'], r'/git/clean'),
         GitCleanHandler)
    ])

def _jupyter_server_extension_paths():
    return [{
        "module": "jupygit"
    }]