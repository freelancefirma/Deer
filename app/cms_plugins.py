# app/cms_plugins.py
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _
from .models import MyPluginModel

class MyPluginPublisher(CMSPluginBase):
    model = MyPluginModel
    module = _("My App Plugins")
    name = _("My Plugin")
    render_template = "app/plugin_template.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(MyPluginPublisher)
