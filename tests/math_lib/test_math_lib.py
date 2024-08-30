import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from math_lib.math_lib import MathLib


class TestMathLib:
    def test_abs(self):
        assert MathLib.abs(0) == 0
        assert MathLib.abs(1) == 1
        assert MathLib.abs(-1) == 1

    def test_add(self):
        assert MathLib.add(1, 1) == 2
        assert MathLib.add(-1, 1) == 0

    def test_sub(self):
        assert MathLib.sub(1, 1) == 0
        assert MathLib.sub(2, 1) == 1

    def test_mult(self):
        assert MathLib.mult(0, 0) == 0
        assert MathLib.mult(0, 1) == 0
        assert MathLib.mult(1, 0) == 0
        assert MathLib.mult(1, 1) == 1
        assert MathLib.mult(1, 10) == 10
        assert MathLib.mult(10, 1) == 10
        assert MathLib.mult(2, 3) == 6
        assert MathLib.mult(-1, 1) == -1
        assert MathLib.mult(1, -1) == -1
        assert MathLib.mult(-1, 10) == -10
        assert MathLib.mult(10, -1) == -10
        assert MathLib.mult(-2, 3) == -6
        assert MathLib.mult(2, -3) == -6
