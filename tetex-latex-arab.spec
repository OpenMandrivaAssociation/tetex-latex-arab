%define name tetex-latex-arab
%define version 3.11s

Name:		%{name}
Summary:	Files for processing Arabic LaTeX documents
Version:	%{version}
Release:	%mkrel 2
Source:		ftp://ftp.informatik.uni-stuttgart.de/pub/arabtex/arab311.tar.bz2
License:	LPPL
Group:		Publishing
URL:		ftp://ftp.informatik.uni-stuttgart.de/pub/arabtex/arabtex.htm
Requires:	tetex >= 1.0.7
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
ArabTeX is a TeX macro package with associated Naskh fonts designed to generate
the Arabic writing from texts coded in an ASCII transliteration as well as in 
some other popular encodings for Arabic and Hebrew, e.g. ASMO 449, ISO 8859-6 
(ASMO 708), Arabic Windows encoding, and HED. It is compatible with Plain TeX, 
LaTeX, NFSS, and the EDMAC package. It also cooperates well with LaTeX 2e of 
June 1996 or later. There is some support for Persian, Urdu, Pashto, and 
Sindhi. Unicode Arabic and Hebrew support is present but not extensively 
tested.

The version 3.11d supports vowelized and non-vowelized Hebrew, and 
bidirectional line-breaking within insertions. The former limitation that an 
insertion must fit on the current line no more exists.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
mv doc/arabtex/txt/* .
rm -rf doc/arabtex/html
install -d -m 0755 %buildroot/%_datadir/texmf
cp -R fonts tex %buildroot/%_datadir/texmf

%post 
/usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0


%clean
rm -rf $RPM_BUILD_ROOT


%files 
%defattr(-,root,root,0755)
%_datadir/texmf/fonts/source/arabtex
%_datadir/texmf/fonts/tfm/arabtex
%_datadir/texmf/fonts/type1/arabtex
%_datadir/texmf/fonts/pk/arabtex
%_datadir/texmf/tex/latex/arabtex
%doc announce.txt arabtex.doc arabtex.faq arwindoc.tex changes.txt changes2.txt hebrew.305 kashmiri.tex lppl.txt malay.tex miktex.mai readme.305 readme.txt sindhi.tex tetex.txt uighur.tex
