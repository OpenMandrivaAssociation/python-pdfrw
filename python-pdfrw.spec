%define	oname pdfrw

Name:		python-%{oname}
Version:	0.2
Release:	2
Summary:	PDF file reader/writer library
Source0:	https://pypi.python.org/packages/source/p/%{oname}/%{oname}-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		https://pypi.python.org/pypi/pdfrw
BuildArch:	noarch
BuildRequires:	python3egg(setuptools)
BuildRequires:	pkgconfig(python3)
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

%package -n python2-%{oname}
Summary:	Python2 PDF file reader/writer library

%description -n python2-%{oname}
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

mv %{oname}-%{version} python3
cp -a python3 python2

%build
pushd python3
%{__python} setup.py build
popd

pushd python2
%{__python2} setup.py build
popd

%install
pushd python3
%{__python} setup.py install --root=%{buildroot}
cp -R examples %{buildroot}%{py_puresitedir}/pdfrw/
chmod +x %{buildroot}%{py_puresitedir}/pdfrw/pdfwriter.py
popd

pushd python2
%{__python2} setup.py install --root=%{buildroot}
cp -R examples %{buildroot}%{py2_puresitedir}/pdfrw/
chmod +x %{buildroot}%{py2_puresitedir}/pdfrw/pdfwriter.py
popd

%files
%{py_puresitedir}/pdfrw/*.py*
%{py_puresitedir}/pdfrw/objects/*.py*
%{py_puresitedir}/pdfrw*.egg-info
%{py_puresitedir}/pdfrw/examples/

%files -n python2-%{oname}
%{py_puresitedir}/pdfrw/*.py*
%{py_puresitedir}/pdfrw/objects/*.py*
%{py_puresitedir}/pdfrw*.egg-info
%{py_puresitedir}/pdfrw/examples/