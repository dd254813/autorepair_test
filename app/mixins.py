from app.models import (Worker,
                        Customer,
                        Schedule)

"""
В функции working_hours и working_days устанавливаются возможное для записи время и дни недели
"""


class UniversalMixins():

    def get_schedule(self):
        schedule = Schedule.objects.all()
        return schedule

    def get_all_workers(self):
        workers = Worker.objects.all()
        return workers

    def working_hours(self):
        hours = ['10-00','11-00','12-00','13-00','14-00','15-00','16-00','17-00','18-00','19-00']
        return hours

    def working_days(self):
        days = [1,2,3,4,5]
        return days

    def get_main(self):
        schedule = self.get_schedule()
        workers = self.get_all_workers()
        hours = self.working_hours()
        days = self.working_days()
        context = {
            'schedule': schedule,
            'workers': workers,
            'hours': hours,
            'days': days,
        }
        return context
