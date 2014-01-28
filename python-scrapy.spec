%global pkg     scrapy
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           python-scrapy
Version:        0.22.0
Release:        1%{?dist}
Summary:        Scrapy, a fast high-level screen scraping and web crawling framework for Python.

License:        BSD
URL:            http://scrapy.org/
Source0:        https://github.com/%{pkg}/%{pkg}/archive/%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-sphinx

Provides:       scrapy

Requires:       python-twisted >= 10.0.0
Requires:       python-lxml
Requires:       pyOpenSSL
# scrapy-0.22.0 requires six>=1.5.2, but F20 contains 1.4.1
# Requires:       python-six >= 1.5.2
Requires:       python-six
# scrapy requires cssselect>=0.9, but F20 contains 0.8
# Requires:       python-cssselect >= 0.9
Requires:       python-cssselect
Requires:       python-w3lib >= 1.2
Requires:       python-queuelib

%description
Scrapy is a fast high-level screen scraping and web crawling framework,
used to crawl websites and extract structured data from their pages.
It can be used for a wide range of purposes, from data mining to
monitoring and automated testing.

%prep
%setup -q -n %{pkg}-%{version}


%build
%{__python} setup.py build
cd docs
make html
rm build/html/.buildinfo


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_mandir}/man1
gzip extras/scrapy.1
%{__install} -pm 644 extras/scrapy.1.gz %{buildroot}%{_mandir}/man1/


%files
%defattr(-,root,root,-)
%attr(755,root,root) %{_bindir}/scrapy
%doc AUTHORS LICENSE README.rst docs/build/html
%{python_sitelib}/*
%{_mandir}/man1/*


%changelog

* Tue Jan 28 2014 Eugene Zamriy <eugene@zamriy.info> - 0.22.0-1
- Initial release
