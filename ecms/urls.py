from django.conf.urls.defaults import *
from ecms.views.cmspageview import CmsPageView

# The URLs of the cmspage are forced to end with a slash,
# so django will redirect /admin will redirect to /admin/.
# The same trick also needs to be used in the main site
# which includes this file. Otherwise a rule matched after all.
urlpatterns = patterns('ecms.views',
    url(r'^$|^(?P<path>.*/)$', CmsPageView.as_view(), name='ecms-page')   # force urls to end with a slash
)
