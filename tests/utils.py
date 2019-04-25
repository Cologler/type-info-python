# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

def generic_as_tuple(type_info):
    if type_info is None:
        return None

    assert type_info.is_generic
    assert not type_info.is_typevar

    return (
        type_info.generic_type,
        type_info.generic_args,
        type_info.dynamic_type
    )

def typevar_as_tuple(type_info):
    if type_info is None:
        return None

    assert not type_info.is_generic
    assert type_info.is_typevar
    return type_info.get_attrs_as_tuple()

class _Any:
    def __eq__(self, value):
        return True

ANY = _Any()
