from dataclasses import dataclass
from datetime import date, timedelta
from math import ceil


@dataclass
class Medicine:
    name: str
    total_amount: int
    amount_taken_per_day: float
    difference_between_dates: int
    initial_date: date
    final_date: date = None

    def what_day_does_the_medicine_run_out(self):
        days = (self.total_amount / self.amount_taken_per_day) * self.difference_between_dates
        self.final_date = self.initial_date + timedelta(days=days)
        print(f"{self.name} will run out in the day {self.final_date} ({days} ~= {ceil(days)} days)\n"
              f"Between {date.today()} and {self.final_date} are {(self.final_date - date.today()).days} days\n")
