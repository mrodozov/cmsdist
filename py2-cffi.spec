### RPM external py2-cffi 1.11.5
## INITENV +PATH PYTHON27PATH %{i}/${PYTHON_LIB_SITE_PACKAGES}

Requires: py2-pycparser libffi

%define pip_name cffi
%define PipPreBuild export CFLAGS=-I${LIBFFI_ROOT}/include

## IMPORT build-with-pip

