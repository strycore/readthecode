from django.conf.urls import patterns, url


urlpatterns = patterns(
    'codereader.views',
    url(r'^projects/$', "project_list", name="project_list"),
    url(r'^project/new/', "project_add", name="project_add"),
    url(r'^project/([\w-]+)/$', "project_details", name="project_details"),

    url(r'^project/([\w-]+)/repository/([\d]+)/', "repository_show", name="repository_show"),
    url(r'^project/([\w-]+)/repository/new/$', "repository_add",
        name="repository_add"),
)
