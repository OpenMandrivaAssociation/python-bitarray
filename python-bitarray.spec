%define module bitarray

Name:		python-bitarray
Version:	3.8.1
Release:	1
Summary:	efficient arrays of booleans -- C extension
License:	PSF-2.0
Group:		Development/Python
URL:		https://pypi.org/project/bitarray/
Source0:	https://files.pythonhosted.org/packages/source/b/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
%{module} provides an object type which efficiently represents an
array of booleans.

Bitarrays are sequence types and behave very much like usual lists.
Eight bits are represented by one byte in a contiguous block of memory.
The user can select between two representations: little-endian and big-endian.
All functionality is implemented in C.

Methods for accessing the machine representation are provided, including the
ability to import and export buffers. This allows creating bitarrays that are
mapped to other objects, including memory-mapped files.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%build -p
export LDFLAGS="%{ldflags} -lpython%{pyver}"

%files
%{python_sitearch}/%{module}
%{python_sitearch}/%{module}-%{version}.dist-info
