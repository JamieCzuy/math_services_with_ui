from django.core.management.base import BaseCommand, CommandError

from services.models import SquaresDifference

class Command(BaseCommand):
    help = 'Initialize the database: populate the SquaresDifference Table.'

    def add_arguments(self, parser):
        # Optional arguments
        parser.add_argument('--force', action='store_true', help='Force the initialization (delete any existing SquareDifferences)!')

    def handle(self, *args, **options):

        if SquaresDifference.objects.all().count() > 0:
            if not options["force"]:
                raise CommandError("SquaresDifference Table is not empty. "
                                   "Database initialization aborted! "
                                   "Use the --force flag to delete the existing SquareDifferences.")
            
            # --force was used so delete all existing rows
            self.stdout.write(f"Deleting existing rows ({SquaresDifference.objects.all().count()}) from SquaresDifference table...")
            SquaresDifference.objects.all().delete()

        running_sum_of_n = 0
        sum_of_squares = 0
        for n in range(0,101):
            sum_of_squares += n*n
            running_sum_of_n += n
            square_of_sums = running_sum_of_n * running_sum_of_n
            value = square_of_sums - sum_of_squares
            self.stdout.write(f"{n=}  {sum_of_squares=}  {square_of_sums=}  {value=}")
            instance = SquaresDifference(
                given_number=n,
                value=value,
                occurrences=0,
                last_requested=None
            )
            instance.save()
