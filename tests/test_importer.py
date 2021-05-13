# -*- coding: utf-8 -*-
import cmath
import itertools
import math

import pytest

from import_monster import methods_importer


class TestMethodsImporter:
    def test_raises_error_on_incorrect_module_input(self):
        with pytest.raises(TypeError):
            methods_importer('cool_method', [123])

    def test_raises_error_on_non_existing_module_name(self):
        with pytest.raises(ModuleNotFoundError):
            methods_importer('cool_method', ['non_existing_module'])

    def test_returns_nothing_for_non_existing_method_for_module_name(self):
        assert methods_importer('non_existing_method', ['math']) == []

    def test_returns_nothing_for_non_existing_method_for_module(self):
        assert methods_importer('non_existing_method', [math]) == []

    def test_returns_nothing_for_non_callable_property_for_module_name(self):
        assert methods_importer('pi', ['math']) == []

    def test_returns_nothing_for_non_callable_property_for_module(self):
        assert methods_importer('pi', [math]) == []

    def test_returns_method_for_single_module_name(self):
        assert methods_importer('exp', ['math']) == [math.exp]

    def test_returns_only_existing_method_for_several_module_names(self):
        assert methods_importer('exp', ['math', 'itertools']) == [math.exp]

    def test_returns_several_existing_method_for_several_module_names(self):
        assert methods_importer('exp', ['math', 'cmath']) == [
            math.exp, cmath.exp]

    def test_keeps_the_order_of_modules_for_module_names(self):
        assert methods_importer('exp', ['cmath', 'math']) == [
            cmath.exp, math.exp]

    def test_returns_method_for_single_module(self):
        assert methods_importer('exp', [math]) == [math.exp]

    def test_returns_only_existing_method_for_several_modules(self):
        assert methods_importer('exp', [math, itertools]) == [math.exp]

    def test_returns_several_existing_method_for_several_modules(self):
        assert methods_importer('exp', [math, cmath]) == [math.exp, cmath.exp]

    def test_keeps_the_order_of_modules_for_modules(self):
        assert methods_importer('exp', [cmath, math]) == [cmath.exp, math.exp]
