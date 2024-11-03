from bot.main import run_bot
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Телеграм бот"

    def handle(self, *args, **options):
        run_bot()
