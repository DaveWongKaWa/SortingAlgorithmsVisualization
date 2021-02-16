import random
import time
import numpy as np
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

@st.cache
def StaticSortingAlgorithms_Times(func, sampleSizes, depth):
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

def DynamicSortingAlgorithms_Times(func, sampleSizes, depth):
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

ExistingPlot = 0

Title = st.sidebar.text_input("Title")
PlotSize = st.sidebar.selectbox("Square Matrix Size", [1, 4, 9], index=2)
sns.set_theme(context="paper", style="darkgrid", font_scale=(1/np.cbrt(PlotSize))*2.3)
#----------------------------------------------------------------------------------------------------------
fig = plt.figure(figsize = (12, 10), dpi=200)
fig.suptitle(Title, fontsize=(1/np.cbrt(PlotSize))*23)
MatrixLength = int(np.sqrt(PlotSize))
AxesContainer = []
for i in range(0, PlotSize):
    pos = i+1
    AxesContainer.append(fig.add_subplot(MatrixLength, MatrixLength, pos))

#----------------------------------------------------------------------------------------------------------
class StaticPlot:
    def __init__(self, PlotName, Functions, SampleSizes, ExecutionDepth, Position):
        self.name = PlotName # String
        self.funcs = Functions # [String]
        self.sizes = SampleSizes # [int]
        self.dp = ExecutionDepth # int
        self.pos = Position # int

    def add_to(self):
        current = AxesContainer[self.pos - 1]
        current.set_title(self.name)
        plt.sca(current)
        for func in self.funcs:
            times = StaticSortingAlgorithms_Times(FuncMap[func], self.sizes, self.dp)
            sns.lineplot(x = self.sizes, y = times, linewidth=0.25, label=func)

def add_StaticPlot(PlotName, Functions, SampleSizes, ExecutionDepth, Position):
    new_plot = StaticPlot(PlotName, Functions, SampleSizes, ExecutionDepth, Position)
    new_plot.add_to()

class DynamicPlot:
    def __init__(self, PlotName, Functions, SampleSizes, ExecutionDepth, Position):
        self.name = PlotName # String
        self.funcs = Functions # [String]
        self.sizes = SampleSizes # [int]
        self.dp = ExecutionDepth # int
        self.pos = Position # int

    def add_to(self):
        current = AxesContainer[self.pos - 1]
        current.set_title(self.name)
        plt.sca(current)
        for func in self.funcs:
            times = DynamicSortingAlgorithms_Times(FuncMap[func], self.sizes, self.dp)
            sns.lineplot(x = self.sizes, y = times, linewidth=0.25, label=func)

def add_DynamicPlot(PlotName, Functions, SampleSizes, ExecutionDepth, Position):
    new_plot = DynamicPlot(PlotName, Functions, SampleSizes, ExecutionDepth, Position)
    new_plot.add_to()

#----------------------------------------------------------------------------------------------------------
def Interface(position):
    key = str(position)

    col1, col2 = st.sidebar.beta_columns(2)
    plotName = col1.text_input("Name", value="Plot " + str(key), key=key)
    state = col2.selectbox("State", ["Static", "Dynamic"], index=0, key=key)

    plotContent = st.sidebar.selectbox("Default or Custom Plot", ["MergeSorts", "HeapSorts", "SimpleSorts", "BestComparison", "QuadraticComparison", "Custom"], key=key)
    functions = PlotMap[plotContent] if (plotContent != "Custom") else st.sidebar.multiselect("Algorithms", Algorithms, key=key)
    
    col3, col4 = st.sidebar.beta_columns(2)
    sizes = range(1, col3.slider("Sample Sizes", min_value = 10, max_value = 1000, key=key)+1)
    depth = col4.slider("Execution Depth", min_value = 1, max_value = 30, key=key)

    if (state == "Static"):
        add_StaticPlot(plotName, functions, sizes, depth, position)
    else:
        add_DynamicPlot(plotName, functions, sizes, depth, position)

#----------------------------------------------------------------------------------------------------------
Compatible = ExistingPlot < PlotSize
add_new_plot = st.sidebar.checkbox("Add Plot", value=False, key=ExistingPlot)

while (add_new_plot):
    position = ExistingPlot+1
    Interface(position)
    ExistingPlot += 1
    if (Compatible == False):
        break
    add_new_plot = st.sidebar.checkbox("Add Plot", value=False, key=ExistingPlot)

st.pyplot(fig=fig, figsize=(12, 10), dpi=500)

