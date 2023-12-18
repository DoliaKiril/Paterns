import haversine as hs


class Port:
    def __init__(self, ID, latitude, longitude):
        self.ID = ID
        self.latitude = latitude
        self.longitude = longitude
        self.containers = []
        self.history = []
        self.current = []

    def getDistance(self, other_port):
        distance_km = hs.haversine((self.latitude, self.longitude),
                                   (other_port.latitude, other_port.longitude))
        return distance_km


port_data = data['ports']
port1 = Port(**port_data[0])
port2 = Port(**port_data[1])

distance = port1.getDistance(port2)
print(f"Відстань між Port 1 та Port 2 є {distance:.2f} кілометрів.")
