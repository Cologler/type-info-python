# type-info

Provide some public api for `typing` module.

## Usage

``` py
from type_info import get_type_info

type_info = get_type_info(typing.Dict[str, int])
assert type_info.generic_type is typing.Dict
assert type_info.generic_args == (str, int)
assert type_info.dynamic_type is dict
```
