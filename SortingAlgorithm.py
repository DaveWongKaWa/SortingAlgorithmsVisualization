import math

#-- QuickSort ---------------------------------------------------------------------------------------------------------------
def QuickSort(raw):
    QuickSortRecursion(raw, 0, len(raw)-1)
def QuickSortRecursion(raw, start, end):
    if (start < end):
        pi = partition(raw, start, end)
        QuickSortRecursion(raw, start, pi-1)
        QuickSortRecursion(raw, pi+1, end)
def partition(raw, start, end):
    I = start - 1
    for J in range(start, end):
        if (raw[J] < raw[end]):
            I += 1
            if (I != J):
                raw[I], raw[J] = raw[J], raw[I]
    raw[I+1], raw[end] = raw[end], raw[I+1]
    return I+1

#-- MergeSorts -------------------------------------------------------------------------------------------------------------
# Ordinary
def OrdinaryMerge(template, start, mid, end, raw):
    I = start
    J = mid+1
    for i in range(start, end+1):
        if (I <= mid and J <= end):
            if (template[I] <= template[J]):
                raw[i] = template[I]
                I += 1
            else:
                raw[i] = template[J]
                J += 1
        elif (I > mid):
            raw[i] = template[J]
            J += 1
        elif (J > end):
            raw[i] = template[I]
            I += 1
def OrdinaryTopDownMergeSort(raw):
    template = []
    for i in range(0, len(raw)):
        template.append(raw[i])
    OrdinaryTopDownSplitMerge(template, 0, len(raw)-1, raw)
def OrdinaryTopDownSplitMerge(template, start, end, raw):
    if (start < end):
        mid = int((start+end)/2)
        OrdinaryTopDownSplitMerge(raw, start, mid, template)
        OrdinaryTopDownSplitMerge(raw, mid+1, end, template)
        OrdinaryMerge(template, start, mid, end, raw)
def OrdinaryBottomUpMergeSort(raw):
    template = [0]*(len(raw))
    for i in range(0, len(raw)):
        template[i] = raw[i]
    width = 1
    while (width < len(raw)):
        i = 0
        while (i < len(raw)):
            OrdinaryMerge(template, i, min(i+width-1, len(raw)-1), min(i+2*width-1, len(raw)-1), raw)
            i += 2*width
        for i in range(0, len(raw)):
            template[i] = raw[i]
        width *= 2
# Alternative N/2
def AltTopDownMergeSort(raw):
    template = [0]*(int(len(raw)/2)+1)
    AltTopDownSplitMerge(raw, 0, len(raw)-1, template)
def AltTopDownSplitMerge(raw, start, end, template):
    if (start < end):
        mid = int((start+end)/2)
        AltTopDownSplitMerge(raw, start, mid, template)
        AltTopDownSplitMerge(raw, mid+1, end, template)
        i = 0
        for j in range(start, mid+1):
            template[i] = raw[j]
            i += 1
        AltTopDownMerge(raw, start, mid, end, template)
def AltTopDownMerge(raw, start, mid, end, template):
    I = 0
    J = mid+1
    for i in range(start, end+1):
        if (I <= mid-start and J <= end):
            if (template[I] <= raw[J]):
                raw[i] = template[I]
                I += 1
            else:
                raw[i] = raw[J]
                J += 1
        elif (I > mid-start):
            raw[i] = raw[J]
            J += 1
        elif (J > end):
            raw[i] = template[I]
            I += 1
def AltBottomUpMergeSort(raw):
    template = [0]*(int(len(raw)/2)+1)
    width = 1
    while (width < len(raw)):
        i = 0
        while (i < len(raw)):
            j = 0
            for k in range(min(i+width-1, len(raw)-1)+1, min(i+2*width-1, len(raw)-1)+1):
                template[j] = raw[k]
                j += 1
            AltBottomUpMerge(raw, i, min(i+width-1, len(raw)-1), min(i+2*width-1, len(raw)-1), template)
            i += 2*width
        width *= 2
def AltBottomUpMerge(raw, start, mid, end, template):
    I = mid
    J = end-mid-1
    for i in range(end, start-1, -1):
        if (I >= start and J >= 0):
            if (template[J] >= raw[I]):
                raw[i] = template[J]
                J -= 1
            else:
                raw[i] = raw[I]
                I -= 1
        elif (I < start):
            raw[i] = template[J]
            J -= 1
        elif (J < 0):
            raw[i] = raw[I]
            I -= 1
# Inplace
def InplaceMerge(raw, start, mid, end):
    I = start
    J = mid+1
    rshift = 0
    for i in range(start, end+1):
        if (I <= mid and J <= end):
            if (raw[I+rshift] < raw[J]):
                I += 1
            else:
                temp = raw[J]
                index = J
                while (index > i):
                    raw[index] = raw[index-1]
                    index -= 1
                raw[i] = temp
                J += 1
                rshift += 1
def InplaceTopDownMergeSort(raw):
    InplaceTopDownSplitMerge(raw, 0, len(raw)-1)
def InplaceTopDownSplitMerge(raw, start, end):
    if (start < end):
        mid = int((start+end)/2)
        InplaceTopDownSplitMerge(raw, start, mid)
        InplaceTopDownSplitMerge(raw, mid+1, end)
        InplaceMerge(raw, start, mid, end)
