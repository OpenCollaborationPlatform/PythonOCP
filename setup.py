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
      packages=["packagename"],

      # Include pre-compiled extension
      package_data={"packagename": ["_precompiled_extension.pyd"]},
      distclass=BinaryDistribution)
