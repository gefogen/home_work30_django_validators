import csv, json


# Параметры
csv_file_ads = 'ads.csv'
json_file_ads = '../fixtures/ads.json'
ads_model = 'ads.ad'

csv_file_catetories = 'categories.csv'
json_file_categories = '../fixtures/categories.json'
categories_model = 'ads.category'


# Функция конвертации
def csv_to_json(csv_file_path: str, json_file_path: str, model: str) -> str:
    """Конвертировать csv в json"""

    # прочитать файл csv и добавить в словарь
    with open(csv_file_path, encoding='utf-8') as file:
        reader = csv.DictReader(file)

        data: list = [
            {'model': model,
             'pk': int(row['id']) if row.get('id') else int(row['Id']),
             'fields': {
                 key: replace_values(value) for key, value in row.items() if key != 'id' and key != 'Id'}
             }
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
    print(csv_to_json(csv_file_ads, json_file_ads, ads_model))
    print(csv_to_json(csv_file_catetories, json_file_categories, categories_model))