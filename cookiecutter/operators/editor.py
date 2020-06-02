# -*- coding: utf-8 -*-

"""Functions for generating a project from a project template."""
from __future__ import unicode_literals
from __future__ import print_function

import logging
from PyInquirer import prompt

from cookiecutter.operators import BaseOperator

logger = logging.getLogger(__name__)


class InquirerEditorOperator(BaseOperator):
    """Operator for PyInquirer type prompts."""

    type = 'editor'

    def __init__(self, operator_dict, context=None):
        """Initialize PyInquirer Hook."""  # noqa
        super(InquirerEditorOperator, self).__init__(
            operator_dict=operator_dict, context=context
        )

    def execute(self):
        """Run the prompt."""  # noqa
        if 'name' not in self.operator_dict:
            self.operator_dict.update({'name': 'tmp'})
            return prompt([self.operator_dict])['tmp']
        else:
            return prompt([self.operator_dict])
