from django.db import models
from acc.models import User

class Table(models.Model):
    작성자 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='작성자')
    주소 = models.TextField()    # 주소
    면적 = models.CharField(max_length=100)
    가격 = models.CharField(max_length=100)
    종류 = models.CharField(max_length=100)
    층수 = models.CharField(max_length=100)
    입주가능일 = models.CharField(max_length=100)
    방수 = models.CharField(max_length=100)
    사용승인 = models.CharField(max_length=100)
    난방 = models.CharField(max_length=100)
    방향 = models.CharField(max_length=100)
    비고 = models.CharField(max_length=100)
    주차 = models.CharField(max_length=100)

    def __str__(self):
        return self.주소
    


