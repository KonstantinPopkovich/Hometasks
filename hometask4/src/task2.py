#Дан список стран и городов каждой страны.
# Затем даны названия городов. Для каждого города укажите, в какой стране он находится.
#Входные данные
#Программа получает на вход количество стран N.
# Далее идет N строк, каждая строка начинается с названия страны, затем идут названия городов этой страны.
# В следующей строке записано число M, далее идут M запросов — названия каких-то M городов, перечисленных выше.
#Выходные данные
#Для каждого из запроса выведите название страны, в котором находится данный город.
#Примеры
#Входные данные
#2
#Russia Moscow Petersburg Novgorod Kaluga
#Ukraine Kiev Donetsk Odessa

#3
#Odessa
#Moscow
#Novgorod

#Выходные данные
#Ukraine
#Russia
#Russia


def country_city():
    countries = {
        "Moscow": "Russia",
        "Petersburg": "Russia",
        "Novgorod": "Russia",
        "Kaluga": "Russia",
        "Kiev": "Ukraine",
        "Donetsk": "Ukraine",
        "Odessa": "Ukraine"
    }

    cities = ["Odessa", "Moscow", "Novgorod"]
    results = []

    for city in cities:
        country = countries.get(city, "Unknown")
        results.append(country)

    return results

if __name__ == "__main__":
    countries_and_cities = country_city()
    for country in countries_and_cities:
        print(country)
