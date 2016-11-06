"""Img URL macro"""

from genshi.builder import tag
from trac.util.translation import cleandoc_
from trac.wiki.macros import WikiMacroBase
from trac.wiki.api import parse_args


class ImgURLMacro(WikiMacroBase):
    _description = cleandoc_(
    """Image from URL macro.

    [[ImgURL(url[, width=<width>, height=<height>])]]

    """)

    def expand_macro(self, formatter, name, args):
        """Returns an image that will be displayed in the Wiki content.

        `name` is the actual name of the macro,
        `args` is the text enclosed in parenthesis at the call of the
          macro.
        """

        params = {}
        args_list, args_dict = parse_args(args)

        img = args_list[0]
        params['eight'] = args_dict.get('eight', '')
        params['width'] = args_dict.get('width', '')

        return tag.image(src=img,
                         width=params['width'],
                         eight=params['eight'])