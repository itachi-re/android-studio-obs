#
# spec file for package android-studio
#
Name:           android-studio
Version:        2025.2.1.8
Release:        0
Summary:        The official Android IDE
Source0:        https://redirector.gvt1.com/edgedl/android/studio/ide-zips/%{version}/%{name}-%{version}-linux.tar.gz
Source1:        android-studio.rpmlintrc
License:        Apache-2.0
BuildRequires:  bsdtar
BuildRequires:  zip
BuildRequires:  -post-build-checks
Requires:       which
Requires:       libgthread-2_0-0
ExclusiveArch:  x86_64
AutoReqProv:    no

# These are needed to handle the pre-compiled binaries in the source tarball
%global debug_package %{nil}
%define _build_create_debug 0
%undefine _missing_build_ids_terminate_build
%define _enable_debug_packages 0
%define __debug_install_post %{nil}

%description
Android Studio is the official IDE for Android development, and includes everything you need to build Android apps.

%prep
%autosetup -n %{name}

# Create the desktop file
cat << EOF > %{name}.desktop
[Desktop Entry]
Version=1.0
Type=Application
Name=Android Studio (Beta branch)
Exec=android-studio %f
Icon=android-studio
Comment=The Official Android IDE (Beta branch)
Categories=Development;IDE;
Terminal=false
StartupNotify=true
StartupWMClass=jetbrains-studio-beta
MimeType=application/x-extension-iml;
EOF

# Modify resources.jar to change product name to "Studio Beta"
# This method avoids the 'iconv' command that caused the previous failure.
# We also use 'sed -i' and 'zip -u' for a more efficient update.
bsdtar -xf lib/resources.jar idea/AndroidStudioApplicationInfo.xml
sed -i 's/"Studio"/"Studio Beta"/' idea/AndroidStudioApplicationInfo.xml
zip -u lib/resources.jar idea/AndroidStudioApplicationInfo.xml
rm -r idea

%install
install -Dm644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm644 bin/studio.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a bin/ lib/ jbr/ plugins/ product-info.json %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_bindir}
ln -s %{_datadir}/%{name}/bin/studio %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_defaultlicensedir}/%{name}
# Use 'cp -a' for safety
cp -a license/. %{buildroot}%{_defaultlicensedir}/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/
# Use the modern %license macro for the license files
%license %{_defaultlicensedir}/%{name}

%changelog
