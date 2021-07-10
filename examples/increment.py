from pamit import map_inplace
import taichi as ti


@ti.func
def increment(element, val):
    return element + val


if __name__ == "__main__":
    field = ti.field(ti.f32, shape=(2, 3))
    map_inplace(field, increment, False, 2.0)
    print(field)
