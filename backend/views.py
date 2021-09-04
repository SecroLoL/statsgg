from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache

# This reads public/index.html, which has <div id='root'> which then triggers the React app to display view
index = never_cache(TemplateView.as_view(template_name='index.html'))
