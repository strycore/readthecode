import os
import shutil
from django.test import TestCase
from django.conf import settings
from codereader.util import clone_repo


class TestRepoUtil(TestCase):
    def delete_local_repos(self):
        shutil.rmtree(os.path.join(settings.MEDIA_ROOT, 'bzr'), True)
        shutil.rmtree(os.path.join(settings.MEDIA_ROOT, 'git'), True)

    def setUp(self):
        self.delete_local_repos()

    def test_bzr_repo_can_be_cloned(self):
        local_branch_path = os.path.join(settings.MEDIA_ROOT, "bzr/lutris")
        clone_repo("lp:lutris", local_branch_path, vcs='bzr')

    def test_git_repo_can_be_cloned(self):
        local_branch_path = os.path.join(settings.MEDIA_ROOT, "git")
        clone_repo("http://github.com/strycore/scripts.git", local_branch_path)

    def tearDown(self):
        self.delete_local_repos()
