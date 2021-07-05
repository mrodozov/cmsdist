### RPM cms toolfiles 1.0

%define branch main
%define tag 08476d9d98a89ec7c115793f8b7fbb7a0e16c99c
%define github_user mrodozov
%define github_repo toolfiles

Source: git+https://github.com/%{github_user}/%{github_repo}.git?obj=%{branch}/%{tag}&export=%{n}-%{realversion}&output=/%{n}-%{realversion}-%{tag}.tgz

%prep
%setup -n %{n}-%{realversion}

%build

%install
cp -r %{_builddir}/%{n}-%{realversion} %{i}/%{n}
