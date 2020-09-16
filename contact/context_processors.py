from .forms import EnquiryForm


def enquiry_form(request):
    return {"enquiry_form": EnquiryForm()}
