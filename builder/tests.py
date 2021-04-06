from django.test import TestCase
from builder.models import Team
from django.urls import reverse

# Create your tests here.
class TeamMethodTests(TestCase):
    def test_ensure_views_are_positive(self):
        """Ensures the number of likes received for a team are positive or zero."""
        team=Team(teamname='test', likes=-1, userprofile="test")
        team.save()

        self.assertEqual((team.likes >= 0), True)

class ViewTests(TestCase):
    def test_home_view_with_no_teams(self):
        response=self.client.get(reverse('builder:home'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response, '--- There are no teams yet, better get building! ---')

    def test_teamview_view_with_no_teams(self):
        """If no categories exist, the appropriate message should be displayed."""
        response = self.client.get(reverse('builder:team_view'))
        self.assertEqual(response.status_code , 200)
        # self.assertContains(response, '--- There are no teams yet, better get building! ---')