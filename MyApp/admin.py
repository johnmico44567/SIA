from django.contrib import admin
from .models import GameSetting


@admin.register(GameSetting)
class GameSettingAdmin(admin.ModelAdmin):
	list_display = ("game_name", "recommended_dpi", "recommended_sensitivity")
	search_fields = ("game_name", "game_description")
