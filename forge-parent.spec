Name:           forge-parent
Version:        38
Release:        1%{?dist}
Summary:        Sonatype Forge Parent Pom
License:        ASL 2.0
URL:            https://docs.sonatype.org/display/FORGE/Index
Source0:        http://repo1.maven.org/maven2/org/sonatype/forge/%{name}/%{version}/%{name}-%{version}.pom
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch
BuildSystem:	maven

BuildRequires:	javapackages-tools
%description
Sonatype Forge is an open-source community dedicated to the creation of the 
next-generation of development tools and technologies.

%prep
%setup -qcT
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE
# We don't have nexus-staging-maven-plugin in Fedora
%pom_remove_plugin :nexus-staging-maven-plugin

%files -f .mfiles
%doc LICENSE
