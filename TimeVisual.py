import random
import time

#-- Generate Data ---------------------------------------------------------
def randList(lo, hi, size):
    randomList = []
    for i in range(0, size):
        randomList.append(random.randint(lo, hi))
    return randomList

def SortingAlgorithms_Times(func, sampleSizes, depth):
    Times = []
    for i in sampleSizes:
        avg = 0
        for j in range(0, depth):
            sampleList = randList(1, i, i)
            start_time = time.time()
            func(sampleList)
            end_time = time.time()
            avg += end_time-start_time
        Times.append(avg/depth)
    return Times

#-- Generate Plot ---------------------------------------------------------
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(context="paper", style="darkgrid")
import streamlit as st

from SortingAlgorithm import QuickSort
from SortingAlgorithm import OrdinaryTopDownMergeSort
from SortingAlgorithm import OrdinaryBottomUpMergeSort
from SortingAlgorithm import AltTopDownMergeSort
from SortingAlgorithm import AltBottomUpMergeSort
from SortingAlgorithm import InplaceTopDownMergeSort
from SortingAlgorithm import InplaceBottomUpMergeSort
from SortingAlgorithm import OrdinaryTopDownHeapSort
from SortingAlgorithm import OrdinaryBottomUpHeapSort
from SortingAlgorithm import TernaryTopDownHeapSort
from SortingAlgorithm import TernaryBottomUpHeapSort
from SortingAlgorithm import InsertionSort
from SortingAlgorithm import SelectionSort

Algorithms = []
Algorithms.append("QuickSort")
Algorithms.append("OTDMergeSort")
Algorithms.append("OBUMergeSort")
Algorithms.append("ATDMergeSort")
Algorithms.append("ABUMergeSort")
Algorithms.append("ITPMergeSort")
Algorithms.append("IBUMergeSort")
Algorithms.append("OTDHeapSort")
Algorithms.append("OBUHeapSort")
Algorithms.append("TTDHeapSort")
Algorithms.append("TBUHeapSort")
Algorithms.append("InsertionSort")
Algorithms.append("SelectionSort")

FuncMap = dict({
    "QuickSort":QuickSort,
    "OTDmergeSort":OrdinaryTopDownMergeSort,
    "OBUMergeSort":OrdinaryBottomUpMergeSort,
    "ATDMergeSort":AltTopDownMergeSort,
    "ABUMergeSort":AltBottomUpMergeSort,
    "ITPMergeSort":InplaceTopDownMergeSort,
    "IBUMergeSort":InplaceBottomUpMergeSort,
    "OTDHeapSort":OrdinaryTopDownHeapSort,
    "OBUHeapSort":OrdinaryBottomUpHeapSort,
    "TTDHeapSort":TernaryTopDownHeapSort,
    "TBUHeapSort":TernaryBottomUpHeapSort,
    "InsertionSort":InsertionSort,
    "SelectionSort":SelectionSort
    })

MergeSorts = ["OTDMergeSort", "OBUMergeSort", "ATDMergeSort", "ABUMergeSort", "ITDMergeSort", "IBUMergeSort"]
HeapSorts = ["OTDHeapSort", "OBUHeapSort", "TTDHeapSort", "TBUHeapSort"]
SimpleSorts = ["InsertionSort", "SelectionSort"]
BestComparison = ["OTDMergeSort", "OBUHeapSort", "QuickSort", "SelectionSort"]
QuadraticComparison = ["ITDMergeSort", "IBUMergeSort", "SelectionSort", "InsertionSort"]

numPlots = 1
sizes = []

def addplot(numPlots):
    newPlot = st.checkbox("Plot " + str(numPlots), False)
    if (newPlot):
        funcs = []
        plotName = st.selectbox("Default or Custom Plot", ["MergeSorts", "HeapSorts", "SimpleSorts", "BestComparison", "QuadraticComparison", "Custom"])
        if (plotName == "MergeSorts"):
            funcs = MergeSorts
        elif (plotName == "HeapSorts"):
            funcs = HeapSorts
        elif (plotName == "SimpleSorts"):
            funcs = SimpleSorts
        elif (plotName == "BestComparison"):
            funcs = BestComparison
        elif (plotName == "QuadraticComparison"):
            funcs = QuadraticComparison
        elif (plotName == "Custom"):
            funcs = st.multiselect("Algorithms", Algorithms)
        sampleSizeUpperBound = st.slider("Sample Sizes", min_value = 10, max_value = 1000)
        sizes = range(1, sampleSizeUpperBound+1)
        depth = st.slider("Execution Depth", min_value = 1, max_value = 5)
        plot(funcs, sizes, depth)
        numPlots += 1
        addplot(numPlots)

def plot(Functions, sampleSizes, depth):
    ax = fig.add_subplot(3, 3, numPlots)
    ax.set_title("Plot " + str(numPlots))
    for func in Functions:
        times = SortingAlgorithms_Times(FuncMap[func], sampleSizes, depth)
        sns.lineplot(x = sampleSizes, y = times, linewidth=0.25, label=func)

fig = plt.figure(figsize = (10, 9), dpi=500, tight_layout = True)
addplot(numPlots)
