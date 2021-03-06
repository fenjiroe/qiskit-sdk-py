# -*- coding: utf-8 -*-

# Copyright 2017 IBM RESEARCH. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================

"""
Node for an OPENQASM real number.
"""
import math
from ._node import Node


class Real(Node):
    """Node for an OPENQASM real number.

    This node has no children. The data is in the value field.
    """

    def __init__(self, id):
        """Create the real node."""
        Node.__init__(self, "real", None, None)
        self.value = id

    def to_string(self, indent):
        """Print with indent."""
        ind = indent * ' '
        print(ind, 'real', self.value)

    def qasm(self, prec=15):
        """Return the corresponding OPENQASM string."""
        fspec = "%%0.%df" % prec
        return fspec % self.value

    def latex(self, prec=15, nested_scope=None):
        """Return the corresponding math mode latex string."""
        if math.isclose(self.value, math.pi):
            return "\\pi"
        fspec = "%%0.%df" % prec
        return fspec % self.value

    def real(self, nested_scope=None):
        """Return the correspond floating point number."""
        return self.value
