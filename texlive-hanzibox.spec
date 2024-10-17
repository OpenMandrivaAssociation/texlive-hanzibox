Name:		texlive-hanzibox
Version:	63062
Release:	2
Summary:	Boxed Chinese characters with Pinyin above and translation below
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hanzibox
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hanzibox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hanzibox.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hanzibox.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a LaTeX package written to simplify the input of
Chinese with Hanyu Pinyin and translation. Hanyu Pinyin is
placed above Chinese with the xpinyin package, and the
translation is placed below. The package can be used as a
utility for learning to write and pronounce Chinese characters,
for Chinese character learning plans, presentations, exercise
booklets and other documentation work.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/xelatex/hanzibox
%{_texmfdistdir}/tex/xelatex/hanzibox
%doc %{_texmfdistdir}/doc/xelatex/hanzibox

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
