#!/usr/bin/env python
import os
import sys
# /usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/bin/python2.7

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "prototype.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
