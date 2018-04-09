#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-gplots
Version  : 3.0.1
Release  : 4
URL      : https://cran.r-project.org/src/contrib/gplots_3.0.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/gplots_3.0.1.tar.gz
Summary  : Various R Programming Tools for Plotting Data
Group    : Development/Tools
License  : GPL-2.0
Requires: R-caTools
Requires: R-gdata
Requires: R-gtools
BuildRequires : R-caTools
BuildRequires : R-gdata
BuildRequires : R-gtools
BuildRequires : clr-R-helpers

%description
- calculating and plotting locally smoothed summary function as
    ('bandplot', 'wapply'),
  - enhanced versions of standard plots ('barplot2', 'boxplot2',
    'heatmap.2', 'smartlegend'),
  - manipulating colors ('col2hex', 'colorpanel', 'redgreen',
    'greenred', 'bluered', 'redblue', 'rich.colors'),
  - calculating and plotting two-dimensional data summaries ('ci2d',
    'hist2d'),
  - enhanced regression diagnostic plots ('lmplot2', 'residplot'),

%prep
%setup -q -c -n gplots

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523306637

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523306637
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gplots
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gplots
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gplots
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library gplots|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/gplots/ChangeLog
/usr/lib64/R/library/gplots/DESCRIPTION
/usr/lib64/R/library/gplots/INDEX
/usr/lib64/R/library/gplots/Meta/Rd.rds
/usr/lib64/R/library/gplots/Meta/data.rds
/usr/lib64/R/library/gplots/Meta/features.rds
/usr/lib64/R/library/gplots/Meta/hsearch.rds
/usr/lib64/R/library/gplots/Meta/links.rds
/usr/lib64/R/library/gplots/Meta/nsInfo.rds
/usr/lib64/R/library/gplots/Meta/package.rds
/usr/lib64/R/library/gplots/Meta/vignette.rds
/usr/lib64/R/library/gplots/NAMESPACE
/usr/lib64/R/library/gplots/NEWS
/usr/lib64/R/library/gplots/R/gplots
/usr/lib64/R/library/gplots/R/gplots.rdb
/usr/lib64/R/library/gplots/R/gplots.rdx
/usr/lib64/R/library/gplots/TODO
/usr/lib64/R/library/gplots/data/rtPCR.rda
/usr/lib64/R/library/gplots/doc/BalloonPlot.pdf
/usr/lib64/R/library/gplots/doc/index.html
/usr/lib64/R/library/gplots/doc/venn.R
/usr/lib64/R/library/gplots/doc/venn.Rnw
/usr/lib64/R/library/gplots/doc/venn.pdf
/usr/lib64/R/library/gplots/help/AnIndex
/usr/lib64/R/library/gplots/help/aliases.rds
/usr/lib64/R/library/gplots/help/gplots.rdb
/usr/lib64/R/library/gplots/help/gplots.rdx
/usr/lib64/R/library/gplots/help/paths.rds
/usr/lib64/R/library/gplots/html/00Index.html
/usr/lib64/R/library/gplots/html/R.css
