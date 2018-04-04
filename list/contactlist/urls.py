from django.conf.urls import url
from contactlist import views
#from django.views.decorators.csrf import csrf_exempt



urlpatterns = [

    url(r'contact-list/$', views.ContactList.as_view()),
    url(r'contactlist/(?P<pk>[\d-]+)/$', views.ContactDetails.as_view()),
    url(r'request/$', views.index, name='index'),
    #url(r'^api/v1/some-resource$', csrf_exempt(ContactDetails.as_view())),

    #url(r'home$', direct_to_template, {"template": "Newtask/contactlist.html"})

]



