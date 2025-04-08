from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email='testuser@example.com', name='Test User', age=25)
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertEqual(user.name, 'Test User')
        self.assertEqual(user.age, 25)

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team', members=['user1@example.com', 'user2@example.com'])
        self.assertEqual(team.name, 'Test Team')
        self.assertEqual(team.members, ['user1@example.com', 'user2@example.com'])

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(email='activityuser@example.com', name='Activity User', age=30)
        activity = Activity.objects.create(user=user, type='Running', duration=60, date='2025-04-08')
        self.assertEqual(activity.user, user)
        self.assertEqual(activity.type, 'Running')
        self.assertEqual(activity.duration, 60)

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard_entry(self):
        user = User.objects.create(email='leaderboarduser@example.com', name='Leaderboard User', age=35)
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(leaderboard.user, user)
        self.assertEqual(leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Test Workout', description='Test Description', duration=45)
        self.assertEqual(workout.name, 'Test Workout')
        self.assertEqual(workout.description, 'Test Description')
        self.assertEqual(workout.duration, 45)
