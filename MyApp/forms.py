from django import forms

from .models import GameSetting


class GameSettingForm(forms.ModelForm):
    class Meta:
        model = GameSetting
        fields = [
            "game_name",
            "game_description",
            "recommended_dpi",
            "recommended_sensitivity",
            "sensitivity_description",
            "notes",
        ]
        widgets = {
            "game_name": forms.TextInput(attrs={"placeholder": "e.g. Valorant"}),
            "game_description": forms.Textarea(attrs={"placeholder": "What makes this profile work?", "rows": 3}),
            "recommended_dpi": forms.NumberInput(attrs={"placeholder": "800", "min": 1}),
            "recommended_sensitivity": forms.TextInput(attrs={"placeholder": "0.35"}),
            "sensitivity_description": forms.Textarea(attrs={"placeholder": "Explain the feel and ideal playstyle.", "rows": 3}),
            "notes": forms.Textarea(attrs={"placeholder": "Extra tips, scoped sensitivity, or setup notes.", "rows": 3}),
        }
