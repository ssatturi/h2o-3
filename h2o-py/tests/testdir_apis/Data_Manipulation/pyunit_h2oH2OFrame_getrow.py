from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
import h2o
from tests import pyunit_utils
import numpy as np
from random import randrange
from h2o.exceptions import H2OValueError
from h2o.utils.typechecks import assert_is_type


def h2o_H2OFrame_getrow():
    """
    Python API test: h2o.frame.H2OFrame.getrow()
    """
    numRow = randrange(1,3)
    numCol = 1
    python_lists = np.random.uniform(-1,1, (numRow, numCol))
    h2oframe = h2o.H2OFrame(python_obj=python_lists)
    onerow = h2oframe.getrow()
    assert_is_type(onerow, list)    # check return type
    # check and make sure random picked elements agree
    rowInd = randrange(0, h2oframe.nrow)
    assert abs(h2oframe[rowInd, 0]-onerow[rowInd]) < 1e-6, "h2o.H2OFrame.getrow() command is not working."


if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrame_getrow())
else:
    h2o_H2OFrame_getrow()
