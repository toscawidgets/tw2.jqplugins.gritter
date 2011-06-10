
# TW2 proper imports
import tw2.core as twc

jquery_gritter_js = twc.JSLink(
    modname=__file__,
    filename='static/jquery/gritter/js/jquery.gritter.min.js'
)
jquery_gritter_css = twc.CSSLink(
    modname=__file__,
    filename='static/jquery/gritter/css/jquery.gritter.css'
)
jquery_gritter_dir = twc.JSLink(
    modname=__file__,
    filename='static/jquery/gritter/img'
)

gritter_resources = [
    jquery_gritter_js,
    jquery_gritter_css,
    jquery_gritter_dir,
]
