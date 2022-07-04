#!/usr/bin/env python

import OpenGL

def play():
    # ['ALLOW_NUMPY_SCALARS', 'ARRAY_SIZE_CHECKING', 'CONTEXT_CHECKING', 'ERROR_CHECKING', 'ERROR_LOGGING', 'ERROR_ON_COPY', 'FORWARD_COMPATIBLE_ONLY', 'FULL_LOGGING', 'FormatHandler', 'MODULE_ANNOTATIONS', 'PlatformPlugin', 'SIZE_1_ARRAY_UNPACK', 'STORE_POINTERS', 'TYPE_ANNOTATIONS', 'UNSIGNED_BYTE_IMAGES_AS_STRING', 'USE_ACCELERATE', 'WARN_ON_FORMAT_UNAVAILABLE', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_bi', 'environ_key', 'os', 'plugins', 'sys', 'version']
    for k in dir(OpenGL):
        if k.isupper():
            print(f"{k} = {getattr(OpenGL, k)}")
