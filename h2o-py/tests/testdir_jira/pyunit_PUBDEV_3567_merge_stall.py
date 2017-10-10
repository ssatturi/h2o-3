import sys
sys.path.insert(1,"../../")
import h2o
from tests import pyunit_utils




def pubdev_3567():
    train = h2o.import_file(pyunit_utils.locate("bigdata/laptop/higgs_train_imbalance_100k.csv"))
    test = h2o.import_file(pyunit_utils.locate("bigdata/laptop/higgs_test_imbalance_100k.csv"))
    merged = train.merge(test,by_x=["response"],by_y=["response"])#, method="radix")
    merged[0,0]
    # col = 10000* [0, 0, 1, 1, 2, 3, 0]
    # fr = h2o.H2OFrame(list(zip(*[col])))
    # fr.set_names(['rank'])
    #
    # mapping = h2o.H2OFrame(list(zip(*[[0,1,2,3],[6,7,8,9]])))
    # mapping.set_names(['rank', 'outcome'])
    #
    # merged = fr.merge(mapping,all_x=True,all_y=False)
    #
    # rows, cols = merged.dim
    # assert rows == 70000 and cols == 2, "Expected 70000 rows and 2 cols, but got {0} rows and {1} cols".format(rows, cols)
    #
    # threes = merged[merged['rank'] == 3].nrow
    # assert threes == 10000, "Expected 10000 3's, but got {0}".format(threes)



if __name__ == "__main__":
    pyunit_utils.standalone_test(pubdev_3567)
else:
    pubdev_3567()
