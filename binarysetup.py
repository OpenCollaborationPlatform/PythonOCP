# setup.py file that installs binary data only
#
# It searches the compiled OCP node, derives the OS and Arch from it 
# and generates a data only wheel with this binary included.
#
# This setup method is intended to be used with the github action, that builds 
# and names the executables accordingly

import os, re
from setuptools import setup
from shutil import copy2
from version import __version__

DESCRIPTION = "Open Collaboration Platform binary package"
MAINTAINER = "Stefan Troeger"
MAINTAINER_EMAIL = "stefantroeger@gmx.net"
URL = "https://github.com/OpenCollaborationPlatform"
LICENSE = "LGPL2.1+"
DOWNLOAD_URL = "https://github.com/OpenCollaborationPlatform"
VERSION = '0.1.5'

# find the build collaboration executable, independent of extension
pyfolder = os.path.dirname(__file__)
ocpfolder = os.path.join(os.path.dirname(pyfolder), "OCP")
regex = re.compile('OCP*')
filepath = ""
for root, dirs, files in os.walk(ocpfolder):
  for file in files:
    if regex.match(file):
       filepath = os.path.join(ocpfolder, file)
       break
   
# name it according to the platform details, and copy into ocp folder
extension = os.path.splitext(filepath)[1]
goos = os.getenv("GOOS", default=None)
goarch = os.getenv("GOARCH", default=None)
if not( goos and goarch):
    raise Exception("GOOS and GOARCH need to be defined as environment variables")

name = f"ocp_{goos}_{goarch}"
os.rename(filepath, os.path.join(os.curdir, "ocp", name+extension))

# setup
setup(name=name,
      description="Open Collaboration Platform binary node package",
      maintainer="Stefan Tröger",
      maintainer_email="stefantroeger@gmx.net",
      author="Stefan Tröger",
      author_email="stefantroeger@gmx.net",
      url="https://github.com/OpenCollaborationPlatform",
      license=LICENSE,
      download_url="https://github.com/OpenCollaborationPlatform/PythonOCP",
      platforms=[name.split("_")[1]],
      version=__version__,
      packages= ['ocp'],
      package_data = {'': [name+extension]})
