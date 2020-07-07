# -*- coding: utf-8 -*-

"""Tests dict input objects for `cookiecutter.operator.checkbox` module."""

import os
from cookiecutter.main import cookiecutter


def test_operator_checkbox_with_dict_and_name_key(monkeypatch, tmpdir):
    """Verify Jinja2 time extension work correctly."""
    monkeypatch.chdir(os.path.abspath(os.path.dirname(__file__)))

    # TODO: Need to properly test this with pty but it works now
    context_dict_ok = cookiecutter(
        '.', context_file='dict_ok.yaml', no_input=True, output_dir=str(tmpdir)
    )

    assert context_dict_ok

    context_string_ok = cookiecutter(
        '.', context_file='string_ok.yaml', no_input=True, output_dir=str(tmpdir)
    )

    assert context_string_ok