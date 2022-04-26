import os
import re
import subprocess

from compilers.Compiler import Compiler
from config.Config import Config


class MasmCompiler(Compiler):

    def __init__(self, args=None, aargs=None, arch="x64"):
        # self.vcvarsall = self.config.get_path("COMPILERS", "VCVARSALL")
        super().__init__(None, args=args, aargs=aargs, sep=":", arch=arch)
        # self.prefix_cmd = f'"{self.vcvarsall}" {self.arch}'

    def default_args(self, outfile):
        self.args = {
            "/c": None,
            "/nologo": None,
            "/Zi": None,
            f'/Fo"{outfile}"': None,
            "/W3": None,
            "/errorReport": "prompt"
        }

    def set_entry(self, entry):
        self.aargs += f" /entry:{entry}"

    def set_link_only(self):
        self.aargs += " /link"

    def set_output_file(self, file):
        if file.endswith(".exe"):
            self.args[f'/Fe"{file}"'] = None
            self.args[f'/Fo"{file}.obj"'] = None
        else:
            self.args[f'/Fo"{file}"'] = None

    def add_include_directory(self, directory):
        self.args[f"/I\"{directory}\""] = None

    def set_libraries(self, libs: list):
        pass

    def set_debug(self):
        pass
