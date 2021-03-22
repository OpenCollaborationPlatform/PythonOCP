from setuptools import setup
from version import __version__


# dependencies. We specify the binary package version, to force an upgrade of those when this meta package is upgraded
required = [f"ocp-linux-386 >= {__version__}; platform_system=='Linux' and platform_machine=='i386'",
            f"ocp-linux-amd64 >= {__version__}; platform_system=='Linux' and platform_machine=='x86_64'",
            f"ocp-linux-arm >= {__version__}; platform_system=='Linux' and platform_machine=='arm'",
            f"ocp-linux-arm64 >= {__version__}; platform_system=='Linux' and platform_machine=='aarch64'",
            f"ocp-windows-386 >= {__version__}; platform_system=='Windows' and platform_machine=='386'",
            f"ocp-windows-amd64 >= {__version__}; platform_system=='Windows' and platform_machine=='AMD64'",
            f"ocp-darwin-arm64 >= {__version__}; platform_system=='Darwin' and platform_machine=='aarch64'",
            f"ocp-darwin-amd64 >= {__version__}; platform_system=='Darwin' and platform_machine=='x86_64'"]

# setup
setup(name="ocp",
      description="Open Collaboration Platform meta package",
      maintainer="Stefan Tröger",
      maintainer_email="stefantroeger@gmx.net",
      author="Stefan Tröger",
      author_email= "stefantroeger@gmx.net",
      url="https://github.com/OpenCollaborationPlatform",
      license="LGPL2.1+",
      download_url="https://github.com/OpenCollaborationPlatform/PythonOCP",
      version=__version__,
      platforms='any',
      install_requires=required)

