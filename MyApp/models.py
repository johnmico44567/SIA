from django.db import models


class GameSetting(models.Model):
    game_name = models.CharField(max_length=100)
    game_description = models.TextField()
    recommended_dpi = models.PositiveIntegerField()
    recommended_sensitivity = models.CharField(max_length=50)
    sensitivity_description = models.TextField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["game_name"]

    def __str__(self):
        return self.game_name


class SensitivityHistory(models.Model):
    game_name = models.CharField(max_length=100)
    recommended_dpi = models.PositiveIntegerField()
    recommended_sensitivity = models.CharField(max_length=50)
    sensitivity_description = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-saved_at", "-id"]

    def __str__(self):
        return f"{self.game_name} sensitivity saved at {self.saved_at}"
