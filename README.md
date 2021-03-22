# PythonOCP
Python package providing the OCP node binary. 

```
pip install ocp
```

## Howto use the package
The package currently only provides the path to the executable file
   
``` python
import ocp 
ocp.node_path
```

The user can use this path than together with syscalls to initialize and startup the OCP node. For this use the default ocp node cli.

## Package Structure
The users need the compiled binary executable, which than can be executed by sys calls for node setup. This means the python package needs to be platform (Linux, Windows...) and architecture (386, amd64...) specific. If python wheels are build as platform specific one runs into problems with linux distributions, as there only the manylinux spec is supported, which adds quite some overhead. To avoid this problem PythonOCP creates a package for each platform, names after the platform itself. Additionally there is a meta package called "ocp" that has no own code or data files, but depends on the platform specific packages. This way a user can always install ocp package only and automatically gets the requiered platform specific package.

## Build
The packages are build and uploaded to PyPi by a github action, that starts for a new release in this repository. It is possible to trigger the action manual.
