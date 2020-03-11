from uuid import uuid4
from django.db import models
from helpers.misc import get_url_friendly

class seller(models.models):
  #  "Information about the seller"
    name_book = models.CharField(max_length=50, editable=False, null=True)
    shotr_des = models.CharField(max_length=250, blank=True)
    genre = models.CharField(max_length=50, blank=True)
    publisher = models.CharField(max_length=50, blank=True)
    name_seller = models.CharField(max_length=50, editable=False, null=True)
    author = models.CharField(max_length=50, editable=False, null=True)
    isbn= models.UUIDField(primary_key=True, default=uuid4, editable=False)
    contact_no= models.UUIDField(primary_key=True, default=uuid4, editable=False)
    def __book__(self):
        return self.name_book
    def __author__(self):
        return self.author
class borrower:
   # "Informaiton about the borrower"
    name_book=models.CharField(max_length=50, editable=False, null=True)
    author=models.CharField(max_length=50, editable=False, null=True)
    name_borrower=models.CharField(max_length=50, editable=False, null=True)
    contact_no=models.UUIDField(primary_key=True, default=uuid4, editable=False)
    def __book__(self):
        return self.name_book
    def __author__(self):
       return self.author
class author:
  #  "list of classes which have same author in seller class"
    author=models.CharField(max_length=50, editable=False, null=True)
    def __init__(self,author):
        self.author=author
    a=models.list()
    def assign(self,b):
        if self.author==b._author_():
            a.append(b)
    
#a contains the list of sellers who have books with the searched author name