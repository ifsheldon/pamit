from pamit import map_inplace
import taichi as ti


@ti.func
def add(_index, _element, v1, v2):
    return v1 + v2


if __name__ == "__main__":
    field = ti.field(ti.f32, shape=(2, 3))
    map_inplace(field, add, True, 2.0, 2.0)
    print(field)
