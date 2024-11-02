from django.core.management import BaseCommand

from bot.main import run_bot


class Command(BaseCommand):
    help = 'Телеграм бот'

    def handle(self, *args, **options):
        run_bot()
