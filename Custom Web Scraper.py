"""
retrieves data on a random roller-coaster from the website -> https://rcdb.com and adds it to a csv file
"""
import csv
from bs4 import BeautifulSoup
import requests
from os import path

ROLLER_COASTERS_URL = "https://rcdb.com/"
roller_data = {}


def scrap_data(url):
    global roller_data
    response = requests.get(url)
    website_html = response.text
    if response.status_code == 200:
        soup = BeautifulSoup(website_html, "html.parser")
        roller_coaster_data = soup.find_all(name="p")
        formatted_data = [entry.text for entry in roller_coaster_data]
        print(formatted_data)

        for entry in formatted_data:
            if "Roller Coaster" in entry:
                roller_data["Roller Coaster Name"] = entry.replace("Roller Coaster", "")
            if "Park" in entry:
                roller_data["Park"] = entry.replace("Park", "")
            if "Location" in entry:
                roller_data["Location"] = entry.replace("Location", "")
            if "Status" in entry:
                roller_data["Status"] = entry.replace("Status", "")
            if "Speed" in entry:
                roller_data["Speed"] = entry.replace("Speed", "")
            if "Height" in entry:
                roller_data["Height"] = entry.replace("Height", "")
            if "Manufacturer" in entry:
                roller_data["Manufacturer"] = entry.replace("Manufacturer", "")

    return roller_data


def save_to_csv(scrapped_data):
    fieldnames = ["Roller Coaster Name", "Park", "Location", "Status", "Speed", "Height", "Manufacturer"]
    if path.exists("roller_coasters.csv"):
        with open("roller_coasters.csv", mode="a", newline="", encoding="utf-8") as csvfile:
            dict_writer_object = csv.DictWriter(csvfile, fieldnames=fieldnames, restval="-")
            dict_writer_object.writerow(roller_data)
    else:
        with open("roller_coasters.csv", mode="w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["Roller Coaster Name", "Park", "Location", "Status", "Speed", "Height", "Manufacturer"]
            csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames, restval="-")
            csv_writer.writeheader()

            csv_writer.writerow(scrapped_data)


if __name__ == "__main__":
    scrap_data(ROLLER_COASTERS_URL)
    save_to_csv(roller_data)

"""
you can run the programme again to add another random
roller coaster data entry to your new 'random roller coasters' data bank :) 
"""
