from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from . import models
from . import tasks


class CrispyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CrispyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit('save', "Save"))


class ProjectForm(CrispyForm):
    class Meta:
        model = models.Project
        fields = ('name', 'homepage_url', 'description')


class RepositoryForm(CrispyForm):
    class Meta:
        model = models.Repository
        fields = ('origin_url', )

    def __init__(self, *args, **kwargs):
        self.project = kwargs.pop('project')
        super(RepositoryForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        print self.project
        self.instance.project = self.project
        self.cleaned_data['project'] = self.project
        repo = super(RepositoryForm, self).save(*args, **kwargs)
        tasks.import_repo.delay(repo.origin_url, repo.project.slug)
        return repo
