### RPM cms toolfiles 1.0

%define branch main
%define tag c7ee117554b97e9bed06ae7be4e07c956cbd3dce
%define github_user mrodozov
%define github_repo toolfiles

Source: git+https://github.com/%{github_user}/%{github_repo}.git?obj=%{branch}/%{tag}&export=%{n}-%{realversion}&output=/%{n}-%{realversion}-%{tag}.tgz

%prep
%setup -n %{n}-%{realversion}

%build

%install
cp -r %{_builddir}/%{n}-%{realversion} %{i}/%{n}
