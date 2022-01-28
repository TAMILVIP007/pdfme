import random
import copy
from argparse import ArgumentParser

from tests import *


if __name__ == '__main__':
    random.seed(20)

    parser = ArgumentParser()
    parser.add_argument('-s', '--single_test')
    parser.add_argument('-g', '--group_test', choices=['text', 'content', 'table'])
    args = parser.parse_args()

    if args.single_test:
        if args.single_test.startswith('test_content'):
            test_content(int(args.single_test[12:]))
        elif args.single_test.startswith('test_table'):
            test_table(int(args.single_test[10:]))
        else:
            globals()[args.single_test]()
    else:
        test_start = 'test_' + args.group_test if args.group_test else 'test'
        globals_ = list(globals().keys())
        for key in globals_:
            val = globals()[key]
            if key.startswith(test_start) and callable(val): val()
