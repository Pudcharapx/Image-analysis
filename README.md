# Image Analysis Laboratory

This repository contains the source code, laboratory assignments, and discussion reports for the **Image Analysis** coursework. It demonstrates foundational and advanced concepts in digital image processing utilizing Python, OpenCV, and relevant data science libraries.

## 📌 Project Overview

This project serves as a comprehensive portfolio of image processing techniques, emphasizing practical implementation. The repository includes interactive Jupyter Notebooks and statically exported HTML documents, accessible via a modernized [Glassmorphism UI](index.html). Each laboratory assignment is meticulously documented with code-level explanations to facilitate understanding and reproducibility.

## 📂 Laboratory Modules

The coursework is divided into the following core modules:

### 1. Manual Grayscale and ROI (Lab 1)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)
- **Source:** `lab1_assignment.ipynb` / `lab1.html`
- **Focus Areas:**
  - Writing mathematical equations to convert RGB to Grayscale manually.
  - Comparing manual arithmetic results with OpenCV's built-in functions.
  - Slicing and cropping specific Region of Interest (ROI) from images.

### 2. Image Basics and Pixel Manipulation (Lab 2)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)
- **Source:** `lab2_assignment (2).ipynb` / `lab2.html`
- **Focus Areas:**
  - Reading, displaying, and converting color spaces (RGB/BGR to Grayscale).
  - Direct pixel access and multi-dimensional array manipulation (NumPy slicing).
  - Region of Interest (ROI) extraction.
  - Fundamental image thresholding techniques for binary segmentation.

### 3. Histograms and Contrast Adjustment (Lab 3)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)
- **Source:** `LAB_3 (1) (1).ipynb` / `lab3.html`
- **Focus Areas:**
  - Non-linear spatial filtering via Gamma Correction.
  - Histogram computation and Cumulative Distribution Function (CDF) analysis.
  - Image enhancement through Contrast Stretching and Histogram Equalization.

### 4. Noise Filtration and Image Sharpening (Lab 4)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)
- **Source:** `lab4_assignment.ipynb` / `lab4.html`
- **Discussion Report:** `Lab4 discussion report.md`
- **Focus Areas:**
  - Application of spatial domain filters (Box Filter, Median Filter) for noise reduction (e.g., Salt & Pepper noise).
  - Edge enhancement utilizing Laplacian Sharpening.
  - Data type management and prevention of arithmetic overflow via `numpy.clip`.

## ⚙️ Architecture and Automation

- **`index.html`**: The central entry point featuring a responsive Glassmorphism interface for seamless navigation across all laboratory reports.
- **`add_explanations.py`**: An automated Python pipeline that parses the raw Jupyter Notebooks, performs code-level analysis, and dynamically injects contextual markdown explanations prior to HTML compilation.

## 🚀 Getting Started

### Prerequisites
Ensure the following dependencies are installed in your environment:
- Python 3.x
- Jupyter Notebook / JupyterLab
- OpenCV (`opencv-python`)
- NumPy
- Matplotlib

### Execution and Export
To explore or modify the notebooks locally, initiate the Jupyter server:
```bash
jupyter notebook
```

To update the source code explanations and regenerate the HTML documentation, execute the provided automation pipeline:
```bash
# Inject contextual explanations into raw notebooks
python add_explanations.py

# Compile notebooks to static HTML format
jupyter nbconvert --to html "lab2_assignment (2).ipynb" --output lab2.html
jupyter nbconvert --to html "LAB_3 (1) (1).ipynb" --output lab3.html
jupyter nbconvert --to html "lab4_assignment.ipynb" --output lab4.html
```

---
*Developed for Image Analysis & Digital Image Processing Studies.*
