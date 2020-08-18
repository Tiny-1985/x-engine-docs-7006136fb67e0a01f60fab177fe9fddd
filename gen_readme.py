#!/Users/zk/anaconda3/bin/python3

from pathlib import Path
from os.path import join, isfile,basename
from pathlib import Path
from distutils.dir_util import copy_tree
import subprocess
import shutil
import os
import sys
import glob


tmplt = """
# {module_name}
{root_readme}
# h5
{h5_readme}

# iOS
{ios_readme}

# android
{android_readme}

"""


class ReadmeAggregator():

    def __init__(self,path,outputDir):
        self.path              = path
        self.module_short_name = self.path.split("-")[-1]
        self.outputDir         = outputDir

    def readReadMe(self,subpath):
        path = join(self.path,subpath,"readme.md")
        path = path if os.path.isfile(path) else join(self.path,subpath,"README.md")
        path = path if os.path.isfile(path) else join(self.path,subpath,"Readme.md")
        path = path if os.path.isfile(path) else join(self.path,subpath,"ReadMe.md")
        if os.path.isfile(path):
            return Path(path).read_text()
        return ""

    
    def gen_root(self):
        return self.readReadMe(".")

    def gen_h5(self):
        return self.readReadMe("h5")

    def gen_iOS(self):
        return self.readReadMe("iOS")

    def gen_android(self):
        return self.readReadMe("android")
    
    def handle_img(self):
        pass
    def get_short_module_name(self):
        return self.module_short_name

    def output_path(self):
        return join(self.outputDir,"组件-"+self.module_short_name+".md")


    def gen(self):
        root_readme    = self.gen_root()
        h5_readme      = self.gen_h5()
        ios_readme     = self.gen_iOS()
        android_readme = self.gen_android()

        content = tmplt.format(module_name = self.module_short_name,root_readme = root_readme,h5_readme = h5_readme, ios_readme = ios_readme, android_readme = android_readme)
        with open(self.output_path(),"w") as f:
            f.write(content)
        # gen _sidebar.md
        with open(join(self.outputDir,"_sidebar.md"),"a") as f:
            f.write(f"- [{self.module_short_name}](./docs/modules/all/组件-{self.module_short_name}.md)\n")
        print(f'{self.module_short_name}')


if __name__ == "__main__":

    outputDir = "./docs/modules/all"
    with open(join(outputDir,"_sidebar.md"),"w") as f:
        f.write("")

    arr = os.listdir("..")
    for d in arr:
        if d.startswith(".") or d.endswith("docs") or "template" in d:
            continue
        # print(d)

 
        path = "../"+d
        # subprocess.Popen(["python3",before_script]).communicate()
        r = ReadmeAggregator(path,outputDir)
        r.gen()




