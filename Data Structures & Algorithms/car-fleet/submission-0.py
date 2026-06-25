class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_fleet = 0
        bundled_fleet = list(zip(position, speed))
        sorted_fleet = sorted(bundled_fleet, key=lambda x:x[0], reverse=True)
        max_time_ahead = 0

        for i, (position, speed) in enumerate(sorted_fleet):
            time_to_target = (target - position) / speed
            if time_to_target > max_time_ahead:
                car_fleet+=1
            max_time_ahead = max(max_time_ahead, time_to_target)
        return car_fleet
