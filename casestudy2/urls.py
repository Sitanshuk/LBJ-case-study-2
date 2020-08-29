from django.contrib import admin
from django.urls import re_path, path
from .views import (
	main,
	add,
	search,
	display,
	)

urlpatterns = [
	re_path(r'^$', main, name = 'main'),
	re_path(r'^add-student$', add, name = 'add'),
	re_path(r'^search-student$', search, name = 'search'),
	re_path(r'^display-all-student$', display, name = 'display'),
]