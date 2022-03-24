from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Event, Review
from accounts.models import UserProfile


def check_if_user_profile(request):
    if request.user.is_authenticated:
        [profile, created] = UserProfile.objects.get_or_create(
            user=request.user)
        return profile


@login_required
def add_attending(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == "POST":
        request.user.profile.attending.add(event)
    return redirect(request.POST.get("redirect_url"))


@login_required
def remove_attending(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == "POST":
        request.user.profile.attending.remove(event)
    return redirect(request.POST.get("redirect_url"))


@login_required
def dashboard(request):
    today = datetime.today()
    profile = check_if_user_profile(request)

    attending = profile.attending.all().filter(
        datetime__gte=today).order_by("datetime")
    attended = profile.attending.all().filter(
        datetime__lt=today).order_by("datetime")
    return render(request, 'events/dashboard.html', {"attending": attending, "attended": attended})


@login_required
def add_review(request, id):
    if request.method == "POST":
        event = get_object_or_404(Event, id=id)
        [profile, created] = UserProfile.objects.get_or_create(
            user=request.user)

        text = request.POST.get("review-text")
        rating = request.POST.get("rating")
        review = Review.objects.create(
            text=text, rating=rating, event=event, profile=profile)
        event.reviews.add(review)

        return redirect(request.POST.get("redirect_url"))


def details(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'events/details.html', {'event': event})


def list(request):
    check_if_user_profile(request)

    today = datetime.today()

    filter_map = {
        'title': 'title__icontains',
        'is_free': 'cost__exact'
    }

    filters = {}
    for key, value in request.GET.items():
        filter_key = filter_map[key]
        filters[filter_key] = value

    events = Event.objects.filter(
        datetime__gte=today).filter(**filters).order_by('datetime')
    return render(request, 'events/list.html', {'events': events})
