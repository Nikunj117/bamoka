from django.urls import path
from .views import *
from django.conf.urls import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sitemaps.views import sitemap
# from app_blog.sitemap import AllBlogsSitemap, HomeSitemap, TagSitemap

# sitemaps = {
#     "posts": AllBlogsSitemap,
#     'home': HomeSitemap,
#     'tags': TagSitemap,
# }

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('contact',ContactView.as_view(),name='contact'),
    path('about',AboutUS.as_view(),name='about'),
    path('applcation',Applcation.as_view(),name='applcation'),
    path('splitguargum',SplitguargumProduct.as_view(),name='splitguargum'),
    path('churiproduct',ChuriProduct.as_view(),name='churiproduct'),
    path('fastHydrationproduct',FastHydrationProduct.as_view(),name='fastHydrationproduct'),
    path('foodgradeproduct',FoodGradeProduct.as_view(),name='foodgradeproduct'),
    path('industrialgradeproduct',IndustrialGradeProduct.as_view(),name='industrialgradeproduct'),
    path('kormaproduct',KormaProduct.as_view(),name='kormaproduct'),
    path('packagingstorage',PackagingStorage.as_view(),name='packagingstorage'),
    path('qualitycontrol',QualityControl.as_view(),name='qualitycontrol'),
   
    # path('robots.txt', RobotsTxtView.as_view(), name='robots.txt'),
    # path('cookie-policy/', cookies.as_view(), name='cookie-policy'),
    # path('privacy-policy/', policy.as_view(), name='privacy-policy'),
    # path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"), 
]


