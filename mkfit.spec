### RPM external mkfit 2.0.0
%define tag V2.0.0-1+pr237
%define branch devel
%define github_user trackreco

Source: git+https://github.com/%{github_user}/%{n}.git?obj=%{branch}/%{tag}&export=%{n}-%{realversion}&output=/%{n}-%{realversion}.tgz
Requires: tbb

Patch0: mkfit-non-intel-fix

%prep
%setup -q -n %{n}-%{realversion}

%ifarch ppc64le
export header_name="htmintrin.h"
%endif
%ifarch aarch64
export header_name="arm_neon.h"
%endif

%ifnarch x86_64
%patch0 -p1
export header_location=$(find  `echo | gcc -E -Wp,-v - 2>&1 | grep -v ignoring | grep -v "#include" | head -1` -name $header_name )
cp ${header_location} %{_builddir}/%{n}-%{realversion}/immintrin.h
%endif

%build

%ifarch x86_64
make TBB_PREFIX=$TBB_ROOT VEC_GCC="-march=core2"
%endif
%ifarch aarch64
make TBB_PREFIX=$TBB_ROOT VEC_GCC="-march=native"
%endif
%ifarch ppc64le
make TBB_PREFIX=$TBB_ROOT VEC_GCC="-mcpu=native"
%endif

%install
mkdir %{i}/include %{i}/include/mkFit %{i}/Geoms
cp -a *.h %{i}/include
cp -a mkFit/*.h %{i}/include/mkFit
cp -a Geoms/*.so %{i}/Geoms
cp -ar lib %{i}/lib
