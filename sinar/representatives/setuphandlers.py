from collective.grok import gs
from sinar.representatives import MessageFactory as _

@gs.importstep(
    name=u'sinar.representatives', 
    title=_('sinar.representatives import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('sinar.representatives.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
