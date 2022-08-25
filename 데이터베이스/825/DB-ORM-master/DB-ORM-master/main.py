import sys
import os
from turtle import title
import django
sys.dont_write_bytecode = True
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import *

# 아래에 코드를 기록하세요.
# 코드 실행은 터미널에서 shell을 실행시켜서 해주세요. 
# $ python manage.py shell_plus 

name1=Director.objects.get(name='봉준호')
print('id :',name1.id)
print('name :',name1.name)
print('debut:',name1.debut)
print('country :',name1.country)

title1=Genre.objects.get(title='드라마')

print('id :',title1.id)
print('title :',title1.title)

director_ = Director.objects.get(name='봉준호')

genre_ = Genre.objects.get(title='드라마')

movie = Movie()

movie.director_id=director_.id
movie.genre_id=genre_.id
movie.title='기생충'
movie.opening_date='2019-05-30'
movie.running_time=132
movie.screening= False
movie.save()

movies = [
    ("봉준호", "드라마", "괴물", "2006-07-27", 119, False),
    ("봉준호", "SF", "설국열차", "2013-10-30", 125, False),
    ("김한민", "사극", "한산", "2022-07-27", 129, True),
    ("최동훈", "SF", "외계+인", "2022-07-20", 142, False),
    ("이정재", "첩보", "헌트", "2022-08-10", 125, True),
    ("이경규", "액션", "복수혈전", "1992-10-10", 88, False),
    ("한재림", "재난", "비상선언", "2022-08-03", 140, True),
    ("Joseph Kosinski", "액션", "탑건 : 매버릭", "2022-06-22", 130, True),
]

for i in range(len(movies)):
    movie = Movie()
    director_ = Director.objects.get(name=movies[i][0])
    genre_ = Genre.objects.get(title=movies[i][1])
    movie.director_id=director_.id
    movie.genre_id=genre_.id
    movie.title=movies[i][2]
    movie.opening_date=movies[i][3]
    movie.running_time=movies[i][4]
    movie.screening=movies[i][5]
    movie.save()




id_1=Movie.objects.get(id=1)
name1=Director.objects.get(name='봉준호')
title1=Genre.objects.get(title='드라마')
id_2=Movie.objects.get(id=2)
name2=Director.objects.get(name='봉준호')
title2=Genre.objects.get(title='드라마')
id_3=Movie.objects.get(id=3)
name3=Director.objects.get(name='봉준호')
title3=Genre.objects.get(title='SF')
id_4=Movie.objects.get(id=4)
name4=Director.objects.get(name='김한민')
title4=Genre.objects.get(title='사극')
id_5=Movie.objects.get(id=5)
name5=Director.objects.get(name='최동훈')
title5=Genre.objects.get(title='SF')
id_6=Movie.objects.get(id=6)
name6=Director.objects.get(name='이정재')
title6=Genre.objects.get(title='첩보')
id_7=Movie.objects.get(id=7)
name7=Director.objects.get(name='이경규')
title7=Genre.objects.get(title='액션')
id_8=Movie.objects.get(id=8)
name8=Director.objects.get(name='한재림')
title8=Genre.objects.get(title='재난')
id_9=Movie.objects.get(id=9)
name9=Director.objects.get(name='Joseph Kosinski')
title9=Genre.objects.get(title='액션')
print(name1.name,title1.title,id_1.title,id_1.opening_date,id_1.running_time,id_1.screening
,name2.name,title2.title,id_2.title,id_2.opening_date,id_2.running_time,id_2.screening
,name3.name,title3.title,id_3.title,id_3.opening_date,id_3.running_time,id_3.screening
,name4.name,title4.title,id_4.title,id_4.opening_date,id_4.running_time,id_4.screening
,name5.name,title5.title,id_5.title,id_5.opening_date,id_5.running_time,id_5.screening
,name6.name,title6.title,id_6.title,id_6.opening_date,id_6.running_time,id_6.screening
,name7.name,title7.title,id_7.title,id_7.opening_date,id_7.running_time,id_7.screening
,name8.name,title8.title,id_8.title,id_8.opening_date,id_8.running_time,id_8.screening
,name9.name,title9.title,id_9.title,id_9.opening_date,id_9.running_time,id_9.screening)

