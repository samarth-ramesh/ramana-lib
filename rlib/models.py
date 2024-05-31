from django.contrib import admin
from django.db import models

# Create your models here.

class Book(models.Model):
    BookId = models.AutoField(primary_key=True)
    BookTitle = models.CharField(max_length=255)
    Description = models.TextField()
    Author = models.CharField(max_length=255)
    Category = models.CharField(max_length=255)
    Volume = models.CharField(max_length=255, null=True, blank=True)
    Language = models.CharField(max_length=255)
    OldShelfCode = models.CharField(max_length=255)
    OldAccNo = models.CharField(max_length=255)
    Publisher = models.CharField(max_length=255)
    YearOfPublication = models.CharField(max_length=10)
    NewShelfCode = models.CharField(max_length=255, null=True, blank=True)
    Checked = models.CharField(max_length=255, null=True, blank=True)
    ISBN = models.CharField(max_length=255)
    Status = models.CharField(max_length=255, default='Available', choices=[('Available', 'Available'), ('Damaged', 'Damaged'), ('Lost', 'Lost')])


    def __str__(self):
        return self.BookTitle
