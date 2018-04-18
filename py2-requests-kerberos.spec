### RPM external py2-requests-kerberos 0.12.0
## INITENV +PATH PYTHON27PATH %{i}/${PYTHON_LIB_SITE_PACKAGES}

Requires: py2-requests py2-kerberos py2-cryptography

%define pip_name requests-kerberos

## IMPORT build-with-pip

