### RPM cms toolfiles 1.0

%define branch main
%define tag a6677f4ec02f260f6e2d2afb810f132b6fdb9ad8
%define github_user mrodozov
%define github_repo toolfiles

Source: git+https://github.com/%{github_user}/%{github_repo}.git?obj=%{branch}/%{tag}&export=%{n}-%{realversion}&output=/%{n}-%{realversion}-%{tag}.tgz

%prep
%setup -n %{n}-%{realversion}

%build

%install
cp -r %{_builddir}/%{n}-%{realversion} %{i}/%{n}
