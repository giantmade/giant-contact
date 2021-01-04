import pytest

from contact import models


@pytest.fixture
def enquiry_instance():
    return models.Enquiry(name="John Doe", email="john@doe.com",)
