from django.core.management.base import BaseCommand
from myapp.models import User
from django.core.mail import EmailMessage
from django.conf import settings


class Command(BaseCommand):
    help = 'Command to create 100 users'
    
    def handle(self, *args, **options):
        
        
        for i in range(1, 101):
            user = User.objects.create(
                name=f'user{i}',
                is_active = True
            )
            user.save()
        self.stdout.write(self.style.SUCCESS('Created 100 users.'))
        