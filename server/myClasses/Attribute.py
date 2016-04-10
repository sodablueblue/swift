#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class of Attribute'

__author__ = 'Sodablueblue'

from Element import *

class Attribute(Element):

	def __init__(self, name, type, use):
		if use == 'required':
			super(Attribute, self).__init__(name, type)
		else:
			super(Attribute, self).__init__(name, type, 0, 0)