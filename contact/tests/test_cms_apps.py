import pytest
from contact.cms_apps import ContactApp


@pytest.mark.requires_django_project
class TestEventsApp:
    """
    Test case for the EventsApp
    """

    def test_get_urls_method(self):
        """
        Test get_urls method on the ContactApp class
        """

        assert ContactApp().get_urls() == ["contact.urls"]
