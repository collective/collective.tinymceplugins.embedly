import re

from Products.PortalTransforms.transforms.safe_html import StrippingParser


# Monkey patches Products.PortalTransforms.transforms.safe_html.StrippingParser.entity_or_charref
# This works around issue https://github.com/plone/Products.PortalTransforms/pull/1
# collective.monkeypatcher cannot do this.
# See https://github.com/plone/collective.monkeypatcher/pull/2
StrippingParser.entity_or_charref__old__ = StrippingParser.entity_or_charref  
StrippingParser.entity_or_charref = re.compile(r'$.')