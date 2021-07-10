from pamit import map_inplace
import taichi as ti


@ti.func
def index_sum(index_2d, _element):
    return index_2d[0] + index_2d[1]


if __name__ == "__main__":
    field = ti.field(ti.i32, shape=(2, 3))
    map_inplace(field, index_sum, True)
    print(field)
