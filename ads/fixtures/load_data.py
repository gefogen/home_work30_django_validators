import csv, json

# Параметры
csv_file_ad = 'ad.csv'
json_file_ad = '../fixtures/ad.json'
ad_model = 'ads.ad'

csv_file_category = 'category.csv'
json_file_category = '../fixtures/category.json'
category_model = 'ads.category'

csv_file_location = 'location.csv'
json_file_location = '../fixtures/location.json'
location_model = 'users.location'

csv_file_user = 'user.csv'
json_file_user = '../fixtures/user.json'
users_model = 'users.user'


# Функция конвертации
def csv_to_json(csv_file_path: str, json_file_path: str, model: str) -> str:
    """Конвертировать csv в json"""

    # прочитать файл csv и добавить в словарь
    with open(csv_file_path, encoding='utf-8') as file:
        reader = csv.DictReader(file)

        data: list = [
            {'model': model,
             'pk': int(row['id']) if row.get('id') else int(row['Id']),
             'fields': {key: replace_values(value) for key, value in row.items() if key != 'id' and key != 'Id'}}
            for row in reader

        ]

    # создать новый файл json и записать данные
    with open(json_file_path, 'w', encoding='utf-8') as file:
        file.write(json.dumps(data, indent=4, ensure_ascii=False))

    return f'Данные из CSV ({csv_file_path}) преобразовано в json ({json_file_path})'


def replace_values(value):
    """Преобразование цифр и логических значений в требуемые типы"""
    if value.isdigit():
        return int(value)
    if value == 'FALSE':
        return False
    if value == 'TRUE':
        return True
    return value


if __name__ == '__main__':
    print(csv_to_json(csv_file_ad, json_file_ad, ad_model))
    print(csv_to_json(csv_file_category, json_file_category, category_model))
    print(csv_to_json(csv_file_location, json_file_location, location_model))
    print(csv_to_json(csv_file_user, json_file_user, users_model))