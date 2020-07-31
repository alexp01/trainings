from typing import List

class Segment:
    def __init__(self, departure, destination):
        self.departure = departure # CDG
        self.destination = destination # LHR


class Flight:
    def __init__(self, segments: List[Segment]):
        self.segments = segments

    def __repr__(self):
        stops = [self.segments[0].departure, self.segments[0].destination]
        for seg in self.segments[1:]:
            stops.append(seg.destination)

        return '->'.join(stops)

    @property
    def departure_point(self) -> str:
        return self.segments[0].departure

    @departure_point.setter
    def departure_point(self, val):
        # self.segment_departure = val
        # OR
        dest = self.segments[0].destination
        self.segments[0] = Segment(departure = val, destination = dest)



flight = Flight([Segment('CDG', 'LHR')])
#print (flight.departure_point)
#flight.segments[0].departure = 'EDI'

# OR
flight.departure_point = 'EDI'
print(flight)