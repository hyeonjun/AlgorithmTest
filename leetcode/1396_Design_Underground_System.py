from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.hashMap = {}
        self.totalTime = defaultdict(int)
        self.count = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.hashMap[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        name, time = self.hashMap.pop(id)
        self.totalTime[(name, stationName)] += t - time
        self.count[(name, stationName)] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.totalTime[(startStation, endStation)] / self.count[(startStation, endStation)]