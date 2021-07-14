# pamit
pamit -> ti map: Taichi Map Utils

**PRs are welcomed! Please see TODOs.**

## Installation and Dependency
To install `pamit`, enter

`python -m pip install pamit`

Make sure you have `Taichi` installed.

## Usage

The APIs of `map_inplace()` and `map_to()` are straight forward.

`map_to` requires the target field to have the same shape of the source field, but the "channels" may differ. Please see `examples/extend_dimension` for example.

If `with_index` is `True`, then the Taichi function is expected to have `index` (i.e., the index of an element in a field) and `element` (i.e., the value of an element in a field) as first two arguments.

Otherwise, the Taichi function is expected to have `element` as the first argument.

```python
from pamit import map_inplace
import taichi as ti


@ti.func
def increment(element, val):
    return element + val


field = ti.field(ti.f32, shape=(2, 3))
map_inplace(field, increment, False, 2.0)
print(field)
```

## TODOs
* Set up CI and write test cases
* Check backward capability
* Reduce function
* Simple user documentation