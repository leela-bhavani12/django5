from django.urls import path,include
from .views import *
urlpatterns=[
    path('home',home,name="home"),
    path('flights',flights,name="flights"),
    path('BookNow',BookNow,name="BookNow"),
    path('Contact',Contact,name="Contact"),
    path('Login',Login,name="Login"),
    path('Details',Details,name="Details"),
    path('CalFare',CalFare,name="CalFare"),
    path('Destinations',Destinations,name="Destinations"),
    path('AboutUs',AboutUs,name="AboutUs"),
    path('booknow', flightrender2, name="Booking"),
    path('Search',Search,name="Search"),
    path('Submit',Submit,name="Submit"),
    path('otp',otp,name="otp"),
    path('Card',Card,name="Card")

]