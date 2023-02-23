"""Unit test for validate."""
# tests/core/test_validate.py

# Unit under test:
import dem.core.dev_env_setup as dev_env_setup

import tests.fake_data as fake_data
from unittest.mock import patch
import json
import pytest
from dem.core.exceptions import InvalidDevEnvJson

@patch("dem.core.validate.get_deserialized_dev_env_json")
@patch("dem.core.validate.__supported_dev_env_major_version__", 0)
def test_validate_dev_env_json_with_invalid_version(mock_get_deserialized_dev_env_json):
    excepted_error_message = "Error in dev_env.json: The dev_env.json version v1.0 is not supported."

    with pytest.raises(InvalidDevEnvJson) as expected_exception_info:
        dev_env_setup.DevEnvSetup(json.loads(fake_data.invalid_version_dev_env_json))
    assert str(expected_exception_info.value) == excepted_error_message

@patch("dem.core.validate.get_deserialized_dev_env_json")
@patch("dem.core.validate.__supported_dev_env_major_version__", 0)
def test_validate_dev_env_json_with_valid_version(mock_get_deserialized_dev_env_json):
    dev_env_setup.DevEnvSetup(json.loads(fake_data.dev_env_json))