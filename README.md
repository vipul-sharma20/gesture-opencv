gesture-opencv
==============

This python script can be used to analyse hand gestures by contour detection,
and convex hull of hand palm using opencv library used for computer vision
processes.

* Built using OpenCV 2.4.12 on Python 2.7.10
* Works on OpenCV 2.4.x, 3.2.x and Python 2.x, Python 3.x

Video
=====

link: [http://goo.gl/fui2MH ](http://goo.gl/fui2MH)

[![IMAGE ALT TEXT](https://img.youtube.com/vi/QYiypuWZPU0/0.jpg)](https://www.youtube.com/watch?v=QYiypuWZPU0)


Installing OpenCV 3.2 from source Python 3.6
============================================

* `wget https://github.com/Itseez/opencv/archive/3.2.0.zip`
* `unzip 3.2.0.zip`
* `cd opencv-3.2.0`
* `mkdir release && cd release`

        cmake -DBUILD_TIFF=ON \
            -DBUILD_opencv_java=OFF \
            -DWITH_CUDA=OFF \
            -DENABLE_AVX=ON \
            -DWITH_OPENGL=ON \
            -DWITH_OPENCL=ON \
            -DWITH_IPP=OFF \
            -DWITH_TBB=ON \
            -DWITH_EIGEN=ON \
            -DWITH_V4L=ON \
            -DWITH_VTK=OFF \
            -DBUILD_TESTS=OFF \
            -DBUILD_PERF_TESTS=OFF \
            -DCMAKE_BUILD_TYPE=RELEASE \
            -DBUILD_opencv_python2=OFF \
            -DCMAKE_INSTALL_PREFIX=$(python3.6 -c "import sys; print(sys.prefix)") \
            -DPYTHON3_EXECUTABLE=$(which python3.6) \
            -DPYTHON3_INCLUDE_DIR=$(python3.6 -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())") \
            -DPYTHON3_PACKAGES_PATH=$(python3.6 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())") ..

* The output of above will be similar to this: [output](https://gist.github.com/vipul-sharma20/d57a779619f22b2254b66c89c957faf2)
* `make -j4`
* make install

See Also
========
Playing Pacman with gestures: [Repository](http://github.com/vipul-sharma20/gesture-pacman)
