# urls.py

from django.conf.urls import handler404

handler404 = 'notfound.views.my_custom_page_not_found_view'
