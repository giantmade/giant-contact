from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register
class ContactApp(CMSApp):
    """
    Apphook for contact enquiries
    """

    name = "Contact"
    app_name = "contact"

    def get_urls(self, page=None, language=None, **kwargs):
        """
        Return urls for this app
        """
        return ["contact.urls"]
