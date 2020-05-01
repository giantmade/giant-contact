from ..cms_apps import ContactApp


class EventsAppTest:
    """
    Test case for the EventsApp
    """

    def test_get_urls_method(self):
        """
        Test get_urls method on the ContactApp class
        """

        assert ContactApp().get_urls() == ["contact.urls"]
