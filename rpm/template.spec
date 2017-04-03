Name:           ros-kinetic-ackermann-controller
Version:        0.1.2
Release:        0%{?dist}
Summary:        ROS ackermann_controller package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-angles
Requires:       ros-kinetic-control-msgs
Requires:       ros-kinetic-control-toolbox
Requires:       ros-kinetic-controller-interface
Requires:       ros-kinetic-forward-command-controller
Requires:       ros-kinetic-hardware-interface
Requires:       ros-kinetic-nav-msgs
Requires:       ros-kinetic-realtime-tools
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-urdf
BuildRequires:  ros-kinetic-angles
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-control-msgs
BuildRequires:  ros-kinetic-control-toolbox
BuildRequires:  ros-kinetic-controller-interface
BuildRequires:  ros-kinetic-forward-command-controller
BuildRequires:  ros-kinetic-hardware-interface
BuildRequires:  ros-kinetic-nav-msgs
BuildRequires:  ros-kinetic-realtime-tools
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-tf
BuildRequires:  ros-kinetic-urdf

%description
The ackermann_controller package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Apr 03 2017 Easymov Robotics <dev@easymov.fr> - 0.1.2-0
- Autogenerated by Bloom

* Mon Apr 03 2017 Easymov Robotics <dev@easymov.fr> - 0.1.1-0
- Autogenerated by Bloom

* Sat Apr 01 2017 Easymov Robotics <dev@easymov.fr> - 0.1.0-0
- Autogenerated by Bloom

