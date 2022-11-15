Name:		texlive-cmupint
Version:	54735
Release:	1
Summary:	Upright integral symbols for Computer Modern
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cmupint
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmupint.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmupint.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package contains various upright integral symbols to match
the Computer Modern font.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/cmupint
%{_texmfdistdir}/fonts/type1/public/cmupint
%{_texmfdistdir}/fonts/tfm/public/cmupint
%doc %{_texmfdistdir}/fonts/source/public/cmupint
%{_texmfdistdir}/fonts/map/dvips/cmupint
%{_texmfdistdir}/fonts/afm/public/cmupint
%doc %{_texmfdistdir}/doc/fonts/cmupint

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
