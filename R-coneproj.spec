#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-coneproj
Version  : 1.16
Release  : 9
URL      : https://cran.r-project.org/src/contrib/coneproj_1.16.tar.gz
Source0  : https://cran.r-project.org/src/contrib/coneproj_1.16.tar.gz
Summary  : Primal or Dual Cone Projections with Routines for Constrained
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-coneproj-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-RcppArmadillo
BuildRequires : R-Rcpp
BuildRequires : R-RcppArmadillo
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-coneproj package.
Group: Libraries

%description lib
lib components for the R-coneproj package.


%prep
%setup -q -c -n coneproj
cd %{_builddir}/coneproj

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640992192

%install
export SOURCE_DATE_EPOCH=1640992192
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library coneproj
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library coneproj
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library coneproj
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc coneproj || :


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
/usr/lib64/R/library/coneproj/libs/coneproj.so
/usr/lib64/R/library/coneproj/libs/coneproj.so.avx2
/usr/lib64/R/library/coneproj/libs/coneproj.so.avx512
