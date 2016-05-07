#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/ros/husky_ws/src/universal_robot/ur_driver"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/ros/husky_ws/install/lib/python2.7/dist-packages:/home/ros/husky_ws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/ros/husky_ws/build" \
    "/usr/bin/python" \
    "/home/ros/husky_ws/src/universal_robot/ur_driver/setup.py" \
    build --build-base "/home/ros/husky_ws/build/universal_robot/ur_driver" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/ros/husky_ws/install" --install-scripts="/home/ros/husky_ws/install/bin"
