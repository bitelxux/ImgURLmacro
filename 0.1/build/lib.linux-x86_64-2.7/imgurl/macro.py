"""Img URL macro"""

from genshi.builder import tag
from trac.util.translation import cleandoc_
from trac.wiki.macros import WikiMacroBase
from trac.wiki.api import parse_args
import requests
import json
import random


class ImgURLMacro(WikiMacroBase):
    _description = cleandoc_(
    """Image from URL macro.

    Note that the name of the class is meaningful:
     - it must end with "Macro"
     - what comes before "Macro" ends up being the macro name

    The documentation of the class (i.e. what you're reading)
    will become the documentation of the macro, as shown by
    the !MacroList macro (usually used in the WikiMacros page).
    """)

    def expand_macro(self, formatter, name, args):
        """Return some output that will be displayed in the Wiki content.

        `name` is the actual name of the macro (no surprise, here it'll be
        `'HelloWorld'`),
        `content` is the text enclosed in parenthesis at the call of the
          macro. Note that if there are ''no'' parenthesis (like in, e.g.
          [[HelloWorld]]), then `content` is `None`.
        `args` will contain a dictionary of arguments when called using the
          Wiki processor syntax and will be `None` if called using the
          macro syntax.
        """

        params = {}
        # Split the args
        args_list, args_dict = parse_args(args)

        img = args_list[0]
        params['eight'] = args_dict.get('eight', '')
        params['width'] = args_dict.get('width', '')

        return tag.image(src=img,
                         width=params['width'],
                         eight=params['eight'])

    # Note that there's no need to HTML escape the returned data,
    # as the template engine (Genshi) will do it for us.
