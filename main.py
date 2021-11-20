def kbig(nums, k):
    list_nums_local = nums
    list_nums_out = []
    for i in range(k):
        list_nums_out.append(max(list_nums_local))
        list_nums_local.remove(max(list_nums_local))
    list_nums_local.clear()
    return min(list_nums_out)
