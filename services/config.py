import os
from datetime import date, timedelta
from os.path import join

resources_path = join(os.getcwd(), 'resources/')

app_cache_path = join(resources_path, 'app-cache.json')

day_zero = date(2020, 8, 9)
farewell_day = day_zero + timedelta(days=90)
total_days = farewell_day - day_zero
