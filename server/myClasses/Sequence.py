#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class of Sequence'

__author__ = 'Sodablueblue'

from Rule import *

class Sequence(Combination):

	def __init__(self, criteria):
		super(Sequence, self).__init__('Sequence', criteria)

	def _checkBench(values, bench):
		if len(values) > len(bench):
			raise BaseException('Sequence: Beyond sequence')

		i, j = 0, 0
		while j < len(bench):
			if i < len(values) and values[i].name == bench[j].name:
				i, j = i + 1, j + 1
				continue
			elif bench[j].minOccurs == 0:
				j = j + 1
				continue
			else:
				raise BaseException('Sequence: Sequence not equal')

	def _toHtml(self):
		resVal = 'Sequence: ('
		for cri in self.criteria:
			resVal += cri.name + ', '
		return resVal[:-2:] + ')'