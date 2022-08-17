%global debug_package   %{nil}

Name:           rhvoice
Version:        1.8.0
Release:        1%{?dist}
Summary:        Free and open source speech synthesizer
    
# The main library is distributed under LGPL v2.1 or later.
# But it relies on MAGE for better responsiveness.
# MAGE is distributed under GPL v3 or later, so the combination is under GPL v3 or later.
# If you want to use the library in your program under GPL v2 or LGPL, compile the library without MAGE.
    
License:        GPLv3+
URL:            https://github.com/Olga-Yakovleva
Source0:        https://github.com/RHVoice/RHVoice/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildArch: x86_64

BuildRequires:  gcc-c++
BuildRequires:  python3-scons
    
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  libao-devel
    
BuildRequires:  portaudio-devel
Suggests:	    portaudio
   
BuildRequires:  speech-dispatcher-devel
BuildRequires:  python3-lxml
    
Requires:	  speech-dispatcher
Requires:	  libao
    
Requires:	%{name}-english 
Requires:	%{name}-utils
Requires:	%{name}-speech-dispatcher-plugin

%description
RHVoice is a free and open source speech synthesizer by Olga Yakovleva.

%package english
Summary:        English voices for RHVoice
BuildArch:      noarch
    
Requires:	%{name}

%description english
This package contains English voices resources for RHVoice.

%package russian
Summary:        Russian voices for RHVoice
BuildArch:      noarch
    
Requires:	%{name}

%description russian
This package contains Russian voices resources for RHVoice.

%package ukrainian
Summary:        Ukrainian voices for RHVoice
BuildArch:      noarch
    
Requires:	%{name}

%description ukrainian
This package contains Ukrainian voice resources for RHVoice.

%package kyrgiz
Summary:        Kyrgiz voices for RHVoice
BuildArch:      noarch

Requires:	%{name}

%description kyrgiz
This package contains Kyrgiz voices resources for RHVoice.

%package esperanto
Summary:        Esperanto voices for RHVoice
BuildArch:      noarch

Requires:	%{name}

%description esperanto
This package contains Esperanto voices resources for RHVoice.

%package brazilian-portuguese
License: CC-BY-NC-SA and CC-BY-NC-ND 
Summary:      Brazilian Portuguese language and voice for RHVoice
BuildArch:      noarch
    
Requires:	%{name}

%description brazilian-portuguese
This package contains Brazilian Portuguese language and voice for RHVoice.

#TODO: Create proper sub-packages
%package new-voices-and-languages-bundle
License: CC-BY-NC-SA
Summary: A bunch of new voices and languages added in this release
BuildArch: noarch
    
Requires:	%{name}

%description new-voices-and-languages-bundle
A bunch of new voices and languages added in this release.

%package utils
Summary:        Helper utilities for RHVoice
Requires: %{name}
    
%description utils
This package contains helper utilities for RHVoice

%package devel
Summary:        Development files for RHVoice

%package speech-dispatcher-plugin
Summary:        Speech dispatcher plugin based on RHVoice
Requires:	%{name}

%description speech-dispatcher-plugin
This package contains speech dispatcher plugin based on RHVoice.

    
%description devel
This package contains necessary header files for RHVoice-based applications development.

%prep
%setup -q -n %{name}-%{version}

%build
scons prefix=%{_prefix} \
      bindir=%{_bindir} \
      libdir=%{_libdir} \
      localedirname=locale \
      extra_flags_release="$RPM_OPT_FLAGS $RPM_LD_FLAGS" %{?_smp_mflags}
  
%install
rm -rf $RPM_BUILD_ROOT
scons DESTDIR=$RPM_BUILD_ROOT install

%files

%doc README.md
%license LICENSE.md

# %%{_bindir}/rhvoice-client
# %%{_bindir}/rhvoice-service

%files speech-dispatcher-plugin
%{_libdir}/speech-dispatcher-modules/sd_rhvoice

%{_libdir}/libRHVoice.so
%{_libdir}/libRHVoice.so.*
%{_libdir}/libRHVoice_core.so
%{_libdir}/libRHVoice_core.so.*
%{_libdir}/libRHVoice_audio.so
%{_libdir}/libRHVoice_audio.so.*
%config %{_prefix}/etc/RHVoice/RHVoice.conf

