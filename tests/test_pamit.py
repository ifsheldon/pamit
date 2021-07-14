from pamit import *
import taichi as ti
import numpy as np


@ti.func
def add(_index, _element, v1, v2):
    return v1 + v2


@ti.func
def increment(element, v1, v2):
    return element + v1 + v2


def test_simple_map_inplace():
    ti.init(ti.cpu)
    field = ti.field(ti.f32, shape=(2, 3))
    map_inplace(field, add, True, 2.0, 2.0)
    output = field.to_numpy()
    assert np.allclose(output, 4.0)


def test_simple_map_to():
    ti.init(ti.cpu)
    field = ti.field(ti.f32, shape=(2, 3))
    map_inplace(field, add, True, 2.0, 2.0)
    field2 = ti.field(ti.f32, shape=(2, 3))
    map_to(field, field2, increment, False, 1.0, 1.0)
    output = field2.to_numpy()
    assert np.allclose(output, 6.0)
