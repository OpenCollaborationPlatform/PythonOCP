import os, re
from setuptools import setup
from setuptools.dist import Distribution

DISTNAME = "ocp"
DESCRIPTION = "Open Collaboration Platform"
MAINTAINER = "Stefan Troeger"
MAINTAINER_EMAIL = "stefantroeger@gmx.net"
URL = ""
LICENSE = "LGPL2.1+"
DOWNLOAD_URL = ""
VERSION = '0.1'


# find the installed collaboration executable, independent of extension
path = os.path.join(os.environ["GOPATH"], "bin")
regex = re.compile('OCP*')
filepath = ""
for root, dirs, files in os.walk(path):
  for file in files:
    if regex.match(file):
       filepath = os.path.join(path, file)
       break

# enforce os specific package
class BinaryDistribution(Distribution):
    """Distribution which always forces a binary package with platform name"""
    def has_ext_modules(self):
        return True

setup(name=DISTNAME,
      description=DESCRIPTION,
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      url=URL,
      license=LICENSE,
      download_url=DOWNLOAD_URL,
      version=VERSION,
      packages=["ocp"],
      data_files =[("ocp", [filepath])],
      distclass=BinaryDistribution)
