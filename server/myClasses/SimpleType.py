#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class of SimpleType'

__author__ = 'Sodablueblue'

from Type import *

class SimpleType(Type):

	def __init__(self, name, rule):
		super(SimpleType, self).__init__(name, rule)

	