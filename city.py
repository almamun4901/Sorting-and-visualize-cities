#Name: Md Al Mamun
#Date: 11/ 01/ 2022
#Purpose: Lab3 Checkpoint


class City:
    def __init__(self, country_code, city_name, region, population, latitude, longitude):
        self.country_code = str(country_code[:2])
        self.city_name = str(city_name)
        self.region = str(region[:2])
        self.population = int(population)
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def __str__(self):
        return str(self.city_name)+","+ str(self.population)+","+ str(self.latitude) + ","+ str(self.longitude)