from route import Route


class Fuel():
    def __init__(self, car):
        # self.car = car
        self.car = {"body": "Midsize", "fuel": "Gas", "consumption": 8}
        self.table = {
            "Gas": {
                "Midsize":
                    {65: 1.15,
                     75: 1.28},
                "Small SUV":
                    {65: 1.16,
                     75: 1.29},
                "Big SUV":
                    {65: 1.07,
                     75: 1.21}
            },
            "Diesel": {
                "Midsize":
                    {65: 1.18,
                     75: 1.33},
                "Small SUV":
                    {65: 1.19,
                     75: 1.34},
                "Big SUV":
                    {65: 1.13,
                     75: 1.27}
            },
            "Hybrid": {
                "Midsize":
                    {65: 1.18,
                     75: 1.28}}
            }
        
    def consumption(self, route: Route, speed):
        """55mph is considered the perfect speed for fuel economy"""
            
            
        loss_table = self.table[self.car["fuel"]][self.car["body"]]
        distance = route.distance() / 1000  # convert to km
        print(distance)
        distance *= 0.621371  # convert to miles
        base_consumption = self.car["consumption"] * 1.60934  # convert to l/100 miles
        
        if speed <= 55:
            return distance * base_consumption / 100
        
        elif speed <= 65 and speed > 55:
            speed_over = speed - 55
            
            multiplier = ((10 - speed_over) + speed_over * loss_table[65]) / 10
            consumption = multiplier * base_consumption
            return distance * consumption / 100
        
        elif speed <= 75 and speed > 65:
            speed_over = speed - 65
            
            multiplier = ((10 - speed_over) + speed_over * loss_table[75]) / 10
            consumption = multiplier * base_consumption
            return distance * consumption / 100
        else:
            consumption = base_consumption * loss_table[75]
            return distance * consumption / 100
    
    def cost(self, route: Route, speed, price):
        consumption = self.consumption(route, speed)
        return price * consumption
        
if __name__ == "__main__":
    route = Route()
    route.directions.get("Białystok Polska", "Vienna Austria")
    fuel = Fuel(None)
    price = fuel.cost(route, 55, 6.5)
    print(price)
    
        
        