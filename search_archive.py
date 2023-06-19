
from scripts.collect import Collect
import datetime


c = Collect("config.ini")
time = {"end": datetime.datetime.strptime("2023-01-09 00:00:00", "%Y-%m-%d %H:%M:%S"), "delta": 4, "delta_type": "hour"}
c.search_archive("stf OR congresso OR planalto OR câmara OR brasília", max_per_request=100, time=time, id="coletaPlanalto", folder="coleta/planalto2")


# Horários

# 0 - 13:00 - 14:00
# 1 - 14:00 - 15:00
# 2 - 15:00 - 16:00
# 3 - 16:00 - 17:00
# 4 - 17:00 - 18:00
# 5 - 18:00 - 19:00
# 6 - 19:00 - 20:00
# 7 - 20:00 - 21:00
# 8 - 21:00 - 22:00
# 9 - 22:00 - 23:00
# 10 - 23:00 - 00:00