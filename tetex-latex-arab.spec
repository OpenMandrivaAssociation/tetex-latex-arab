%define name tetex-latex-arab
%define version 3.11k
%define release 1mdk 

Name:		%{name}
Summary:	Files for processing Arabic LaTeX documents
Version:	%{version}
Release:	%{release}
Source:		ftp://ftp.informatik.uni-stuttgart.de/pub/arabtex/arabtex.tar.bz2
License:	LPPL
Group:		Publishing
URL:		ftp://ftp.informatik.uni-stuttgart.de/pub/arabtex/arabtex.htm
Requires:	tetex >= 1.0.7
Packager:	Taha Obeid <munzirtaha@newhorizons.com.sa>	
BuildArch:	noarch
Obsoletes:	arabtex
Provides:	arabtex = %version
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
%setup -q -n arabtex

%install
install -d -m 0755 %buildroot/%_datadir/texmf/fonts/source/arabtex
install -d -m 0755 %buildroot/%_datadir/texmf/fonts/tfm/arabtex
install -d -m 0755 %buildroot/%_datadir/texmf/fonts/type1/arabtex
install -d -m 0755 %buildroot/%_datadir/texmf/fonts/pk/arabtex
install -d -m 0755 %buildroot/%_datadir/texmf/tex/latex/arabtex
install -d -m 0755 %buildroot/%_datadir/texmf/doc/arabtex

for i in mfinput/*.mf; do
	install -m 0644 $i %buildroot/%_datadir/texmf/fonts/source/arabtex
done
for i in tfm/*.tfm; do
	install -m 0644 $i %buildroot/%_datadir/texmf/fonts/tfm/arabtex
done
for i in psfonts/*.pfb; do
	install -m 0644 $i %buildroot/%_datadir/texmf/fonts/type1/arabtex
done
for i in laser.pk/*; do
	install -m 0644 $i %buildroot/%_datadir/texmf/fonts/pk/arabtex
done

for i in texinput/*; do
	install -m 0644 $i %buildroot/%_datadir/texmf/tex/latex/arabtex
done
for i in doc/* examples/*; do
	install -m 0644 $i %buildroot/%_datadir/texmf/doc/arabtex
done


%post 
/usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0


%clean
rm -rf $RPM_BUILD_ROOT


%files 
%defattr(-,root,root,0755)
%doc announce.txt changes2.txt changes.txt install.txt readme.txt
%_datadir/texmf/fonts/source/arabtex
%_datadir/texmf/fonts/tfm/arabtex
%_datadir/texmf/fonts/type1/arabtex
%_datadir/texmf/fonts/pk/arabtex
%_datadir/texmf/tex/latex/arabtex
%doc %_datadir/texmf/doc/arabtex


