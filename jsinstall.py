from JumpScale import j

j.do.execute("python3 setup.py build")
j.do.execute("rm -rf %s/IPython/*"%j.do.getPythonLibSystem())
j.do.execute("rm -rf %s/ipython*"%j.do.getPythonLibSystem())
j.do.copyTree("build/lib/", dest=j.do.getPythonLibSystem(), keepsymlinks = False, deletefirst = False, overwriteFiles=True,rsync=False,recursive=True)

j.do.copyFile("build/scripts-3.5/ipython3", dest=j.do.getBinDirSystem(),makeExecutable=True)
j.do.copyFile("build/scripts-3.5/ipython", dest=j.do.getBinDirSystem(),makeExecutable=True)


install_requires = [
    'decorator',
    'pickleshare',
    'simplegeneric>0.8',
    'traitlets',
]
for install in install_requires:
    j.do.execute("pip3 install %s --upgrade"%install)
