# -*- coding: utf-8 -*-

# Name of the database
DB_NAME = 'tebores_db.sqlite'
# Bot type: DesktopBot or TwitterAPIBot
BOT_TYPE = 'TwitterAPIBot'
# Bot timetable
TIMETABLE_SCRA = {
    # Scraping hours (data recolection) from-tog 24h format.
    'FROM' : '11:45',
    'TO' : '22:00'
    }
TIMETABLE_TWI = {
    # Tweeting hours from-to 24h format.
    'FROM' : '12:00',
    'TO' : '22:00'
    }

# Scraping frequency, seconds
S_FREQ = 300
# Tweeting frequency
TW_FREQ = 180
