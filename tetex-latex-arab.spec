%define name tetex-latex-arab
%define version 3.11s

Name:		%{name}
Summary:	Files for processing Arabic LaTeX documents
Version:	%{version}
Release:	15
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


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 3.11s-8mdv2011.0
+ Revision: 670678
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 3.11s-7mdv2011.0
+ Revision: 607990
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 3.11s-6mdv2010.1
+ Revision: 524228
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 3.11s-5mdv2010.0
+ Revision: 427346
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 3.11s-4mdv2009.1
+ Revision: 351476
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 3.11s-3mdv2009.0
+ Revision: 225675
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 3.11s-2mdv2008.1
+ Revision: 179646
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix description-line-too-long
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jun 14 2007 Adam Williamson <awilliamson@mandriva.org> 3.11s-1mdv2008.0
+ Revision: 39310
- install documentation correctly, only include text docs
- simplify installation routine
- new release 3.11s


* Wed Jun 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.11k-1mdk
- from Munzir Taha Obeid <munzirtaha@newhorizons.com.sa> : 
- Upgraded to 3.11k which fixed Arabic and Hebrew insertions
  in a LTR paragraph. There used to be spurious spaces and shifted baselines.
- Removed locales-ar from the spec file header. #ArabTeX is locale independent
- Removed rm -rf from the prep script since the %%setup macro should takes care of this.
- Rebuild

* Thu Dec 04 2003 Lenny Cartier <lenny@mandrakesoft.com> 3.11d-1mdk
- from Munzir Taha Obeid <munzirtaha@newhorizons.com.sa> : 
        - Upgraded to 3.11d which which fixed many bugs related to 
LyX, Arabic, Farsi, Uighuric, Urdu, Pashto, Persian and Hebrew modes. 
(Prof. Klaus Lagally)
- Fix Bug #5712 (Munzir Taha)
- Specfile clean up
- Add examples
- Injected new description
- Corrected the Licence line to say LPPL
- gz to bz2 compression

* Tue Jul 22 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 3.09f-4mdk
- rebuild

* Wed May 22 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 3.09f-3mdk
- Automated rebuild with gcc 3.1-1mdk

* Sat Mar 23 2002 David BAUDENS <baudens@mandrakesoft.com> 3.09f-2mdk
- Allow build
- Spec clean up

* Mon Jan 08 2001 Pablo Saratxaga <pablo@mandrakesoft.com> 0.9f-1mdk
- created the package for MDK.

