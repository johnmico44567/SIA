from django.test import TestCase

from .models import GameSetting, SensitivityHistory


class SensitivityHistoryTests(TestCase):
	def test_saved_profile_creates_history_and_refresh_does_not_duplicate_it(self):
		response = self.client.post(
			"/add/",
			{
				"game_name": "VALORANT",
				"game_description": "A steady baseline.",
				"recommended_dpi": 1600,
				"recommended_sensitivity": "0.22",
				"sensitivity_description": "Low, controlled sensitivity.",
				"notes": "Wrist and arm hybrid.",
			},
		)

		self.assertRedirects(response, "/")
		self.assertEqual(GameSetting.objects.count(), 1)
		self.assertEqual(SensitivityHistory.objects.count(), 1)

		history_entry = SensitivityHistory.objects.get()
		self.assertEqual(history_entry.game_name, "VALORANT")
		self.assertEqual(history_entry.recommended_dpi, 1600)
		self.assertEqual(history_entry.recommended_sensitivity, "0.22")

		response = self.client.get("/")

		self.assertContains(response, "Sensitivity History")
		self.assertContains(response, "Low, controlled sensitivity.")
		self.assertEqual(SensitivityHistory.objects.count(), 1)

	def test_home_displays_history_newest_first(self):
		SensitivityHistory.objects.create(
			game_name="VALORANT",
			recommended_dpi=1600,
			recommended_sensitivity="0.22",
		)
		SensitivityHistory.objects.create(
			game_name="CS2",
			recommended_dpi=800,
			recommended_sensitivity="1.20",
		)

		response = self.client.get("/")

		self.assertEqual(
			list(response.context["history"].values_list("game_name", flat=True)),
			["CS2", "VALORANT"],
		)
