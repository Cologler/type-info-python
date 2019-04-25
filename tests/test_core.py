# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import typing

from type_info import get_type_info

def test_typeinfo_eq():
    assert get_type_info(int) == int
    assert int == get_type_info(int)

    assert get_type_info(int) == get_type_info(int)

def test_typeinfo_is_generic_closed():
    assert get_type_info(int).is_generic_closed()
    assert get_type_info(typing.List[int]).is_generic_closed()
    assert not get_type_info(typing.List).is_generic_closed()
