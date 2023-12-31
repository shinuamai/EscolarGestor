#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
| This file is part of the web2py Web Framework
| Developed by Massimo Di Pierro <mdipierro@cs.depaul.edu>,
| limodou <limodou@gmail.com> and srackham <srackham@gmail.com>.
| License: LGPLv3 (http://www.gnu.org/licenses/lgpl.html)

Just for backward compatibility
--------------------------------
"""
__all__ = ["DAL", "Field", "DRIVERS"]

from pydal.base import BaseAdapter
from pydal.drivers import DRIVERS
from pydal.helpers.classes import SQLALL
from pydal.objects import Expression, Query, Row, Rows, Set, Table

from gluon.dal import DAL, Field, SQLCustomType

SQLDB = DAL
GQLDB = DAL
SQLField = Field
SQLTable = Table
SQLXorable = Expression
SQLQuery = Query
SQLSet = Set
SQLRows = Rows
SQLStorage = Row
