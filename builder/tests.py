from django.test import TestCase
from builder.models import Team

# Create your tests here.
class TeamMethodTests(TestCase):
    def test_ensure_views_are_positive(self):
        """Ensures the number of views received for a Category are positive or zero."""
        team=Team(teamname='test', likes=-1, userprofile="test")
        team.save()

        self.assertEqual((team.likes >= 0), True)
