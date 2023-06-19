import os
import django



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "python_meetup_django.settings")
django.setup()
from bot.models import Book

book = Book(title='Sample Book', author='John Doe', publication_date='2022-01-01')
book.save()
