from django.db import models

# Create your models here.

class Blog(models.Model): #models.Model 프레임워크 틀. 장고는 프레임워크 - 이건 장고의 규칙!!
    title = models.CharField(max_length=200) #문자열인데 200자가 최대
    mydate = models.DateTimeField('date published') #쓴 날짜는 datetime 여기서오류날거같아아앙
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]