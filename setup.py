from setuptools import setup

DISTNAME = "ocp"
DESCRIPTION = "Open Collaboration Platform meta package"
AUTHOR = "Stefan Tröger"
AUTHOR_EMAIL = "stefantroeger@gmx.net"
URL = "https://github.com/OpenCollaborationPlatform"
LICENSE = "LGPL2.1+"
DOWNLOAD_URL = "https://github.com/OpenCollaborationPlatform"
VERSION = '0.1.5'

# dependencies. We specify the binary package version, to force an upgrade of those when this meta package is upgraded
required = [f"ocp-linux-386 >= {VERSION}; platform_system=='Linux' and platform_machine=='i386'",
            f"ocp-linux-amd64 >= {VERSION}; platform_system=='Linux' and platform_machine=='x86_64'",
            f"ocp-linux-arm >= {VERSION}; platform_system=='Linux' and platform_machine=='arm'",
            f"ocp-linux-arm64 >= {VERSION}; platform_system=='Linux' and platform_machine=='aarch64'",
            f"ocp-windows-386 >= {VERSION}; platform_system=='Windows' and platform_machine=='386'",
            f"ocp-windows-amd64 >= {VERSION}; platform_system=='Windows' and platform_machine=='AMD64'",
            f"ocp-darwin-arm64 >= {VERSION}; platform_system=='Darwin' and platform_machine=='aarch64'",
            f"ocp-darwin-amd64 >= {VERSION}; platform_system=='Darwin' and platform_machine=='x86_64'"]

# setup
setup(name=DISTNAME,
      description=DESCRIPTION,
      maintainer=AUTHOR,
      maintainer_email=AUTHOR_EMAIL,
      author=AUTHOR,
      author_email= AUTHOR_EMAIL,
      url=URL,
      license=LICENSE,
      download_url=DOWNLOAD_URL,
      version=VERSION,
      platforms='any',
      install_requires=required)

