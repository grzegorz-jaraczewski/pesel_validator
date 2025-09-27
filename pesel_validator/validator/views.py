from django.shortcuts import render
from validator.forms import PeselForm
from validator.utils import validate_pesel


def home(request):
    """
    Handle the homepage view for PESEL validation.

    - On GET: renders an empty PESEL form.
    - On POST: processes the submitted form, validates the PESEL number,
      and returns the validation result.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Rendered HTML response with:
            - "form": the PESEL input form (empty or bound).
            - "output": validation result dict if PESEL submitted,
                        otherwise None.
    """
    output = None
    if request.method == "POST":
        form = PeselForm(request.POST)
        if form.is_valid():
            pesel = form.cleaned_data.get("pesel", "Unknown")
            output = validate_pesel(pesel)
    else:
        form = PeselForm()

    return render(
        request=request,
        template_name="validator/home.html",
        context={"form": form, "output": output}
    )
