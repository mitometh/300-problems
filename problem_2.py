# This question was asked by Riot Games.
# Design and implement a HitCounter class that keeps track of requests (or hits). It should support the following operations:
# record(timestamp): records a hit that happened at timestamp
# total(): returns the total number of hits recorded
# range(lower, upper): returns the number of hits that occurred between timestamps lower and upper (inclusive)

class HitCounter:
    def __init__(self):
        self.hits = []

    def record(self, timestamp):
        """Records a hit at the given timestamp."""
        self.hits.append(timestamp)
    
    def total(self) -> int:
        """Returns the total number of hits recorded."""
        return len(self.hits)
    
    def range(self, lower, upper) -> int:
        """Returns the number of hits that occurred between timestamps lower and upper (inclusive)."""
        return len([hit for hit in self.hits if lower <= hit <= upper])
    
if __name__ == '__main__':
    hitCounter = HitCounter()
    hitCounter.record(5)
    hitCounter.record(8)
    hitCounter.record(10)
    hitCounter.record(13)
    hitCounter.record(23)
    print(hitCounter.total())
    print(hitCounter.range(2, 13))