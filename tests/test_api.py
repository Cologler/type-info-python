# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import sys
import typing

import pytest

@pytest.mark.skipif(sys.version_info[:3] > (3, 7, 0), reason='version 3.7.0 api')
def test_py_370():
    pass

@pytest.mark.skipif(sys.version_info[:3] > (3, 7, 1), reason='version 3.7.1 api')
def test_py_371():
    assert not hasattr(typing, 'OrderedDict')
