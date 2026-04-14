# Sorting Algorithms — Data Structures Study

> University project · Comparing sorting algorithm performance in Python · Data Structures course

![Python](https://img.shields.io/badge/Python-3572A5?style=flat-square&logo=python&logoColor=white)
![University](https://img.shields.io/badge/University_Project-79c0ff?style=flat-square)
![Algorithms](https://img.shields.io/badge/Algorithms_%26_Data_Structures-a78bfa?style=flat-square)

A **Data Structures** university project that implements and compares different **sorting algorithms** in Python. The study uses a simulated dataset of **1,000 products** — each with price, rating, date, and category — to measure and compare the **execution time** of each algorithm across multiple sorting criteria.

---

## ⚙️ Algorithms implemented

| Algorithm | Strategy | Status |
|-----------|----------|--------|
| Bubble Sort | Compares and swaps adjacent elements. Supports ascending/descending order via custom `key` lambda. | ✅ Implemented |
| Quick Sort | Divide-and-conquer using pivot partitioning. Implemented recursively with in-place sorting. | ✅ Implemented |

---

## 📊 Sorting criteria

- Price — ascending and descending
- Rating — ascending and descending
- Date added — most recent and oldest
- Category — alphabetical order

---

## 📁 Project files

| File | Description |
|------|-------------|
| `NocoesDeOrdenancao.py` | Initial version — Quick Sort with a small dataset of 5 products |
| `version2.py` | Expanded version — Bubble Sort with 1,000 products and execution time measurement |
| `quadro_branco.py` | Whiteboard scratch file used during development |

---

## 🚀 How to run

```bash
# Clone the repository
git clone https://github.com/Victor-Emanuell/Trabalho-da-faculdade-sobre-Estrutura-de-Dados.git
cd Trabalho-da-faculdade-sobre-Estrutura-de-Dados

# Run the main version (Bubble Sort + timing)
python version2.py

# Run the Quick Sort version
python NocoesDeOrdenancao.py
```

No external dependencies — only Python standard library (`random`, `datetime`, `time`).

---

## 📚 Concepts covered

- Time complexity analysis in practice
- Object-oriented programming — `Produto` class with multiple attributes
- Higher-order functions — sorting with lambda `key` parameter
- Recursive algorithms — Quick Sort with in-place partitioning
- Execution time measurement with `time.time()`
- Random data generation for testing

---

## 👤 Author

**Victor Emanuell**
· [LinkedIn](https://www.linkedin.com/in/victor-albernaz-3b3220295/)
· [victoralberanz@gmail.com](mailto:victoralberanz@gmail.com)
