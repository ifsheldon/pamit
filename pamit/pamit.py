import taichi as ti


@ti.kernel
def mapto_kernel(src_field: ti.template(), target_field: ti.template(), ti_func: ti.template()):
    for index in ti.grouped(ti.ndrange(*src_field.shape)):
        target_field[index] = ti_func(index, src_field[index])


def map_to(src_field, target_field, ti_func, with_index, *args):
    assert src_field.shape == target_field.shape

    @ti.func
    def _func_with_index(index, element):
        arguments = args
        return ti_func(index, element, *arguments)

    @ti.func
    def _func(_index, element):
        arguments = args
        return ti_func(element, *arguments)

    if with_index:
        mapto_kernel(src_field, target_field, _func_with_index)
    else:
        mapto_kernel(src_field, target_field, _func)
    pass


def map_inplace(field, ti_func, with_index, *args):
    map_to(field, field, ti_func, with_index, *args)
