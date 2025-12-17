from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutuser, name="logout"),
    path('profile/', views.userprofile, name="profile"),
    path('update/', views.updateuser, name="update"),
    path('signup/', views.registerpage, name="signup"),
    path('',views.index,name='index'),
    path('culture.html',views.culture,name='culture'),
    path('states_selection.html',views.states_selection,name='states_selection'),
    path('ecommerce.html',views.ecommerce,name='ecommerce'),

    path('FCAI.html',views.FCAI,name='FCAI'),

    path('food.html',views.food,name='food'),

    path('harvest_festivals.html',views.harvest_festivals,name='harvest_festivals'),

    path('karnataka.html',views.karnataka,name='karnataka'),

    path('MAH_festivals.html',views.MAH_festivals,name='MAH_festivals'),

    path('maha_clothing_dance_lang.html',views.maha_clothing_dance_lang,name='maha_clothing_dance_lang'),

    path('mahaculture.html',views.mahaculture,name='mahaculture'),

    path('maha_trad.html',views.maha_trad,name='maha_trad'),

     path('maharashtra.html',views.maharashtra,name='maharashtra'),

    path('religions.html',views.religions,name='religions'),

    path('UttarPradesh.html',views.UttarPradesh,name='UttarPradesh'),

    path('shaniwarwada_hotel.html',views.shaniwarwada_hotel,name='shaniwarwada_hotel'),

    path('agakhan_hotel.html',views.agakhan_hotel,name='agakhan_hotel'),

    path('Raigadh_hotel.html',views.Raigadh,name='Raigadh_hotel'),

    path('TajMahal_hotel.html',views.TajMahal_hotel,name='TajMahal_hotel'),

    path('add_to_cart/<pk>',views.add_to_cart,name="add_to_cart"),

    path('order_list_cart.html',views.order_list_cart,name="order_list_cart"),

    path('add_item/<int:pk>',views.add_item,name="add_item"),

     path('remove_item/<int:pk>',views.remove_item,name="remove_item"),

     path('checkout',views.checkout,name='checkout')
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)