%files english
%{_datadir}/RHVoice/languages/English/*
%{_datadir}/RHVoice/voices/alan/*
%{_datadir}/RHVoice/voices/clb/*
%{_datadir}/RHVoice/voices/slt/*
%{_datadir}/RHVoice/voices/bdl/*

%files russian
%{_datadir}/RHVoice/languages/Russian/*
%{_datadir}/RHVoice/voices/aleksandr/*
%{_datadir}/RHVoice/voices/anna/*
%{_datadir}/RHVoice/voices/elena/*
%{_datadir}/RHVoice/voices/irina/*

%files ukrainian
%{_datadir}/RHVoice/languages/Ukrainian/*
%{_datadir}/RHVoice/voices/anatol/*
%{_datadir}/RHVoice/voices/natalia/*

%files kyrgiz
%{_datadir}/RHVoice/languages/Kyrgyz/*
%{_datadir}/RHVoice/voices/azamat/*
%{_datadir}/RHVoice/voices/nazgul/*

%files esperanto
%{_datadir}/RHVoice/languages/Esperanto/*
%{_datadir}/RHVoice/voices/spomenka/*

%files devel
%{_includedir}/RHVoice.h
%{_includedir}/RHVoice_common.h

%files utils
%{_bindir}/RHVoice-test
%ghost %{_bindir}/RHVoice-transcriptor
%ghost %{_bindir}/RHVoice-hts_labeller

%files brazilian-portuguese
%{_datadir}/RHVoice/languages/Brazilian-Portuguese/*
%{_datadir}/RHVoice/voices/Leticia-F123/*

%files new-voices-and-languages-bundle
%{_datadir}/RHVoice/voices/tatiana/*
%{_datadir}/RHVoice/voices/victoria/*
%{_datadir}/RHVoice/voices/vitaliy/*
%{_datadir}/RHVoice/voices/volodymyr/*
%{_datadir}/RHVoice/voices/yuriy/*
%{_datadir}/RHVoice/voices/aleksandr-hq/*
%{_datadir}/RHVoice/voices/arina/*
%{_datadir}/RHVoice/voices/evgeniy-eng/*
%{_datadir}/RHVoice/voices/evgeniy-rus/*
%{_datadir}/RHVoice/voices/hana/*
%{_datadir}/RHVoice/voices/kiko/*
%{_datadir}/RHVoice/voices/lyubov/*
%{_datadir}/RHVoice/voices/magda/*
%{_datadir}/RHVoice/voices/marianna/*
%{_datadir}/RHVoice/voices/mikhail/*
%{_datadir}/RHVoice/voices/natan/*
%{_datadir}/RHVoice/voices/pavel/*
%{_datadir}/RHVoice/voices/suze/*

%{_datadir}/RHVoice/languages/Polish/*
%{_datadir}/RHVoice/languages/Macedonian/*
%{_datadir}/RHVoice/languages/Albanian/*


# FIXME
# Excluded due to... idk
%ghost %{_datadir}/RHVoice/languages/Georgian/*
%ghost %{_datadir}/RHVoice/voices/natia/*

# New Russian voice
# Excluded due to regression
%ghost %{_datadir}/RHVoice/voices/artemiy/*

%{_datadir}/RHVoice/languages/Tatar/*
%{_datadir}/RHVoice/voices/talgat/*


%changelog
* Wed Aug 17 2022 Xoloitzcuintle <xoloitzcuintle_god@protonmail.com> - 1.8.0-2
- Dropped nonfree sub-package in favor of brazilian-portuguese sub-package


* Wed Aug 17 2022 Xoloitzcuintle <xoloitzcuintle_god@protonmail.com> - 1.8.0-1
- New version
- New (out of laziness) new-voices-and-languages-bundle sub-package

* Tue Sep 29 2020 Xoloitzcuintle <xoloitzcuintle_god@protonmail.com> - 1.2.3-1
- New version

* Thu Sep 10 2020 Xoloitzcuintle <xoloitzcuintle_god@protonmail.com> - 1.2.2-2
- 1.2.2
- Regression due to audio issues (clipping) on master branch

* Thu Sep 10 2020 Xoloitzcuintle <xoloitzcuintle_god@protonmail.com> - 1.2.2-1
- New version (git version)
- Brazilian Portuguese language support (LetÃ­cia-F123 voice)
- Licence and Readme files
- New Russian voice (Artemiy)
- nonfree sub-package

* Tue Aug 21 2018 Alex <alex@linuxonly.ru> - 0.7.2-1
- Update version

* Mon Aug 20 2018 Alex <alex@linuxonly.ru> - 0.7.0-2
- Split voices, plugins and helper utilities

* Wed May 16 2018 Alex <alex@linuxonly.ru> - 0.7.0-1
- New version

* Thu Mar 29 2018 Alex <alex@linuxonly.ru> - 0.6.0-2
- Fix development package requirement

* Tue Oct 10 2017 Alex <alex@linuxonly.ru> - 0.6.0-1
- New version

* Sat Aug 27 2016 Alex <alex@linuxonly.ru> - 0.6.0-1
- First package for Fedora

