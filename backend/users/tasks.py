from django.core import management

from Oxossi import celery_app


@celery_app.task
def clearsessions():
    management.call_command("clearsessions")
