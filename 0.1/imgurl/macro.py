"""
Img URL macro
Bitelxux 2016
"""

from genshi.builder import tag
from trac.util.translation import cleandoc_
from trac.wiki.macros import WikiMacroBase
from trac.wiki.api import parse_args


class ImgURLMacro(WikiMacroBase):
    _description = cleandoc_(
    """Image from URL macro.

    [[ImgURL(url[, width=<width>, height=<height>, align=left|center|right])]]

    Example
    -------

    .. code::
       [[ImgURL(https://s6.postimg.org/bbx4clrsx/batteries_included.png, width=50%, align=center)]]

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
        params['align'] = args_dict.get('align', '')

        return tag.p(tag.image(src=img,
                               width=params['width'],
                               eight=params['eight'],
                               align=params['align']
                              ),
                     style="text-align:%s;" % params['align'])
