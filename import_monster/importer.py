# -*- coding: utf-8 -*-
from functools import reduce
from importlib import import_module
from types import ModuleType
from typing import Callable, List, Union


def _get_module(module: Union[str, ModuleType]) -> ModuleType:
    if isinstance(module, ModuleType):
        return module

    elif isinstance(module, str):
        return import_module(module)

    raise TypeError('''
        'module' must be a str or a ModuleType
    ''')


def methods_importer(
    method_name: str, modules: List[Union[str, ModuleType]]
) -> List[Callable]:
    if not isinstance(method_name, str):
        raise TypeError('''
            'method_name' must be a str
        ''')

    def has_callable_method(module: ModuleType) -> bool:
        return hasattr(module, method_name) and callable(getattr(module, method_name))

    return reduce(
        lambda result, module: result + [getattr(module, method_name)]
        if has_callable_method(module)
        else result,
        map(_get_module, modules),
        [],
    )
