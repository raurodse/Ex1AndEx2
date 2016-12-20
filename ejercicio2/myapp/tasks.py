#from celery.decorators import task
from __future__ import absolute_import, unicode_literals
from celery import shared_task

@shared_task
def write_file(fichero):
    f = open(fichero,'w')
    f.write('Hello Wolrd\n')
    f.close()
