#!/usr/bin/env python3

# Copyright 2023 (author: lamnguyenx)


# technical
from typing_extensions import Self
import dataclasses as dcl
import typing as tp


# parent
from ..black.lines import LinesBlock, Line
from ..black.mode import Mode
from ..black.blib2to3.pytree import Leaf
from ..black.blib2to3.pgen2 import token


# nice_utils
# import nice_utils as hnu; logger = hnu.getLogger(__name__)


### FUNCTIONS
def format_super_brackets(Inp_Lines_Blocks: tp.List[LinesBlock], mode: Mode):
    for b, Curr_Lines_Block in enumerate(Inp_Lines_Blocks):
        for i, line in enumerate(Curr_Lines_Block.content_lines):
            if line.leaves[-1].type in (token.LBRACE, token.LPAR, token.LSQB):
                pass
