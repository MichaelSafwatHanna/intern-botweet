import datetime
import os
from os.path import join

resources_path = join(os.getcwd(), 'resources/')

app_cache_path = join(resources_path, 'app-cache.json')

day_zero = datetime.date(2020, 8, 9)
