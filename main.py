from remedio import *


def main():
    print(end="\n")

    ans = Medicine(name="Ansitec", total_amount=20, amount_taken_per_day=0.5,
                   difference_between_dates=1, initial_date=date.fromisoformat("2023-04-28"))
    ans.what_day_does_the_medicine_run_out()

    ins = Medicine(name="Inseris XR", total_amount=30, amount_taken_per_day=1.5,
                   difference_between_dates=2, initial_date=date.fromisoformat("2023-04-28"))
    ins.what_day_does_the_medicine_run_out()

    div = Medicine(name="Divalcon ER", total_amount=30, amount_taken_per_day=1,
                   difference_between_dates=1, initial_date=date.fromisoformat("2023-04-28"))
    div.what_day_does_the_medicine_run_out()


if __name__ == '__main__':
    main()
