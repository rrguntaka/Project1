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
    
    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.longitude == other.longitude and self.latitude == other.latitude
    
    def __hash__(self):
        return int(self.longitude +self.latitude)

class EarthPostion(Position):
    pass
