"""Pytest session configuration."""
import ee
import pytest

import pytest_gee


def pytest_configure():
    """Init GEE in the test environment."""
    pytest_gee.init_ee_from_token()


@pytest.fixture(scope="session")
def test_folder(gee_hash):
    """Create a test folder for the test session."""
    structure = {
        "folder": {
            "image": ee.Image(1),
            "fc": ee.FeatureCollection(ee.Geometry.Point([0, 0])),
        }
    }
    folder = pytest_gee.init_tree(structure, gee_hash)

    return folder
