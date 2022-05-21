#!/usr/bin/python3

import utils.algo_num
import utils.algo_str

if __name__ == "__main__":
    values = (2, 3, 1, 4, 6)
    min_val = utils.algo_num.min(values)
    max_val = utils.algo_num.max(values)
    sum_val = utils.algo_num.sum(values)
    print([min_val, max_val, sum_val])

    arr = [3, 2, 1, 5, -3, 2, 0, -2, 11, 9]
    sorted_arr = utils.algo_num.selection_sort(arr)
    print(sorted_arr)

    is_pal = utils.algo_str.is_palindrome('malayalam')
    print(is_pal)
