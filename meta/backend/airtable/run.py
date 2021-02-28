from local_settings import AIRTABLE_TABLE_NAME, AIRTABLE_BASE_ID, AIRTABLE_YOUR_API_KEY
from backend.wsgi import *
import sys
import requests
from api.models import Profile, Skills, Launch


class Airtable(object):
    API_BASE_URL = 'https://api.airtable.com/v0/'

    def __init__(self, base_id, table_name, api_key):
        self.__base_id = base_id
        self.__table_name = table_name
        self.__api_key = api_key

    def _connect(self):
        """Подключается к db airtable"""

        endpoint = f'{self.API_BASE_URL}{self.__base_id}/{self.__table_name}'
        headers = {
            "authorization": f'Bearer {self.__api_key}',
            "Content-Type": "application/json"
        }
        r = requests.get(endpoint, headers=headers)
        if r.status_code == 200:
            return r
        else:
            print('Ошибка соединения')
            exit()

    def get_data(self):
        c = self._connect()
        return c.json()

    def get_fields(self):
        """ Получаем название всех полей по ключу 'fields' """
        data = self.get_data()
        if data:
            try:
                count = len(self.get_all_id())
                for i in range(0, count):
                    while len(data['records'][i]['fields'].keys()) != count:
                        return list(data['records'][i]['fields'].keys())
                    break
            except:
                print('Не удалось получить данные')
                exit()

    def get_all_id(self):
        """Получаем все id записей"""
        data = self.get_data()
        if data:
            try:
                ids = [item['id'] for item in data['records']]
                return ids
            except:
                print('Не удалось получить данные')
                exit()

    def get_records(self):
        """Получаем список словарей очищенных от лишних элементов,
            если нет ключа, то добавляет """
        print('Подключение')
        data = self.get_data()
        print('Получение данных')
        if data['records']:
            print('Данные получины')
            items = data['records']
            result = []

            for item in items:
                id = item['id']
                fields = item['fields'].items()
                keys = item['fields'].keys()
                res = {}
                res['id'] = id

                '''Проверяем наличие всех ключей'''
                if len(keys) < len(self.get_fields()):
                    print('Проверка полей')
                    for num in self.get_fields():
                        if num not in keys:
                            item['fields'][num] = None

                print('Формируем список', '\n', f'{item}')

                '''Формируем очищенный список'''
                for field in fields:
                    if isinstance(field[1], list):
                        value = field[1]
                        if 'url' in value[0]:
                            url = value[0].get('url')
                            res[field[0]] = url
                        else:
                            res[field[0]] = field[1]
                    else:
                        res[field[0]] = field[1]

                result.append(res)
            print(f'Список получен, {len(items)} объектов')
            return result
        else:
            print('Нет данных')
            exit()


class Num(object):
    """Данный код не масштабируем. Данный класс создан исключительно для читаемости кода"""

    def update(self, item):
        profiles_local = Profile.objects.get(id=item['id'])
        skills = list(profiles_local.methods.values_list('title', flat=True))
        fields_airtable = item.values()

        if profiles_local.name not in fields_airtable or profiles_local.photo not in fields_airtable:
            Profile.objects.filter(id=item['id']).update(photo=item['Фотография'], name=item['Имя'])

        for method in item['Методы']:
            if method not in skills:
                skill = Skills.objects.get_or_create(title=method)
                profiles_local.methods.add(skill[0])
            else:
                for skill_item_local in skills:
                    if skill_item_local not in item['Методы']:
                        profiles_local.methods.filter(title=skill_item_local).delete()

    def create(self, item):
        """New profile"""
        try:
            print('Запись нового объекта')
            new_profile = Profile.objects.create(id=item['id'], photo=item['Фотография'], name=item['Имя'])
            for method in item['Методы']:
                skill = Skills.objects.get_or_create(title=method)
                new_profile.methods.add(skill[0])
        except:
            print('Объект не создался')

    def check(self, item=None, required_fields=[]):
        for i in item:
            if not item[i]:
                print(f"Это поле необходимо заполнить {i} в {item['id']}")
                return True
        return False


n = Num()
a = Airtable(AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME, AIRTABLE_YOUR_API_KEY)
items = a.get_records()
Launch.objects.create(data=a.get_data())

for item in items:

    if n.check(item=item, required_fields=['Методы', 'Фотография', 'Имя']):
        exit()
    else:
        profile = Profile.objects.filter(id=item['id'])
        if not profile:
            '''New profile'''
            n.create(item)
        else:
            '''Update profile'''
            n.update(item)

'''Delete profile local db if not in Airtable'''
profiles_local = Profile.objects.all()
profiles_airtable = a.get_all_id()

if profiles_local.count() != len(profiles_airtable):
    for pl in profiles_local:
        if pl.id not in profiles_airtable:
            pl.delete()
            print(f'удалена запись {pl.id} - {pl.name}')
