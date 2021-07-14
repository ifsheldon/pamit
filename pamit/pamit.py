import taichi as ti


@ti.kernel
def mapto_kernel(src_field: ti.template(), target_field: ti.template(), ti_func: ti.template()):
    for index in ti.grouped(ti.ndrange(*src_field.shape)):
        target_field[index] = ti_func(index, src_field[index])


def map_to(src_field, target_field, ti_func, with_index, *args):
    """

    :param src_field: a taichi field of which values are mapped
    :param target_field: a taichi field that receives mapped values
    target_field must have the same shape of src_field
    :param ti_func: @ti.func mapping function
    :param with_index: whether ti_func receive indices
    if True, ti_func should have index and element as first two arguments
    if False, ti_func should have element as the first argument
    :param args: arguments passed to ti_func
    :return: None
    """
    assert src_field.shape == target_field.shape, "source field and target field must have the same shape"

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


def map_inplace(field, ti_func, with_index, *args):
    """

    :param field: a taichi field of which values are mapped inplace
    :param ti_func: a @ti_func mapping function
    :param with_index: whether ti_func receive indices
    if True, ti_func should have index and element as first two arguments
    if False, ti_func should have element as the first argument
    :param args: arguments passed to ti_func
    :return: None
    """
    map_to(field, field, ti_func, with_index, *args)
