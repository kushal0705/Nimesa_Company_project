def get_pressure_by_date(weather_data, date):
    for item in weather_data["list"]:
        if item["dt_txt"].startswith(date):
            return item["main"]["pressure"]
    return None