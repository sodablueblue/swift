#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class of SimpleContent'

__author__ = 'Sodablueblue'

from Extension import *

class SimpleContent(object):

	def __init__(self, extension):
		self.extension = extension

	def check(self):
		self.extension.check()