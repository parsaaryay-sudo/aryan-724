import requests

class SearcherBus :
    def __init__( self , origin , destination , date ) :
        self.origin = origin 
        self.destination = destination
        self.date = date


    def print_services(self) :
        

        url = "https://service.safar724.com/buses/api/bus/route"

        params = {
            "Date": self.date,
            "Origin": self.origin,
            "Destination": self.destination
        }


        response = requests.get(url, params=params)
        data = response.json()

        services = data.get("items", [])
        bus_list = " "
        for item in services:
            time_ = item.get("departureTime")
            price = item.get("price")
            bus_type = item.get("busType")
            company = item.get("companyPersianName")
            seats = item.get("availableSeatCount")
            bus_list += f"""⏱ ساعت: {time_} | 💰 قیمت: {price} | 🚍 نوع: {bus_type} | 🏢 شرکت: {company} | صندلی خالی: {seats}\n\n"""

        return bus_list
    
