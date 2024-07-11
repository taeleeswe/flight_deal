import time
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()



if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    pprint(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_code()