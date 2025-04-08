from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(email='thundergod@mhigh.edu', name='Thor', age=30),
            User(email='metalgeek@mhigh.edu', name='Tony Stark', age=35),
            User(email='zerocool@mhigh.edu', name='Steve Rogers', age=32),
            User(email='crashoverride@hmhigh.edu', name='Natasha Romanoff', age=28),
            User(email='sleeptoken@mhigh.edu', name='Bruce Banner', age=40),
        ]
        User.objects.bulk_create(users)

        # Create teams
        teams = [
            Team(name='Blue Team', members=['thundergod@mhigh.edu', 'metalgeek@mhigh.edu', 'zerocool@mhigh.edu']),
            Team(name='Gold Team', members=['crashoverride@hmhigh.edu', 'sleeptoken@mhigh.edu']),
        ]
        Team.objects.bulk_create(teams)

        # Create activities
        activities = [
            Activity(user=User.objects.get(email='thundergod@mhigh.edu'), type='Cycling', duration=60, date=date(2025, 4, 1)),
            Activity(user=User.objects.get(email='metalgeek@mhigh.edu'), type='Crossfit', duration=120, date=date(2025, 4, 2)),
            Activity(user=User.objects.get(email='zerocool@mhigh.edu'), type='Running', duration=90, date=date(2025, 4, 3)),
            Activity(user=User.objects.get(email='crashoverride@hmhigh.edu'), type='Strength', duration=30, date=date(2025, 4, 4)),
            Activity(user=User.objects.get(email='sleeptoken@mhigh.edu'), type='Swimming', duration=75, date=date(2025, 4, 5)),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(user=User.objects.get(email='thundergod@mhigh.edu'), score=100),
            Leaderboard(user=User.objects.get(email='metalgeek@mhigh.edu'), score=90),
            Leaderboard(user=User.objects.get(email='zerocool@mhigh.edu'), score=95),
            Leaderboard(user=User.objects.get(email='crashoverride@hmhigh.edu'), score=85),
            Leaderboard(user=User.objects.get(email='sleeptoken@mhigh.edu'), score=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event', duration=60),
            Workout(name='Crossfit', description='Training for a crossfit competition', duration=120),
            Workout(name='Running Training', description='Training for a marathon', duration=90),
            Workout(name='Strength Training', description='Training for strength', duration=30),
            Workout(name='Swimming Training', description='Training for a swimming competition', duration=75),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
