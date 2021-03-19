# setup.py file that installs binary data only
#
# It searches the compiled OCP node, derives the OS and Arch from it 
# and generates a data only wheel with this binary included.
#
# This setup method is intended to be used with the github action, that builds 
# and names the executables accordingly

import os, re
from setuptools import setup
from setuptools.dist import Distribution

DISTNAME = "ocp"
DESCRIPTION = "Open Collaboration Platform binary package"
MAINTAINER = "Stefan Troeger"
MAINTAINER_EMAIL = "stefantroeger@gmx.net"
URL = "https://github.com/OpenCollaborationPlatform"
LICENSE = "LGPL2.1+"
DOWNLOAD_URL = "https://github.com/OpenCollaborationPlatform"
VERSION = '0.1.2'


# find the installed collaboration executable, independent of extension
pyfolder = os.path.dirname(__file__)
ocpfolder = os.path.join(os.path.dirname(pyfolder), "OCP")
regex = re.compile('ocp_*')
filepath = ""
for root, dirs, files in os.walk(ocpfolder):
  for file in files:
    if regex.match(file):
       filepath = os.path.join(ocpfolder, file)
       break
   
#get the full name of the compiled binary and use as project name
base = os.path.basename(filepath)
name = os.path.splitext(base)[0]
DISTNAME = name

setup(name=DISTNAME,
      description=DESCRIPTION,
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      url=URL,
      license=LICENSE,
      download_url=DOWNLOAD_URL,
      version=VERSION,
      data_files =[("ocp", [filepath])])
