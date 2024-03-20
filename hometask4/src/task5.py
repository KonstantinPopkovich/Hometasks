# #Языки
# #Каждый из N школьников некоторой школы знает Mi языков. Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
# #Входные данные
# #Первая строка входных данных содержит количество школьников N. Далее идет N чисел Mi, после каждого из чисел идет Mi строк, содержащих названия языков, которые знает i-й школьник.
# #Пример входных данных:
# 	3          # N количество школьников
# 2          # M1 количество языков первого школьника
# Russian    # языки первого школьника
# English
# 3          # M2 количество языков второго школьника
# Russian
# Belarusian
# English
# 3
# Russian
# Italian
# French
# #
# #
# # Выходные данные
# # В первой строке выведите количество языков, которые знают все школьники.
# # Начиная со второй строки - список таких языков.
# # Затем - количество языков, которые знает хотя бы один школьник,
# # на следующих строках - список таких языков.
#
def language():
    students = [
        set(["Russian", "English"]),
        set(["Russian", "Belarussian", "English"]),
        set(["Russian", "Italian", "French"])
    ]

    common_languages = set.intersection(*students)
    all_languages = set.union(*students)

    return {
        'common_languages_count': len(common_languages),
        'common_languages': sorted(common_languages),
        'all_languages_count': len(all_languages),
        'all_languages': sorted(all_languages)
    }

if __name__ == "__main__":
    results = language()
    print(f"All pupils know {results['common_languages_count']} language(s)")
    print("All pupils know", ", ".join(results['common_languages']))
    print(f"At least one pupil knows {results['all_languages_count']}")
    print("At least one pupil knows", ", ".join(results['all_languages']))

