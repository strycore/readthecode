import os
from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Project(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    homepage_url = models.URLField(max_length=255, blank=True)

    def __unicode__(self):
        return "{}".format(self.name)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)


class Repository(models.Model):
    project = models.ForeignKey(Project)
    origin_url = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return "{}: {}".format(self.project.name, self.origin_url)

    @property
    def code_root(self):
        return os.path.join(settings.MEDIA_ROOT, "repositories",
                            self.project.slug)

    def files(self):
        repo_structure = {}
        for (dirpath, dirnames, filenames) in os.walk(self.code_root):
            rel_path = dirpath[len(self.code_root):]
            repo_structure_dir = repo_structure
            dirs = rel_path.split('/')
            for dirname in dirs:
                if dirname:
                    repo_structure_dir = repo_structure_dir[dirname]
            for filename in filenames:
                repo_structure_dir[filename] = filename
            for dirname in dirnames:
                repo_structure_dir[dirname] = {}
        return repo_structure