def InplaceBottomUpMergeSort(raw):
    width = 1
    while (width < len(raw)):
        i = 0
        while (i < len(raw)):
            InplaceMerge(raw, i, min(i+width-1, len(raw)-1), min(i+2*width-1, len(raw)-1))
            i += 2*width
        width *= 2
#-- HeapSorts --------------------------------------------------------------------------------------------------------------
# Ordinary
def OrdinaryTopDownHeapSort(raw):
    hsize = 1
    while (hsize <= len(raw)):
        i = int(hsize/2) - 1
        while (i >= 0):
            OrdinaryMaxHeapify(raw, hsize, i)
            i = int((i+1)/2)-1
        hsize += 1
    hsize = len(raw)-1
    while (hsize > 0):
        raw[0], raw[hsize] = raw[hsize], raw[0]
        OrdinaryMaxHeapify(raw, hsize, 0)
        hsize -= 1 
def OrdinaryBottomUpHeapSort(raw):
    i = int(len(raw)/2)-1
    while (i >= 0):
        OrdinaryMaxHeapify(raw, len(raw), i)
        i -= 1
    hsize = len(raw)-1
    while (hsize > 0):
        raw[0], raw[hsize] = raw[hsize], raw[0]
        OrdinaryMaxHeapify(raw, hsize, 0)
        hsize -= 1
def OrdinaryMaxHeapify(raw, hsize, i):
    if (i < hsize and i >= int(hsize/2)):
        return
    if (2*i+2 < hsize and (raw[i] < raw[2*i+1] or raw[i] < raw[2*i+2])):
        j = 2*i+1 if (raw[2*i+1] >= raw[2*i+2]) else 2*i+2
        raw[i], raw[j] = raw[j], raw[i]
        OrdinaryMaxHeapify(raw, hsize, j)
    elif (raw[i] < raw[2*i+1]):
        raw[i], raw[2*i+1] = raw[2*i+1], raw[i]
        OrdinaryMaxHeapify(raw, hsize, 2*i+1)
# Ternary
def TernaryTopDownHeapSort(raw):
    hsize = 1
    while (hsize <= len(raw)):
        i = hsize-1
        while (i >= 0):
            TernaryMaxHeapify(raw, hsize, i)
            i = int(math.ceil(i/3)-1)
        hsize += 1
    hsize = len(raw)-1
    while (hsize > 0):
        raw[0], raw[hsize] = raw[hsize], raw[0]
        TernaryMaxHeapify(raw, hsize, 0)
        hsize -= 1
def TernaryBottomUpHeapSort(raw):
    i = len(raw) - (2*int(math.ceil(len(raw)/3)) - int(math.ceil((len(raw)%3)/2))) - 1
    while (i >= 0):
        TernaryMaxHeapify(raw, len(raw), i)
        i -= 1
    hsize = len(raw)-1
    while (hsize > 0):
        raw[0], raw[hsize] = raw[hsize], raw[0]
        TernaryMaxHeapify(raw, hsize, 0)
        hsize -= 1
def TernaryMaxHeapify(raw, hsize, i):
    if (i < hsize and i >= hsize - (2*int(math.ceil(hsize/3)) - int(math.ceil((hsize%3)/2)))):
        return
    if (3*i+3 < hsize and (raw[i] < raw[3*i+1] or raw[i] < raw[3*i+2] or raw[i] < raw[3*i+3])):
        targetIndex = i
        if (raw[3*i+1] >= raw[3*i+2]):
            if (raw[3*i+1]) >= raw[3*i+3]:
                targetIndex = 3*i+1
            else:
                targetIndex = 3*i+3
        else:
            if (raw[3*i+2] >= raw[3*i+3]):
                targetIndex = 3*i+2
            else:
                targetIndex = 3*i+3
        raw[i], raw[targetIndex] = raw[targetIndex], raw[i]
        TernaryMaxHeapify(raw, hsize, targetIndex)
    elif (3*i+2 < hsize and (raw[i] < raw[3*i+1] or raw[i] < raw[3*i+2])):
        targetIndex = 3*i+1 if (raw[3*i+1] >= raw[3*i+2]) else 3*i+2
        raw[i], raw[targetIndex] = raw[targetIndex], raw[i]
        TernaryMaxHeapify(raw, hsize, targetIndex)
    elif (raw[i] < raw[3*i+1]):
        raw[i], raw[3*i+1] = raw[3*i+1], raw[i]
        TernaryMaxHeapify(raw, hsize, 3*i+1)
#-- SimpleSorts ------------------------------------------------------------------------------------------------------------
def InsertionSort(raw):
    for i in range(1, len(raw)):
        temp = raw[i]
        index = i-1
        while (index > 0 and temp < raw[index-1]):
            raw[index+1] = raw[index]
            index -= 1
        raw[index] = temp
def SelectionSort(raw):
    for i in range(0, len(raw)):
        minIndex = i
        minVal = raw[i]
        for j in range(i, len(raw)):
            if (raw[j] < minVal):
                minIndex = j
                minVal = raw[j]
        raw[i], raw[minIndex] = raw[minIndex], raw[i]