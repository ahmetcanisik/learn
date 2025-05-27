#!/usr/bin/env python
from re import match as re_match

class ClockConverter:
    def __init__(self):
        pass
    
    @staticmethod
    def second_to_minute(second: int) -> float | int:
        return second / 60
    
    @staticmethod
    def second_to_hours(second: int) -> float | int:
        return second / 3600
    
    @staticmethod
    def minute_to_second(minute: int) -> float | int:
        return minute * 60

    @staticmethod
    def minute_to_hours(minute: int) -> float | int:
        return minute / 60
    
    @staticmethod
    def hours_to_second(hours: int) -> float | int:
        return hours * 3600
    
    @staticmethod
    def hours_to_minute(hours: int) -> float | int:
        return hours * 60
    
    
    """
    usage: 3 hours to minute
    """
    def convert(self, pattern: str, n: int | None = None) -> int:
        try:
            match = re_match(r"^(\d+)?\s?(h|s|m)\s?(?:to|->)\s?(h|s|m)", pattern)
            if not match:
                raise ValueError("Invalid pattern format")
            time, time1, time2 = match.groups()
            
            try:
                time = n if n is not None else int(time)
            except ValueError:
                raise ValueError("Invalid time!")
            
            match [time1, time2]:
                case ["s", "h"]:
                    return self.second_to_hours(time)
                case ["s", "m"]:
                    return self.second_to_minute(time)
                case ["m", "h"]:
                    return self.minute_to_hours(time)
                case ["m", "s"]:
                    return self.minute_to_second(time)
                case ["h", "s"]:
                    return self.hours_to_second(time)
                case ["h", "m"]:
                    return self.hours_to_minute(time)
                case _:
                    raise ValueError("Invalid time conversion pattern")
        except Exception as e:
            print("Time conversion failed!", e)
            return 0

def main():
    clock_converter = ClockConverter()
    second = 120
    print(
        round(
            clock_converter.convert(
                f"{second}stom"
            )
        )
    )
    
if __name__ == "__main__":
    main()