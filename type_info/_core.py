# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import abc
import typing
import collections

class ITypeInfo(abc.ABC):
    def __init__(self, target_type, is_classvar=False):
        self._target_type = target_type
        self._is_classvar = is_classvar

    def __repr__(self):
        return f'{type(self).__name__}({self.target_type!r})'

    @property
    def target_type(self):
        return self._target_type

    @property
    def is_generic(self):
        return False

    def is_generic_closed(self):
        return True

    @property
    def is_typevar(self):
        return False

    @property
    def is_classvar(self):
        return self._is_classvar


class TypeInfo(ITypeInfo):
    def __hash__(self):
        return hash(self._get_attrs_tuple())

    def __eq__(self, value):
        if self is value:
            return True

        if isinstance(value, type):
            return self.target_type == value and not self.is_classvar

        if type(value) is TypeInfo:
            return self._get_attrs_tuple() == value._get_attrs_tuple()

        return NotImplemented

    def _get_attrs_tuple(self):
        return (self._is_classvar, self._target_type)


class GenericTypeInfo(ITypeInfo):
    def __init__(self, target_type, **kwargs):
        self.generic_type = kwargs.pop('generic_type')
        self.generic_args = kwargs.pop('generic_args')

        # dynamic_type can be abs, std_type cannot be abs
        # `GenericTypeInfo(List[str]).std_type` is `list`
        # but `GenericTypeInfo(Iterable[str]).std_type` is None
        self.dynamic_type = kwargs.pop('dynamic_type')
        self.std_type = kwargs.pop('std_type')

        super().__init__(target_type, **kwargs)

    # from ITypeInfo

    @property
    def is_generic(self):
        return True

    def is_generic_closed(self):
        return all(arg.is_generic_closed() for arg in self.generic_args)

    #

    def __hash__(self):
        return hash(self._get_attrs_tuple())

    def __eq__(self, value):
        if self is value:
            return True

        if type(value) is GenericTypeInfo:
            return self._get_attrs_tuple() == value._get_attrs_tuple()

        return NotImplemented

    def _get_attrs_tuple(self):
        return (
            self._is_classvar,
            self.generic_type,
            self.generic_args
        )


class TypeVarTypeInfo(ITypeInfo):
    def __init__(self, target_type, **kwargs):
        self.typevar_constraints = kwargs.pop('constraints')
        self.typevar_covariant = kwargs.pop('covariant')
        self.typevar_contravariant = kwargs.pop('contravariant')
        super().__init__(target_type, **kwargs)

    # from ITypeInfo

    def is_generic_closed(self):
        return False

    @property
    def is_typevar(self):
        return True

    #

    def __hash__(self):
        return hash(self._get_attrs_tuple())

    def __eq__(self, value):
        if self is value:
            return True

        if type(value) is TypeVarTypeInfo:
            return self._get_attrs_tuple() == value._get_attrs_tuple()

        return NotImplemented

    def _get_attrs_tuple(self):
        return (
            self._is_classvar,
            self.typevar_constraints,
            self.typevar_covariant,
            self.typevar_contravariant
        )


STD_TYPES = {
    dict,
    frozenset,
    list,
    set,
    tuple,
    type,
    bytes,

    # collections
    collections.ChainMap,
    collections.Counter,
    collections.defaultdict,
    collections.deque,
    collections.OrderedDict
}

def from_any():
    ''' get type info for `typing.Any` '''
    return TypeVarTypeInfo(
        typing.Any,
        constraints=(),
        covariant=False,
        contravariant=False
    )

def from_type(target, args):
    ''' get type info for `typing.Type[]` '''
    # like: typing.Type[str]
    return TypeVarTypeInfo(target,
        constraints=args,
        covariant=True,
        contravariant=False,
    )

def from_union(target, args):
    ''' get type info for `typing.Union[]` '''
    # union should be a typevar
    # this canbe parameter or return value
    # so `covariant` and `contravariant` should be `False`
    return TypeVarTypeInfo(target,
        constraints=args,
        covariant=False,
        contravariant=False,
    )

