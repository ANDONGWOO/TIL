import sys
import os
from unicodedata import name
import django
sys.dont_write_bytecode = True
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import *

# 아래에 코드를 기록하세요.
# 코드 실행은 터미널에서 shell을 실행시켜서 해주세요. 
# $ python manage.py shell_plus 

Director.objects.create(name="봉준호",debut="1993-01-01",country="KOR")
Director.objects.create(name="김한민",debut="1999-01-01",country="KOR")
Director.objects.create(name="최동훈",debut="2004-01-01",country="KOR")
Director.objects.create(name="이정재",debut="1993-01-01",country="KOR")
Director.objects.create(name="이경규",debut="2022-01-01",country="KOR")
Director.objects.create(name="한재림",debut="2005-01-01",country="KOR")
Director.objects.create(name="Joseph Kosinski",debut="1999-01-01",country="KOR")
Director.objects.create(name="김철수",debut="2022-01-01",country="KOR")

a=Director.objects.get(id=24)
a.delete()
a=Director.objects.get(id=23)
a.delete()
a=Director.objects.get(id=22)
a.delete()
a=Director.objects.get(id=21)
a.delete()
a=Director.objects.get(id=20)
a.delete()
a=Director.objects.get(id=19)
a.delete()
a=Director.objects.get(id=18)
a.delete()
a=Director.objects.get(id=17)
a.delete()
a=Director.objects.get(id=16)
a.delete()
a=Director.objects.get(id=15)
a.delete()
a=Director.objects.get(id=14)
a.delete()
a=Director.objects.get(id=13)
a.delete()
a=Director.objects.get(id=12)
a.delete()
a=Director.objects.get(id=11)
a.delete()
a=Director.objects.get(id=10)
a.delete()
a=Director.objects.get(id=9)
a.delete()

c=Director.objects.get(id=1)
c.name="봉준호"
c.debut="1993-01-01"
c.country="KOR"
c.save()

b=Director.objects.get(id=8)
b.name="김철수"
b.debut="2022-01-01"
b.country="KOR"
b.save()

genre=Genre()
genre.title='액션'
genre.save()

genre=Genre()
genre.title='드라마'
genre.save()

genre=Genre()
genre.title='사극'
genre.save()

genre=Genre()
genre.title='범죄'
genre.save()

genre=Genre()
genre.title='스릴러'
genre.save()

genre=Genre()
genre.title='SF'
genre.save()

genre=Genre()
genre.title='무협'
genre.save()

genre=Genre()
genre.title='첩보'
genre.save()

genre=Genre()
genre.title='재난'
genre.save()

s=Director.objects.all()

for i in s:
    print(i.name,i.debut,i.country)

s=Director.objects.get(id=1)
print(s.name,s.debut,s.country)