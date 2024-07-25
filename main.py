def create_car(color, consumption, tank_volume, mileage=0):
    return {
        "color": color,
        "consumption": consumption,  # Qolgan yoqilg'i
        "tank_volume": tank_volume,  # Yoqilg'i baki
        "reserve": tank_volume,  # Yoqilg'i zahirasi
        "mileage": mileage,  # Yurgan masofa
        "engine_on": False  # Dvigatel to'xtatildi.
    }


def start_engine(car):
    if not car["engine_on"] and car["reserve"] > 0:
        car["engine_on"] = True
        return "Dvigatel ishga tushirildi."
    return "Dvigatel allaqachon ishga tushirilgan."


def stop_engine(car):
    if car["engine_on"]:
        car["engine_on"] = False
        return "Dvigatel to'xtatildi."
    return "Dvigatel allaqachon to'xtatilgan."


def drive(car, distance):
    if not car["engine_on"]:
        return "Dvigatel ishga tushirilmagan."
    if car["reserve"] / car["consumption"] * 100 < distance:
        return "Yoqilg'i zahirasi kam."
    car["mileage"] += distance
    car["reserve"] -= distance / 100 * car["consumption"]
    return f"{distance} km yurgan. Qolgan yoqilg'i: {car['reserve']} l."


def refuel(car):
    car["reserve"] = car["tank_volume"]


def get_mileage(car):
    return f"Yurgan masofa {car['mileage']} km."


def get_reserve(car):
    return f"Yoqilg'i zahirasi {car['reserve']} l."


# car_1 = create_car(color="black", consumption=10, tank_volume=55)
# print(start_engine(car_1))  # Dvigatel ishga tushirildi.
# print(drive(car_1, 100))  # 100 km yurgan. Qolgan yoqilg'i: 45.0 l.
# print(drive(car_1, 100))  # 100 km yurgan. Qolgan yoqilg'i: 35.0 l.
# print(drive(car_1, 100))  # 100 km yurgan. Qolgan yoqilg'i: 25.0 l.
# print(drive(car_1, 300))  # Yoqilg'i zahirasi kam.
# print(get_mileage(car_1))  # Yurgan masofa 300 km.
# print(get_reserve(car_1))  # Yoqilg'i zahirasi 25.0 l.
# print(stop_engine(car_1))  # Dvigatel to'xtatildi.
# print(drive(car_1, 100))  # Dvigatel ishga tushirilmagan.


class Car:
    def __init__(self, color, consumption, tank_volume, mileage=0):
        self.color = color
        self.consumption = consumption
        self.tank_volume = tank_volume
        self.reserve = tank_volume
        self.mileage = mileage
        self.engine_on = False

    def start_engine(self):
        if not self.engine_on and self.reserve > 0:
            self.engine_on = True
            return "Dvigatel ishga tushirildi."
        return "Dvigatel allaqachon ishga tushirilgan."

    def stop_engine(self):
        if self.engine_on:
            self.engine_on = False
            return "Dvigatel to'xtatildi."
        return "Dvigatel allaqachon to'xtatilgan."

    def drive(self, distance):
        if not self.engine_on:
            return "Dvigatel ishga tushirilmagan."
        if self.reserve / self.consumption * 100 < distance:
            return "Yoqilg'i zahirasi kam."
        self.mileage += distance
        self.reserve -= distance / 100 * self.consumption
        return f"{distance} km yurgan. Qolgan yoqilg'i: {self.reserve} l."

    def refuel(self):
        self.reserve = self.tank_volume

    def get_mileage(self):
        return f"Yurgan masofa {self.mileage} km."

    def get_reserve(self):
        return f"Yoqilg'i zahirasi {self.reserve} l."


car_1 = Car(color="black", consumption=10, tank_volume=55)
print(car_1.start_engine())
print(car_1.drive(100))
print(car_1.drive(100))
print(car_1.drive(100))
print(car_1.drive(300))
print(f"Yurgan masofa {car_1.get_mileage()} km.")
print(f"Yoqilg'i zahirasi {car_1.get_reserve()} l.")
print(car_1.stop_engine())
print(car_1.drive(100))
