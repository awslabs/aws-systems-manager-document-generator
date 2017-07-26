import re
from glob import glob
from setuptools import setup, find_packages

data_files = []

# declare your scripts:
# scripts in bin/ with a shebang containing python will be
# recognized automatically
scripts = []
for fname in glob('bin/*'):
    with open(fname, 'r') as fh:
        if re.search(r'^#!.*python', fh.readline()):
            scripts.append(fname)


setup(name="SSMDocumentGenerator",
      version="1.0",

      # declare your packages
      packages=find_packages(where="src", exclude=("test",)),
      package_dir={"": "src"},

      # declare your scripts
      scripts=scripts,

      # include data files
      data_files=data_files,

      # set up the shebang
      options={
          # make sure the right shebang is set for the scripts - use the environment default Python
          'build_scripts': {
              'executable': '/apollo/sbin/envroot "$ENVROOT/bin/python"',
          },
      },

      # Because the live versionset ships CPython 3.4 by default, we want to add
      # its scripts to `bin/`. *If* you want a different set of scripts in bin,
      # or your versionset is configured for a different CPython, then you can
      # change this accordingly.

      # Ship the python 3.4 script in $ROOT/bin. Remove this flag to skip
      # installing scripts into $ROOT/bin/
      #
      # Note that if your versionset doesn't build for 3.4, this won't do the right thing!
      root_script_source_version="python3.4",

      # When we have something that's only for one version, use 3.4
      default_python="python3.4",

      # Use the pytest brazilpython runner. Provided by BrazilPython-Pytest-2.x
      test_command='brazilpython_pytest',

      # Use Sphinx for docs
      doc_command='build_sphinx',
)
