import os
from bzrlib.plugin import load_plugins
from bzrlib.branch import Branch

from git import Git


def clone_git_repo(url, local_path):
    git_repo = Git(local_path)
    git_repo.clone(url)


def clone_bzr_repo(url, local_path):
    load_plugins()
    bzr_repo = Branch.open(url)
    bzr_repo.bzrdir.sprout(local_path).open_branch()


def clone_repo(url, local_path, vcs='git'):
    clone_functions = {
        'git': clone_git_repo,
        'bzr': clone_bzr_repo
    }
    if vcs not in clone_functions:
        raise ValueError('vcs argument must be one of %s',
                         ' ,'.join(clone_functions))
    os.makedirs(local_path)
    clone_functions[vcs](url, local_path)
