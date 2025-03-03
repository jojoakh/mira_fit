from .forms import NewsletterForm
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.safestring import mark_safe


def newsletter_form(request):
    """
    Handles the newsletter form submission,
    validating input and providing feedback messages to the user.

    :param request: HttpRequest object representing the client request.
    :return: Dictionary containing the newsletter form to be used
    in the context.
    """
    form = NewsletterForm()

    if request.method == 'POST' and request.POST.get(
                                'form_type') == 'newsletter':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            subscriber = form.save()
            messages.success(
                request,
                mark_safe(f'Thank you for subscribing, {subscriber.email}!'),
                extra_tags='newsletter'
            )
            return redirect(request.path)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(
                        request,
                        f"{field.capitalize()}: {error}",
                        extra_tags='newsletter'
                    )

    return {'newsletter_form': form}
