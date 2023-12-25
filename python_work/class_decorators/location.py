class Position:

    def __init__(self, latitude, longitude):
        if not (-90 <= latitude <= +90):
            raise ValueError(f"Latitude {latitude} out of range")
        
        if not (-180 <= longitude <= +180):
            raise ValueError(f"Longitude {longitude} out of range")
        
        self._latitude = latitude
        self._longitude = longitude
    
    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

class EarthPostion(Position):
    pass

class Location:

    def __init__(self, name, position):
        self._name = name
        self._position = position
    
    @property
    def name(self):
        return self._name
    
    @property
    def position(self):
        return self._position
    
    def __repr__(self):
        return f"{typename(self)}(name={self.name}, position={self.position})"
    
    def __str__(self):
        return self.name


def typename(obj): return obj.__class__.__name__

hong_kong = Location("Hong Kong", EarthPostion(22.29, 114.16))
stockholm = Location("Stockholm", EarthPostion(59.33, 18.06))
cape_town = Location("Cape Town", EarthPostion(-33.93, 18.42))
rotterdam = Location("Rotterdam", EarthPostion(51.96, 4.47))
maracaibo = Location("Maracaibo", EarthPostion(10.65, -71.65))
