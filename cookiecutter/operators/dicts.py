# -*- coding: utf-8 -*-

"""Operator plugin that inherits a base class and is made available through `type`."""
from __future__ import unicode_literals
from __future__ import print_function

import logging
from typing import Union, Dict, List

from cookiecutter.operators import BaseOperator
from cookiecutter.config import merge_configs

logger = logging.getLogger(__name__)


class DictUpdateOperator(BaseOperator):
    """
    Operator for updating dict objects with items.

    :param src: The input dict to update
    :param input: A dict or list of dicts to update the input `src`
    :return: An updated dict object.
    """

    type: str = 'update'

    input: Union[Dict, List[Dict]]
    src: Dict

    def execute(self):
        if isinstance(self.input, list):
            for i in self.input:
                self.src.update(i)
        else:
            self.src.update(self.input)

        return self.src


class DictMergeOperator(BaseOperator):
    """
    Operator for recursively merging dict objects with input maps.

    :param src: The input dict to update
    :param input: A dict or list of dicts to update the input `dict`
    :return: An updated dict object.
    """

    type: str = 'merge'
    input: Union[Dict, List[Dict]]
    src: Dict

    def execute(self):
        if isinstance(self.input, list):
            for i in self.input:
                self.src = merge_configs(self.src, i)
            return self.src
        else:
            return merge_configs(self.src, self.input)


class DictPopOperator(BaseOperator):
    """
    Operator for recursively merging dict objects with input maps.

    :param src: The input dict to update
    :param item: A list or string of items to remove from a dictionary or list
    :return: An updated dict object.
    """

    type: str = 'pop'

    item: Union[Dict, List[str], str]
    src: Dict

    def execute(self):
        if isinstance(self.item, list):
            for i in self.item:
                self.src.pop(i)
            return self.src
        else:
            self.src.pop(self.item)
            return self.src
