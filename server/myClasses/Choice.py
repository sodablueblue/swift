#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class of Choice'

__author__ = 'Sodablueblue'

from Rule import *

class Choice(Combination):

	def __init__(self, criteria):
		super(Choice, self).__init__('Choice', criteria)

	def _checkBench(values, bench):
		if len(values) > 1:
			raise BaseException('Choice: Data more than one')

		if not values[0].name in tuple(v.name for v in bench):
			raise BaseException('Choice: Invalid data ', values[0])

	def _toHtml(self):
		resVal = 'Choice: ('
		for cri in self.criteria:
			resVal += cri.name + ', '
		return resVal[:-2:] + ')'