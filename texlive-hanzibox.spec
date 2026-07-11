%global tl_name hanzibox
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.3.0
Release:	%{tl_revision}.1
Summary:	Boxed Chinese characters with Pinyin above and translation below
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/hanzibox
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hanzibox.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hanzibox.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hanzibox.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a LaTeX package written to simplify the input of Chinese with
Hanyu Pinyin and translation. Hanyu Pinyin is placed above Chinese with
the xpinyin package, and the translation is placed below. The package
can be used as a utility for learning to write and pronounce Chinese
characters, for Chinese character learning plans, presentations,
exercise booklets and other documentation work.

