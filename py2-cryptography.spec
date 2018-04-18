### RPM external py2-cryptography 2.2.2
## INITENV +PATH PYTHON27PATH %{i}/${PYTHON_LIB_SITE_PACKAGES}

Requires: py2-idna py2-six py2-enum34 py2-cffi py2-ipaddress py2-asn1crypto

%define pip_name cryptography

## IMPORT build-with-pip

