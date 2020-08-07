import xadmin
from .models import *

class FriendLinksAdmin(object):
    list_display = ['id','name','link']
    model_icon = 'fa fa-link'


class SeoAdmin(object):
    list_display = ['id','title','description','keywords']
    model_icon = 'fa fa-globe'


class CustomCodeAdmin(object):
    list_display = ['id','statistics']
    model_icon = 'fa fa-code'


class SiteInfoAdmin(object):
    list_display = ['id','created_time','record_info']
    model_icon = 'fa fa-info-circle'


class SocialAdmin(object):
    list_display = ['id','github','instagram','facebook']
    model_icon = 'fa fa-github'

xadmin.site.register(FriendLinks,FriendLinksAdmin)
xadmin.site.register(Seo,SeoAdmin)
xadmin.site.register(CustomCode,CustomCodeAdmin)
xadmin.site.register(SiteInfo,SiteInfoAdmin)
xadmin.site.register(Social,SocialAdmin)
