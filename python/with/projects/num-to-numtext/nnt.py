NUMBERS = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

TEENS = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]

TENS = [
    "ten",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]

BIGS = [
    "hundred",
    "thousand",
    "million",
    "billion",
    "trillion",
    "quadrillion",
    "quintillion",
    "sextillion",
    "septillion",
    "octillion",
    "nonillion",
    "decillion",
]

"""
NumNumText: Numbers to Numbers Text
"""
class Nnt:
    def __init__(self):
        pass
        
        
    # numbers
    def number2text(self, number: int) -> str | None:
        if 9 >= number >= 0:
            for i, number_text in enumerate(NUMBERS):
                if i == number:
                    return number_text
        
        return None
    
    
    # tens
    def tens2text(self, tens: int) -> str | None:
        if 10 <= tens <= 99:
            if tens < 20:
                return TEENS[tens - 10]
            else:
                tens_digit = tens // 10
                unit_digit = tens % 10
                
                if unit_digit == 0:
                    return TENS[tens_digit - 1]
                else:
                    return f"{TENS[tens_digit - 1]}-{self.number2text(unit_digit)}"
        
        return None
    
    def bigs2text(self, num: int) -> str | None:
        if num < 100:
            return None

        powers = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33]
        names = BIGS[1:]
        
        for i in range(len(powers) - 1, -1, -1):
            power_of_10 = 10 ** powers[i]
            if num >= power_of_10:
                main_part = num // power_of_10
                remainder = num % power_of_10
                if remainder == 0:
                    return f"{self.num2text(main_part)} {names[i]}"
                else:
                    return f"{self.num2text(main_part)} {names[i]} {self.num2text(remainder)}"

        if num >= 100:
            main_part = num // 100
            remainder = num % 100
            if remainder == 0:
                return f"{self.number2text(main_part)} hundred"
            else:
                return f"{self.number2text(main_part)} hundred {self.num2text(remainder)}"
                
        return None
    
        
    def num2text(self, num: int) -> str:
        if (number := self.number2text(num)) is not None:
            return number
        
        if (tens := self.tens2text(num)) is not None:
            return tens
        
        if (bigs := self.bigs2text(num)) is not None:
            return bigs
            
        return "not supported"