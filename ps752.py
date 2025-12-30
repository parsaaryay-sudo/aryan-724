import requests

class SearcherBus:
    def _init_(self, origin, destination, date):
        self.origin = origin
        self.destination = destination
        self.date = date

    def print_services(self):

        url = "https://service.safar724.com/buses/api/bus/route"

        params = {
            "Date": self.date,
            "Origin": self.origin,
            "Destination": self.destination
        }

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json",
            "Referer": "https://safar724.com/"
        }

        try:
            response = requests.get(url, params=params, headers=headers, timeout=10)

            # 👇 وضعیت HTTP
            if response.status_code != 200:
                return f"❌ API Error: {response.status_code}"

            data = response.json()

        except requests.exceptions.RequestException as e:
            return f"❌ Request failed: {e}"

        except ValueError:
            return "❌ Response is not JSON"

        services = data.get("items", [])

        if not services:
            return "⚠️ هیچ سرویسی پیدا نشد"

        bus_list = ""
        for item in services:
            time_ = item.get("departureTime")
            price = item.get("price")
            bus_type = item.get("busType")
            company = item.get("companyPersianName")
            seats = item.get("availableSeatCount")

            bus_list += (
                f"⏱ ساعت: {time_} | 💰 قیمت: {price} | "
                f"🚍 نوع: {bus_type} | 🏢 شرکت: {company} | "
                f"🪑 صندلی خالی: {seats}\n\n"
            )

        return bus_list
