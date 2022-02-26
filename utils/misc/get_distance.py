import math
from aiogram import types
from utils.misc import show_on_gmaps

# from data.locations import Masjidlar
from loader import db

def calc_distance(lat1, lon1, lat2, lon2):
    R = 6371000
    phi_1 = math.radians(lat1)
    phi_2 = math.radians(lat2)

    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2.0) ** 2 + \
        math.cos(phi_1) * math.cos(phi_2) * \
        math.sin(delta_lambda / 2.0) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    meters = R * c  # output distance in meters
    return meters / 1000.0  # output distance in kilometers


async def choose_shortest(location: types.Location):
    distances = list()
    Masjidlar = await db.get_mosques()
    for masjid in Masjidlar:
        distances.append((masjid['name'],
                          calc_distance(location.latitude, location.longitude,
                                        float(masjid['latitude']), float(masjid['longtitude'])),
                          show_on_gmaps.show(float(masjid['latitude']), float(masjid['longtitude'])),
                          float(masjid['latitude']), float(masjid['longtitude'])
                          ))
    return sorted(distances, key=lambda x: x[1])[:3]