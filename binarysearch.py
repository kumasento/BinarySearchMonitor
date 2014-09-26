
import monitor as mon

def regular(num, val, monitor):
    #monitor init
    monitor.clear()

    length = len(num)
    if length == 0:
        return -1
    h = length - 1
    l = 0
    while l <= h:
        #monitor insert
        monitor.insert(l, h)

        mid = l + (h-l)/2
        tmp = num[mid]
        if tmp == val:
            return mid
        elif tmp < val:
            l = mid + 1
        else:
            h = mid - 1
    return -1


def lowerbound(num, val, monitor):
    #monitor init
    monitor.clear()

    length = len(num)
    if length == 0:
        return -1
    h,l = length-1, 0
    while l <= h:
        monitor.insert(l, h)
        mid = l + (h-l)/2
        tmp = num[mid]
        if tmp < val:
            l = mid + 1
        else:
            h = mid -1
    if num[l] == val:
        return l
    else:
        return -1

def upperbound(num, val, monitor):
    #monitor init
    monitor.clear()

    length = len(num)
    if length == 0:
        return -1
    h,l = length-1, 0
    while l <= h:
        monitor.insert(l, h)
        mid = l + (h-l)/2
        tmp = num[mid]
        if tmp > val:
            h = mid -1
        else:
            l = mid + 1
    if num[h] == val:
        return h
    else:
        return -1
