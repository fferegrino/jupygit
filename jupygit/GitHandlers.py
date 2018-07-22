from glob import glob
from urllib.parse import parse_qs
import os

from notebook.base.handlers import IPythonHandler

class GitCleanHandler(IPythonHandler):

    file_suffix = "*-jupygit___.ipynb"

    def get(self):
        data = parse_qs(self.request.query)
        
        self.add_gitignore_entry(os.path.dirname(data["path"][0]))

        self.write({'status':200,'content':'Hola'})
        self.flush()

    def add_gitignore_entry(self, path):
        gitignore_path = os.path.join(path,".gitignore")
        if not os.path.exists(gitignore_path):
            with open(gitignore_path, "w") as w:
                w.write("# jupygit file \"extension\"\n")
                w.write(self.file_suffix)
        else:
            with open(gitignore_path, "r") as r:
                entries = set([s.strip() for s in r.readlines()])
            if self.file_suffix not in entries:
                with open(gitignore_path, "a") as w:
                    w.write("\n# jupygit file \"extension\"\n")
                    w.write(self.file_suffix)    