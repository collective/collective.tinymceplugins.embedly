import logging

from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.interfaces import INonInstallable as INonInstallableProfiles
from Products.PortalTransforms.Transform import make_config_persistent
from zope.interface import implements


logger = logging.getLogger('collective.tinymceplugins.embedly.setuphandlers')


class HiddenProfiles(object):
    implements(INonInstallableProfiles)

    def getNonInstallableProfiles(self):
        return ['collective.tinymceplugins.embedly:uninstall'
                ]
        
        
def setup_portal_transforms(context):
    if not context.readDataFile('collective-tinymceplugins-embedly-default.txt'):
        return
    
    logger.info('Updating portal_transform safe_html settings')

    tid = 'safe_html'

    pt = getToolByName(context, 'portal_transforms')
    if not tid in pt.objectIds(): return

    trans = pt[tid]

    tconfig = trans._config
    
    tconfig['valid_tags']['iframe'] = '1'
    
    make_config_persistent(tconfig)
    trans._p_changed = True
    trans.reload()