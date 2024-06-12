#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v12
# autospec commit: fbcebd0
#
Name     : R-coneproj
Version  : 1.19
Release  : 15
URL      : https://cran.r-project.org/src/contrib/coneproj_1.19.tar.gz
Source0  : https://cran.r-project.org/src/contrib/coneproj_1.19.tar.gz
Summary  : Primal or Dual Cone Projections with Routines for Constrained
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-coneproj-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-RcppArmadillo
BuildRequires : R-Rcpp
BuildRequires : R-RcppArmadillo
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package lib
Summary: lib components for the R-coneproj package.
Group: Libraries

%description lib
lib components for the R-coneproj package.


%prep
%setup -q -n coneproj
pushd ..
cp -a coneproj buildavx2
popd
pushd ..
cp -a coneproj buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1718231018

%install
export SOURCE_DATE_EPOCH=1718231018
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/coneproj/CITATION
/usr/lib64/R/library/coneproj/DESCRIPTION
/usr/lib64/R/library/coneproj/INDEX
/usr/lib64/R/library/coneproj/Meta/Rd.rds
/usr/lib64/R/library/coneproj/Meta/data.rds
/usr/lib64/R/library/coneproj/Meta/features.rds
/usr/lib64/R/library/coneproj/Meta/hsearch.rds
/usr/lib64/R/library/coneproj/Meta/links.rds
/usr/lib64/R/library/coneproj/Meta/nsInfo.rds
/usr/lib64/R/library/coneproj/Meta/package.rds
/usr/lib64/R/library/coneproj/NAMESPACE
/usr/lib64/R/library/coneproj/R/coneproj
/usr/lib64/R/library/coneproj/R/coneproj.rdb
/usr/lib64/R/library/coneproj/R/coneproj.rdx
/usr/lib64/R/library/coneproj/data/FEV.rda
/usr/lib64/R/library/coneproj/data/TwoDamat.rda
/usr/lib64/R/library/coneproj/data/cubic.rda
/usr/lib64/R/library/coneproj/data/feet.rda
/usr/lib64/R/library/coneproj/help/AnIndex
/usr/lib64/R/library/coneproj/help/aliases.rds
/usr/lib64/R/library/coneproj/help/coneproj.rdb
/usr/lib64/R/library/coneproj/help/coneproj.rdx
/usr/lib64/R/library/coneproj/help/paths.rds
/usr/lib64/R/library/coneproj/html/00Index.html
/usr/lib64/R/library/coneproj/html/R.css

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/coneproj/libs/coneproj.so
/V4/usr/lib64/R/library/coneproj/libs/coneproj.so
/usr/lib64/R/library/coneproj/libs/coneproj.so
