

from django.urls import path
# rest router
from rest_framework.routers import SimpleRouter


from .views import UserList


router = SimpleRouter()
router.register('', UserList)

urlpatterns = router.urls
