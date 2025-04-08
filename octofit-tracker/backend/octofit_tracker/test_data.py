from datetime import date

test_data = {
    "users": [
        {"email": "thundergod@mhigh.edu", "name": "Thor", "age": 30},
        {"email": "metalgeek@mhigh.edu", "name": "Tony Stark", "age": 35},
        {"email": "zerocool@mhigh.edu", "name": "Steve Rogers", "age": 32},
        {"email": "crashoverride@hmhigh.edu", "name": "Natasha Romanoff", "age": 28},
        {"email": "sleeptoken@mhigh.edu", "name": "Bruce Banner", "age": 40},
    ],
    "teams": [
        {"name": "Blue Team", "members": ["thundergod@mhigh.edu", "metalgeek@mhigh.edu", "zerocool@mhigh.edu"]},
        {"name": "Gold Team", "members": ["crashoverride@hmhigh.edu", "sleeptoken@mhigh.edu"]},
    ],
    "activities": [
        {"user_email": "thundergod@mhigh.edu", "type": "Cycling", "duration": 60, "date": date(2025, 4, 1)},
        {"user_email": "metalgeek@mhigh.edu", "type": "Crossfit", "duration": 120, "date": date(2025, 4, 2)},
        {"user_email": "zerocool@mhigh.edu", "type": "Running", "duration": 90, "date": date(2025, 4, 3)},
        {"user_email": "crashoverride@hmhigh.edu", "type": "Strength", "duration": 30, "date": date(2025, 4, 4)},
        {"user_email": "sleeptoken@mhigh.edu", "type": "Swimming", "duration": 75, "date": date(2025, 4, 5)},
    ],
    "leaderboard": [
        {"user_email": "thundergod@mhigh.edu", "score": 100},
        {"user_email": "metalgeek@mhigh.edu", "score": 90},
        {"user_email": "zerocool@mhigh.edu", "score": 95},
        {"user_email": "crashoverride@hmhigh.edu", "score": 85},
        {"user_email": "sleeptoken@mhigh.edu", "score": 80},
    ],
    "workouts": [
        {"name": "Cycling Training", "description": "Training for a road cycling event", "duration": 60},
        {"name": "Crossfit", "description": "Training for a crossfit competition", "duration": 120},
        {"name": "Running Training", "description": "Training for a marathon", "duration": 90},
        {"name": "Strength Training", "description": "Training for strength", "duration": 30},
        {"name": "Swimming Training", "description": "Training for a swimming competition", "duration": 75},
    ],
}
