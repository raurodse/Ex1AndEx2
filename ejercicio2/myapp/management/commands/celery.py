from django.core.management.base import BaseCommand, CommandError
import myapp.tasks
class Command(BaseCommand):
    help = ''

    def add_arguments(self, parser):
		parser.add_argument(
            '--dest',
            action='store',
            dest='dest',
            help='Destination of file',
        )
        

    def handle(self, *args, **options):
    	destiny = options['dest'] if options['dest'] != None else '/tmp/fichero'
        myapp.tasks.write_file.apply_async(args=[destiny],countdown=30)
