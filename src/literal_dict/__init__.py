from inspect import currentframe
from typing import Sequence, TypeVar, cast

T = TypeVar("T")


class DictBuilder:
    def __getitem__(self, args: slice | T | Sequence[slice | T]) -> dict[str, T]:
        if not isinstance(args, tuple):
            args = cast(tuple, (args,))

        frame = currentframe()
        assert frame, "Unable to get the current frame."

        caller_frame = frame.f_back
        assert caller_frame, "Unable to get the caller's frame."

        obj = {}
        for arg in args:
            if isinstance(arg, slice):
                assert isinstance(arg.start, str), "Ket must be a string"
                obj[arg.start] = arg.stop
            else:
                for name, var in caller_frame.f_locals.items():
                    if var is arg:
                        obj[name] = arg
                        break

        return obj
