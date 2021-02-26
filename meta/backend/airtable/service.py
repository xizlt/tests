from local_settings import AIRTABLE_TABLE_NAME, AIRTABLE_BASE_ID, AIRTABLE_YOUR_API_KEY
from backend.wsgi import *
import requests
from api.models import Profile, Skills, Launch

endpoint = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'
headers = {
    "authorization": f'Bearer {AIRTABLE_YOUR_API_KEY}',
    "Content-Type": "application/json"
}
airtable_records = []
r = requests.get(endpoint, headers=headers)
airtable_response = r.json()
airtable_records += (airtable_response['records'])


def airtableConnect(data):
    ind = [i['id'] for i in data]
    profile_ind = list(Profile.objects.values_list('id', flat=True))
    ind_exclude = list(set(profile_ind) - set(ind))

    # Check profile in airtable. If not then delete
    if ind_exclude:
        for i in ind_exclude:
            Profile.objects.get(id=i).delete()

    # get profiles
    for item in data:

        ids = item['id']
        fields = item['fields']

        try:
            profile = Profile.objects.get(id=ids)
            skills_loc = profile.methods.values_list('id', flat=True)

            # check 'Методы' - writing
            for title_methods_air in fields['Методы']:
                skill_loc = Skills.objects.get_or_create(title=title_methods_air)

                if skill_loc[0].id not in skills_loc:
                    profile.methods.add(skill_loc[0].id)

            # check 'Методы' if not in Profile - dell
            for sk in profile.methods.values_list('title', flat=True):
                if sk not in fields['Методы']:
                    profile.methods.filter(title=sk).delete()

            # update profile
            if profile.name != fields['Имя'] or profile.photo != fields['Фотография'][0]['url']:
                profile.name = fields['Имя']
                profile.photo = fields['Фотография'][0]['url']
                profile.save()

        except:
            # Create new profile
            p = Profile.objects.create(id=ids, name=fields['Имя'], photo=fields['Фотография'][0]['url'])
            for method in fields['Методы']:
                m = Skills.objects.get_or_create(title=method)
                p.methods.add(m[0].id)


if r.status_code == 200:
    if __name__ == '__main__':
        Launch.objects.create(data=airtable_records)
        airtableConnect(airtable_records)
else:
    print(f'не удалось соединиться. Код сервера {r.status_code}')
