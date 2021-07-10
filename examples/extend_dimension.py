from pamit import *
import taichi as ti
import taichi_glsl as tl


@ti.func
def increment(element, val):
    return element + val


@ti.func
def extend(element):
    return tl.vec3(element)


if __name__ == "__main__":
    shape = (2, 3)
    field = ti.field(ti.f32, shape=shape)
    vec_field = ti.Vector.field(3, dtype=ti.f32, shape=shape)
    map_inplace(field, increment, False, 2.0)
    map_to(field, vec_field, extend, False)
    print(f"scalar field {field}")
    print(f"vec field {vec_field}")
