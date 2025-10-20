Version: 2025.1.4
    Name:           android-studio
    Version:        2025.1.4.8
    Release:        1
    Summary:        The official IDE for Android application development
    License:        Android Studio License Agreement
    URL:            https://developer.android.com/studio
    Source0:        https://redirector.gvt1.com/edgedl/android/studio/ide-zips/%{version}/android-studio-%{version}-linux.tar.gz
    BuildArch:      noarch

    Requires:       java-11-openjdk
    BuildRequires:  fdupes

    %description
    Android Studio is the official integrated development environment for Google's
    Android operating system, built on JetBrains' IntelliJ IDEA software.

    %prep
    %setup -q -n android-studio

    %install
    mkdir -p %{buildroot}/opt/android-studio
    cp -r ./* %{buildroot}/opt/android-studio/

    mkdir -p %{buildroot}%{_bindir}
    ln -s /opt/android-studio/bin/studio.sh %{buildroot}%{_bindir}/android-studio

    mkdir -p %{buildroot}%{_datadir}/applications
    cat > %{buildroot}%{_datadir}/applications/android-studio.desktop << EOF
    [Desktop Entry]
    Version=1.0
    Type=Application
    Name=Android Studio
    Comment=The official IDE for Android development
    Icon=/opt/android-studio/bin/studio.svg
    Exec=android-studio %f
    Categories=Development;IDE;
    Terminal=false
    StartupWMClass=jetbrains-studio
    EOF

    %fdupes %{buildroot}/opt/android-studio

    %files
    /opt/android-studio
    %{_bindir}/android-studio
    %{_datadir}/applications/android-studio.desktop

    %changelog
    * Thu Aug 28 2025 itachi_re <quackxan99@gmail.com>
    - Initial packaging
    
