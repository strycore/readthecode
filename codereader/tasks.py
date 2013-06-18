import os
from django.conf import settings
from celery import task
from . import util


@task
def import_repo(repo_url, project_slug):
    dest_path = os.path.join(settings.MEDIA_ROOT, "repositories", project_slug)
    util.clone_repo(repo_url, dest_path, vcs='autodetect')
