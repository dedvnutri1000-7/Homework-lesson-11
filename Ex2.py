class MyTime:
    def __init__(self, *args):
        if len(args) == 0:
            self.hours, self.minutes, self.seconds = 0, 0, 0

        elif len(args) == 1:
            if isinstance(args[0], str):
                # Строка вида "12:30:45"
                parts = args[0].split(":")
                self.hours, self.minutes, self.seconds = map(int, parts)
        elif len(args) == 3:
                self.hours = args[0]
                self.minutes = args[1]
                self.seconds = args[2]
        else:
            raise ValueError("Ошибка!")
        self._normalize()

    def _normalize(self):
        total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds
        if total_seconds < 0:
            total_seconds = 0

        self.hours = (total_seconds // 3600) % 24
        self.minutes = (total_seconds % 3600) // 60
        self.seconds = total_seconds % 60

    def total_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


    def __eq__(self, other):
        return self.total_seconds() == MyTime(other).total_seconds()

    def __ne__(self, other):
        return self.total_seconds() != MyTime(other).total_seconds()

    def __lt__(self, other):
        return self.total_seconds() < MyTime(other).total_seconds()

    def __le__(self, other):
        return self.total_seconds() <= MyTime(other).total_seconds()

    def __gt__(self, other):
        return self.total_seconds() > MyTime(other).total_seconds()

    def __ge__(self, other):
        return self.total_seconds() >= MyTime(other).total_seconds()

    def __add__(self, other):
        total = self.total_seconds() + other.total_seconds()
        return MyTime(0, 0, total)

    def __sub__(self, other):
        total = self.total_seconds() - other.total_seconds()
        return MyTime(0, 0, total)

    def __mul__(self, number):
        total = int(self.total_seconds() * number)
        return MyTime(0, 0, total)

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"


t1 = MyTime("12:85:53") #Неправильный по умолчанию ввод (85 минут не бывает в одном часу)
t2 = MyTime(1, 30, 40)
t3 = MyTime()

print(t1)
print(t2 + t1)
print(t1 - t2)
print(t2 * 3)
print(t1 > t2)
