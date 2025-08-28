%define _binaries_in_noarch_packages_terminate_build 0
%define debug_package %{nil}

Name:           android-studio
Version:        2025.1.2
Release:        1%{?dist}
Summary:        The official IDE for Android application development
License:        Android Studio License Agreement
URL:            https://developer.android.com/studio/
Source0:        https://redirector.gvt1.com/edgedl/android/studio/ide-zips/%{version}/android-studio-%{version}-linux.tar.gz

BuildRequires:  bash
Requires:       java-11-openjdk

%description
Android Studio is the official integrated development environment (IDE) for Google's
Android operating system, built on JetBrains' IntelliJ IDEA software and designed
specifically for Android development.

%prep
%setup -q -n android-studio

%build
# Nothing to build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/android-studio
cp -r ./* %{buildroot}%{_datadir}/android-studio/

# Create a symlink to the executable
mkdir -p %{buildroot}%{_bindir}
ln -s %{_datadir}/android-studio/bin/studio.sh %{buildroot}%{_bindir}/android-studio

# Create desktop entry
mkdir -p %{buildroot}%{_datadir}/applications
cat <<EOF > %{buildroot}%{_datadir}/applications/android-studio.desktop
[Desktop Entry]
Version=1.0
Type=Application
Name=Android Studio
Icon=%{_datadir}/android-studio/bin/studio.svg
Exec="/opt/android-studio/bin/studio.sh" %f
Comment=The official IDE for Android development
Categories=Development;IDE;
Terminal=false
StartupWMClass=jetbrains-studio
EOF

%files
%{_datadir}/android-studio
%{_bindir}/android-studio
%{_datadir}/applications/android-studio.desktop

%changelog
* Thu Aug 28 2025 itachi_re <your_email@example.com> - 2025.1.2-1
- Initial package
