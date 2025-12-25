# 📐 Linear Algebra for Machine Learning  
### Visual Foundations with Manim — Sam SciTech

Linear Algebra is the **core mathematical language of Machine Learning**.  
This folder contains **carefully designed Manim animations** that visually
explain linear algebra concepts *exactly as they are used in ML models* —
from vectors and matrices to transformations and high-dimensional intuition.

These animations are created for **Sam SciTech** with the goal of helping
learners **see what machine learning is actually doing under the hood**.

---

## 🎯 Why Linear Algebra Matters in Machine Learning

Every major ML and Deep Learning concept relies on linear algebra:

- Data is represented as **vectors**
- Datasets are **matrices**
- Model parameters are **weight vectors**
- Neural networks perform **linear transformations**
- Training is driven by **matrix multiplications**

If you understand linear algebra *visually*, ML becomes **simpler, clearer,
and far less abstract**.

---

## 🧠 Learning Philosophy

This repository focuses on:

- ✅ **Geometric intuition first**
- ✅ **Visual correctness (not just aesthetics)**
- ✅ **ML-aligned explanations**
- ✅ **Clean, reusable Manim scenes**
- ❌ No rote memorization
- ❌ No symbol overload without meaning

Every animation answers one question:

> *“What is the machine actually doing?”*

---

## 📂 Folder Structure

```text
Linear_Algebra/
├── Vector_Visualizations/
│   ├── vector_vs_line.py
│   ├── vector_components.py
│
├── Matrix_Operations/
│   ├── matrix_multiplication.py
│   ├── linear_transformation.py
│
├── Eigen_Concepts/
│   ├── eigenvectors_visual.py
│   ├── eigenvalues_intuition.py
│
└── README.md
```
Each .py file contains a self-contained Manim scene that corresponds
to a specific concept used in Machine Learning

---
## 🧩 Topics Covered (ML-Focused)

### 🔹 Vectors
- Feature vectors and data representation
- Direction vs magnitude in feature space
- Column vectors in ML datasets
- Why a vector is **not** a straight line
- Vector intuition behind dot products

### 🔹 Matrices
- Data matrices and batch representation
- Weight matrices in ML models
- Matrix multiplication as feature transformation
- Understanding linear layers geometrically

### 🔹 Linear Transformations
- Scaling, rotation, projection, and shear
- Transforming feature spaces
- How neural network layers reshape data
- Geometric meaning of affine transformations

### 🔹 Eigenvalues & Eigenvectors
- Principal directions in data
- Dominant features and stability
- Visual intuition behind PCA
- Dimensionality reduction concepts

---

## 🤖 Machine Learning Connections

Each visualization in this folder directly maps to machine learning concepts such as:

- Linear Regression
- Logistic Regression
- Gradient Descent (geometric intuition)
- Neural Network layers
- Principal Component Analysis (PCA)
- High-dimensional feature spaces

The goal is to **bridge mathematical intuition and ML implementation**.

---

## ▶️ Running the Animations

### Requirements
- Python 3.10+
- Manim Community Edition
- NumPy

### Example Command

```bash
manim -pqh filename.py classname
