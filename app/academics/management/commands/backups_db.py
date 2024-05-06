from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import json

class Command(BaseCommand):
    #Configure help information
    help = 'Make a database backup in JSON format'

    def handle(self, *args, **options):
        #Get data from User model
        users = User.objects.all()

        #Convert data to dictionaries
        data = [
            {
                'id':       user.id,
                'email':    user.email,
                'password': user.password

            }
            for user in users
        ]

        #Save to JSON format
        with open('backup_db.json','w') as file:
            json.dump(data, file, indent=4)