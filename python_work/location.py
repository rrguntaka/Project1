import inspect

def typename(obj): return obj.__class__.__name__


def auto_repr(cls):
    print(f"Decorating {cls.__name__} with auto repr")
    members = vars(cls)
    
    if "__repr__" in members:
        raise TypeError(f"{cls.__name__} already defines __repr__")
    
    if "__init__" not in members:
        raise TypeError(f"{cls.__name__} does not override __init__")
    
    sig = inspect.signature(cls.__init__)
    parameter_names = list(sig.parameters)[1:]
    
    if not all(
        isinstance(members.get(name, None), property)
        for name in parameter_names
    ):
        raise TypeError(f"Cannot apply auto_repr to {cls.__name__} because not all "
        "__init__ parameters have matching propoerties"
        )
    
    def sythesized_repr(self):
        return "{typename}({args})".format(
            typename=typename(self),
            args=", ".join(
                "{name}={value!r}".format(name=name, value=getattr(self, name)
                ) for name in parameter_names)
        )
    
    setattr(cls, "__repr__", sythesized_repr)

    return cls

from dataclasses import dataclass
from position import Position, EarthPostion

@dataclass(eq=True, frozen=True)
class Location:
    name:str
    position: Position

    def __post_init__(self):
        if self.name == "":
            raise ValueError("Location name cannot be empty!")


hong_kong = Location("Hong Kong", EarthPostion(22.29, 114.16))
stockholm = Location("Stockholm", EarthPostion(59.33, 18.06))
cape_town = Location("Cape Town", EarthPostion(-33.93, 18.42))
rotterdam = Location("Rotterdam", EarthPostion(51.96, 4.47))
maracaibo = Location("Maracaibo", EarthPostion(10.65, -71.65))
