from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test, login_required
from .forms import UserRegisterForm, UserUpdateForm, CustomAuthenticationForm, VocabularyForm
from .models import Profile, Vocabulary


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now logged in as {username}.')
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'form': form})


@login_required
def vocabulary(request):
    return render(request, 'users/vocabulary.html')


@user_passes_test(lambda user: not user.is_authenticated, login_url='profile')
def custom_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if 'remember_me' in request.POST:
                request.session.set_expiry(60 * 60 * 24 * 30)  # Сессия активна 30 дней
            else:
                request.session.set_expiry(0)  # Сессия будет закрыта при закрытии браузера

            return redirect('profile')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


@login_required
def vocabulary_view(request, phrase_id=None):
    if phrase_id:
        vocabulary_item = get_object_or_404(Vocabulary, id=phrase_id)
        form = VocabularyForm(request.POST or None, instance=vocabulary_item)
    else:
        form = VocabularyForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('vocabulary')

    vocabulary_list = Vocabulary.objects.all()
    return render(request, 'users/vocabulary.html', {'form': form, 'vocabulary_list': vocabulary_list, 'editing': phrase_id is not None})
