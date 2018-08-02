#!/usr/bin/env python
# encoding: utf-8

import argparse
# http://kuanghy.github.io/2016/06/30/python-argparse
def get_args():
    parser = argparse.ArgumentParser(description='argparse demo')
    parser.add_argument('--train_data', type=str, default='../data/train.csv',
                        help='training data path')
    parser.add_argument('--char_model', type=bool, default=True,
                        help='whether to use character level model')
    parser.add_argument('--embedding_dim', type=int, default=64,
                        help='size of word embeddings')
    parser.add_argument('--kernel_sizes', type=list, default=[2,3,4,5],
                        help='kernel sizes in CNN')
    parser.add_argument('--dropout', type=float, default=0.1,
                        help='dropout applied to layers (0 = no dropout)')
    parser.add_argument('--cuda', action='store_true',
                        help='use CUDA')
    parser.add_argument('--log_interval', type=int, default=100, metavar='N',
                        help='train log interval')
    return parser.parse_args()

args = get_args()
print(args)
print(vars(args))