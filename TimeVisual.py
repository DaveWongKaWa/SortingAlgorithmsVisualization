import random
import time
import matplotlib.pyplot as plt
import seaborn as sns
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
sns.set_theme(context="paper", style="darkgrid")

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
    "OTDMergeSort":OrdinaryTopDownMergeSort,
    "OBUMergeSort":OrdinaryBottomUpMergeSort,
    "ATDMergeSort":AltTopDownMergeSort,
    "ABUMergeSort":AltBottomUpMergeSort,
    "ITDMergeSort":InplaceTopDownMergeSort,
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

PlotMap = dict({
    "MergeSorts":MergeSorts,
    "HeapSorts":HeapSorts,
    "SimpleSorts":SimpleSorts,
    "BestComparison":BestComparison,
    "QuadraticComparison":QuadraticComparison
})

numPlots = 1
plots = []
names = []
sizes = []
depths = []
def addplot(numPlots):
    newPlot = st.checkbox("Plot " + str(numPlots), False)
    if (newPlot):
        funcs = []
        col1, col2 = st.beta_columns(2)
        plotContent = col1.selectbox("Default or Custom Plot", ["MergeSorts", "HeapSorts", "SimpleSorts", "BestComparison", "QuadraticComparison", "Custom"], key=str(numPlots))
        plotName = col2.text_input("Name", value = "Plot " + str(numPlots))
        names.append(plotName)
        if (plotContent != "Custom"):
            plots.append(PlotMap[plotContent])
        elif (plotContent == "Custom"):
            plots.append(st.multiselect("Algorithms", Algorithms, key=str(numPlots)))
        sampleSizeUpperBound = st.slider("Sample Sizes", min_value = 10, max_value = 1000, key=str(numPlots))
        sizes.append(range(1, sampleSizeUpperBound+1))
        depths.append(st.slider("Execution Depth", min_value = 1, max_value = 10, key=str(numPlots)))
        numPlots += 1
        if (numPlots <= 9):
            addplot(numPlots)

addplot(numPlots)
execute = st.checkbox("Execute ", False)
if (execute == True):
    fig = plt.figure(figsize = (10, 9), dpi=200, tight_layout=True)
    for i in range(0, len(plots)):
        pos = i+1
        ax = fig.add_subplot(3, 3, pos)
        ax.set_title(names[i])
        for func in plots[i]:
            times = SortingAlgorithms_Times(FuncMap[func], sizes[i], depths[i])
            sns.lineplot(x = sizes[i], y = times, linewidth=0.25, label=func)
    st.pyplot(fig=fig, dpi=500)


