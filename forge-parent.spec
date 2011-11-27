Name:           forge-parent
Version:        5
Release:        8
Summary:        Sonatype Forge Parent Pom

Group:          Development/Java
#Note: The license is confirmed at:
#http://nexus.sonatype.org/mailing-list-dev-archives.html#nabble-ts28522017
License:        ASL 2.0
#svn export http://svn.sonatype.org/forge/tags/forge-parent-5 forge-parent
URL:            http://svn.sonatype.org/forge/tags/forge-parent-5

# tar czf forge-parent-5.tgz forge-parent
Source0:        forge-parent-5.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: java
BuildRequires: java-devel

Requires: jpackage-utils

%description
Sonatype Forge is an open-source community dedicated to the creation of the 
next-generation of development tools and technologies.

%prep
%setup -q -n %{name}

%build
#nothing to do for the pom

%install
rm -rf %{buildroot}/

%add_to_maven_depmap org.sonatype.forge forge-parent %{version} JPP forge-parent

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%post
%update_maven_depmap

%postun
%update_maven_depmap

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)

%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

