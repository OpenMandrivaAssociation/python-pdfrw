%define	oname	pdfrw

Name:		python-%{oname}
Version:	0.2
Release:	1
Summary:	PDF file reader/writer library
Source0:	https://pypi.python.org/packages/source/p/%{oname}/%{oname}-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		https://pypi.python.org/pypi/pdfrw
BuildArch:	noarch
BuildRequires:	python3egg(setuptools)
BuildRequires:	pkgconfig(python)

%description
pdfrw lets you read and write PDF files, including
compositing multiple pages together (e.g. to do watermarking,
or to copy an image or diagram from one PDF to another),
and can output by itself, or in conjunction with reportlab.

pdfrw will faithfully reproduce vector formats without
rasterization, so the rst2pdf package has used pdfrw
by default for PDF and SVG images by default since
March 2010.  Several small examples are provided.

%prep
%setup -q -n %{oname}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --root=%{buildroot}
cp -R examples %{buildroot}%{py_puresitedir}/pdfrw/
chmod +x %{buildroot}%{py_puresitedir}/pdfrw/pdfwriter.py

%files
%doc README.txt
%{py_puresitedir}/pdfrw/*.py*
%{py_puresitedir}/pdfrw/objects/*.py*
%{py_puresitedir}/pdfrw*.egg-info
%{py_puresitedir}/pdfrw/examples/