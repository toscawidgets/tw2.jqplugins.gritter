
# TW2 proper imports
import tw2.core as twc

import simplejson

jquery_gritter_js = twc.JSLink(
    modname='tw2.jqplugins.gritter',
    filename='static/jquery/gritter/js/jquery.gritter.min.js'
)
jquery_gritter_css = twc.CSSLink(
    modname='tw2.jqplugins.gritter',
    filename='static/jquery/gritter/css/jquery.gritter.css'
)
jquery_gritter_dir = twc.DirLink(
    modname='tw2.jqplugins.gritter',
    filename='static/jquery/gritter/images'
)

gritter_resources = [
    jquery_gritter_js,
    jquery_gritter_css,
    jquery_gritter_dir,
]

def gritter_callback(**kw):
    """ Return js_callbacks that create gritter popups.

    >>> gritter_callback(title="Some Title", text="A message...")

    """
    json = simplejson.dumps(kw)
    return twc.js_callback('function() { $.gritter.add(%s); }' % json)
