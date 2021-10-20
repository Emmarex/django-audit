from django.core.management.base import BaseCommand

from ...models import AuditLog


class Command(BaseCommand):
    """ clean up management command """

    help = "Cleans up dj-audit AuditLog table"

    def handle(self, **options):
        """
        Removes all Audit log from the database
        """
        print("Starting clean up of dj-audit AuditLog table")

        count, _ = AuditLog.objects.all().delete()

        print(f'Deleted {count} records from dj-audit AuditLog table')
