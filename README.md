Read the code
=============

Source code browser / search engine / collaborative tool.

This project uses the following technologies:

- [codesearch](http://code.google.com/p/codesearch/)
- [linguist (the python version)](https://github.com/liluo/linguist)
- [angularjs for the frontend](http://angularjs.org/)
- Django, TastyPie and Celery for the backend


Planned features
----------------

- Powerful source code browser and search engine.
- Support for all major DVCS (git, bzr, hg)
- A user can comment on specific lines of code
- A user can bookmark a project, a file or a specific line in a file
- Files and directories can be tagged
- A dependency tree between projects can be automatically generated
- Function names, classes, variables are hyperlinks that points to their
  original definition, even if in another project (I believe the use of ctags
  would be appropriate here)
