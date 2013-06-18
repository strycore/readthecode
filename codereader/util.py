import os
import subprocess
from bzrlib.plugin import load_plugins
from bzrlib.branch import Branch

from git import Git


def autodetect_vcs(url):
    if 'bitbucket' in url:
        return 'hg'
    if 'launchpad' in url:
        return 'bzr'
    if 'github' in url:
        return 'git'


def clone_git_repo(url, local_path):
    git_repo = Git(local_path)
    git_repo.clone(url)


def clone_bzr_repo(url, local_path):
    load_plugins()
    bzr_repo = Branch.open(url)
    bzr_repo.bzrdir.sprout(local_path).open_branch()


def clone_hg_repo(url, local_path):
    subprocess.Popen(['hg', 'clone', url, local_path])


def clone_repo(url, local_path, vcs='git'):
    clone_functions = {
        'git': clone_git_repo,
        'bzr': clone_bzr_repo,
        'hg': clone_hg_repo,
    }
    if vcs == 'autodetect':
        vcs = autodetect_vcs(url)
    if vcs not in clone_functions:
        raise ValueError('vcs argument must be one of %s',
                         ' ,'.join(clone_functions))
    os.makedirs(local_path)
    clone_functions[vcs](url, local_path)
