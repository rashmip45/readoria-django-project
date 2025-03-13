from django.db import models

# Create your models here.

category = {
     "FICTION": "Fiction",
    "FANTASY": "Fantasy",
    "SCI_FI": "Science Fiction",
    "MYSTERY": "Mystery & Thriller",
    "ROMANCE": "Romance",
    "HORROR": "Horror",
    "HISTORICAL": "Historical Fiction",
    "ADVENTURE": "Adventure",
    "DYSTOPIAN": "Dystopian",
    "CONTEMPORARY": "Contemporary",
    "CLASSIC": "Classic Literature",
    "GRAPHIC_NOVEL": "Graphic Novel",
    "SHORT_STORIES": "Short Stories",
    "POETRY": "Poetry",
    "YOUNG_ADULT": "Young Adult",
    "CHILDRENS": "Children’s Books",
    "NON_FICTION": "Non-Fiction",
    "BIOGRAPHY": "Biography & Memoir",
    "SELF_HELP": "Self-Help",
    "BUSINESS": "Business & Finance",
    "SCIENCE": "Science & Technology",
    "HISTORY": "History",
    "PHILOSOPHY": "Philosophy",
    "RELIGION": "Religion & Spirituality",
}
class Book(models.Model):
    title = models.CharField(max_length=20,null=False)
    genre = models.CharField(choices=category,max_length=20,null=False)
    author = models.CharField(max_length=25,null=False)

    