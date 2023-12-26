import functools, inspect
from location import *

def postcondition(predicate):

    def function_decorator(f):

        @functools.wraps(f)
        def wrapper(self, *args, **kwargs):
            result = f(self, *args, **kwargs)
            if not predicate(self):
                raise RuntimeError(
                    f"Post-condition {predicate.__name__} not maintained for {self!r}"
                )
            return result
        
        return wrapper
    
    return function_decorator

def invariant(predicate):
    function_decorator = postcondition(predicate)

    def class_decorator(cls):
        members = list(vars(cls).items())
        for name, member in members:
            if inspect.isfunction(member):
                decorated_member = function_decorator(member)
                setattr(cls, name, decorated_member)
        return cls
    
    return class_decorator

def no_dups(itinerary):
    already_seen = set()
    for location in itinerary._locations:
        if location in already_seen: return False
        already_seen.add(location)
    return True

def at_least_two_locations(itinerary):
    return len(itinerary._locations) >= 2

@auto_repr
@invariant(no_dups)
@invariant(at_least_two_locations)
class Itinerary:

    @classmethod
    def from_locations(cls, *locations):
        return cls(locations)
    
    def __init__(self, locations):
        self._locations = list(locations)
    
    def __str__(self):
        return "\n".join(location.name for location in self._locations)
    
    @property
    def locations(self):
        return tuple(self._locations)
    
    @property
    def origin(self):
        return self._locations[0]
    
    @property
    def destination(self):
        return self._locations[-1]
    
    def add(self, location):
        self._locations.append(location)
    
    def remove(self, name):
        removal_indexes = [
            index for index, location in enumerate(self._locations) if location.name == name
        ]
        for index in reversed(removal_indexes):
            del self._locations[index]
    
    def truncate_at(self, name):
        stop = None
        for index, location in enumerate(self._locations):
            if location.name == name:
                stop = index + 1
        
        self._locations = self._locations[:stop]


trip = Itinerary.from_locations(hong_kong, rotterdam)
