from glob import glob
import os

from notebook.base.handlers import IPythonHandler

class GitCleanHandler(IPythonHandler):

    def get(self):
        print(glob("*"))
        self.write({'status':200,'content':'Hola'})
        self.flush()