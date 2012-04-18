import json
from urllib import urlencode
from urllib2 import urlopen
from urllib2 import HTTPError

from collective.embedly.interfaces import IEmbedlySettings
from plone.memoize.view import memoize_contextless
from plone.registry.interfaces import IRegistry
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from zope.component import getUtility

from collective.tinymceplugins.embedly.config import API_ROOT
    
    
class EmbedlyConfigurationJSSnippet(BrowserView):
    
    @memoize_contextless
    def _get_settings(self):
        registry = getUtility(IRegistry)
        return registry.forInterface(IEmbedlySettings)
    
    def get_api_key(self):
        return self._get_settings().api_key
    
    @memoize_contextless
    def has_feature(self, feature_name):
        params = urlencode({
            'feature': feature_name,
            'key': self.get_api_key()
        })
        url = '%s/feature?%s' % (API_ROOT, params)
        
        try:
            resp = urlopen(url, timeout=5)
            try:
                resp_data = json.loads(resp.read())
            except ValueError:
                return False
        except HTTPError:
            return False
        
        return resp_data.get(feature_name, False)
    
    def __call__(self, *args, **kwargs):
        self.request.response.content_type = 'text/javascript'
        portal_url = getToolByName(self.context, 'portal_url')()
        plugin_root = '%s/tinymce_embedly' % (portal_url)
        endpoint = self.has_feature('preview') and 'preview' or ''
        settings = {
            'plugin_root': plugin_root,
            'api_key': self.get_api_key(),
            'endpoint': endpoint
        }
        return """EMBEDLY_TINYMCE = '%(plugin_root)s'; embedly_key = '%(api_key)s'; embedly_endpoint = '%(endpoint)s';""" % settings