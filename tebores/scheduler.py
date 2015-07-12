# -*- coding: utf-8 -*-

import datetime

class Scheduler(object):
    """Schedules Tebores' publication times."""

    def __init__(self, timetable):
        self.timetable = timetable
        self.time_from = datetime.time(int(timetable['FROM'].split(':')[0]),
                                       int(timetable['FROM'].split(':')[1]))
        self.time_to = datetime.time(int(timetable['TO'].split(':')[0]),
                                     int(timetable['TO'].split(':')[1]))
    def is_time(self):
        return self.time_from <= datetime.datetime.now().time() <= self.time_to
