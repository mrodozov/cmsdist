### RPM cms toolfiles 1.0

%define branch main
%define tag b084843fdeca68156d707b7610ea0c357b103487
%define github_user mrodozov
%define github_repo toolfiles

Source: git+https://github.com/%{github_user}/%{github_repo}.git?obj=%{branch}/%{tag}&export=%{n}-%{realversion}&output=/%{n}-%{realversion}-%{tag}.tgz

%prep
%setup -n %{n}-%{realversion}

%build

%install
cp -r %{_builddir}/%{n}-%{realversion} %{i}/%{n}
