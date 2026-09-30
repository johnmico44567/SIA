from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import GameSettingForm
from .models import GameSetting, SensitivityHistory

def index(request):
    query = request.GET.get("q", "").strip()
    settings = GameSetting.objects.all()
    if query:
        settings = settings.filter(game_name__icontains=query)

    context = {
        "settings": settings,
        "history": SensitivityHistory.objects.all(),
        "query": query,
        "form": GameSettingForm(),
    }
    return render(request, "im_fat_mico/home.html", context)


def add_setting(request):
    if request.method != "POST":
        return redirect("home")

    form = GameSettingForm(request.POST)
    if form.is_valid():
        setting = form.save()
        SensitivityHistory.objects.create(
            game_name=setting.game_name,
            recommended_dpi=setting.recommended_dpi,
            recommended_sensitivity=setting.recommended_sensitivity,
            sensitivity_description=setting.sensitivity_description,
            notes=setting.notes,
        )
        messages.success(request, "Game profile added to your aim library.")
    else:
        messages.error(request, "Check the profile details and try again.")
    return redirect("home")


def delete_setting(request, setting_id):
    if request.method == "POST":
        setting = get_object_or_404(GameSetting, id=setting_id)
        setting.delete()
        messages.success(request, "Game profile removed.")
    return redirect("home")
