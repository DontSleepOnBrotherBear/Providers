

from django.contrib import admin
from .models import Post
from .models import Provider
from .models import Address
from .models import Friend

admin.site.register(Post)
admin.site.register(Provider)
admin.site.register(Address)
admin.site.register(Friend)


