# LoopSkillCheck

A Python repository for practicing and testing **loop** skills in Python and **DataFrame** operations through structured skill check exercises.

## Table of Contents

- [Overview](#overview)
- [Quick Access](#quick-access)
- **🔄 [Loop Skill Checks](#loop-skill-checks)** ← *Master Python loops and iteration*
- **📊 [DataFrame Skill Checks](#dataframe-skill-checks)** ← *Master pandas and data transformation*
- [Key Concepts Covered](#key-concepts-covered)
- [How to Use](#how-to-use)
- [Getting Started](#getting-started)
- [Contributing](#contributing)

## Overview

This repository contains skill check exercises focused on mastering:
1. **Looping concepts and patterns** in Python - Core programming fundamentals using `for` loops
2. **DataFrame operations** with pandas - Data manipulation and analysis with tabular data

The exercises are organized by skill type and progress in difficulty, covering fundamental to intermediate level skills. Each exercise includes both the assignment (`.md` file) and completed solution (`.py` file).

## Quick Access

### 🔄 For Loop Skill Checks
*Master Python loop fundamentals and data processing with loops*

| # | Description | Topics |
|---|---|---|
| [#1](#for-loop-work-1) | Fundamental for loop concepts | Basic iteration, range(), accumulators, conditionals |
| [#2](#for-loop-work-2) | Practical applications | Accumulator pattern, real-world scenarios |
| [#3](#for-loop-work-3) | Data cleaning with type() | Type checking, data validation |
| [#4](#for-loop-work-4) | Inventory data validation | Type checking, counting, data integrity |
| [#5](#for-loop-work-5) | Data deduplication & validation | Duplicate removal, unique filtering, advanced data cleaning |
| [#6](#for-loop-work-6) | Advanced loop patterns | Complex iterations, nested structures |

### 📊 DataFrame Skill Checks
*Master pandas DataFrame operations and data transformation*

| # | Description | Topics |
|---|---|---|
| [#1](#column-skill-check-1) | Column operations in DataFrames | Adding columns, calculations, data manipulation |
| [#2](#splitting-and-combining-columns) | Splitting and combining columns | String splitting, column merging, data restructuring |

---

## Repository Structure

```
LoopSkillCheck/
├── .idea/                                          # PyCharm IDE configuration
│
├── FOR LOOP SKILL CHECKS (Root directory)
├── For loop work # 1.md                            # Assignment
├── For loop work #1.py                             # Solution
├── For loop Work #2.md
├── For loop Work #2.py
├── For loop work #3.md
├── For loop work #3.py
├── For loop work #4.md
├── For loop work #4.py
├── For loop work #5.md
├── For loop work #5.py
├── For loop work #6.md
├── For loop work #6.py
│
├── DATAFRAME SKILL CHECKS (Columns in DataFrames/)
├── Columns in DataFrames/
│   ├── Column skill check #1.md                   # Assignment
│   ├── Column skill check #1.py                   # Solution
│   ├── Splitting and Combining Columns.md
│   └── Splitting and Combining Columns.py
│
├── main.py                                         # PyCharm template file
└── README.md                                       # This file
```

---

## Loop Skill Checks

*Foundational Python programming exercises focused on mastering `for` loops, iteration patterns, and loop-based data processing.*

### For loop work #1
**Files:** [For loop work # 1.md](For%20loop%20work%20%23%201.md) | [For loop work #1.py](For%20loop%20work%20%231.py)

Fundamental `for` loop concepts covering:
- Basic list iteration
- Working with `range()`
- The accumulator pattern
- Combining loops with conditionals

### For loop Work #2
**Files:** [For loop Work #2.md](For%20loop%20Work%20%232.md) | [For loop Work #2.py](For%20loop%20Work%20%232.py)

Practical application of loop fundamentals:
- Real-world scenario-based challenges
- Accumulator pattern in context
- Calculating totals and aggregations

### For loop work #3
**Files:** [For loop work #3.md](For%20loop%20work%20%233.md) | [For loop work #3.py](For%20loop%20work%20%233.py)

Data cleaning with type checking:
- Using `type()` function for type checking
- Data validation and noise reduction
- Filtering non-numeric placeholder values
- Essential for AI/ML data preprocessing

### For loop work #4
**Files:** [For loop work #4.md](For%20loop%20work%20%234.md) | [For loop work #4.py](For%20loop%20work%20%234.py)

Inventory data validation:
- Verifying data integrity through type checking
- Counting valid numeric entries (`int` or `float`)
- Mixed-type list processing
- Real-world data cleaning scenarios

### For loop work #5
**Files:** [For loop work #5.md](For%20loop%20work%20%235.md) | [For loop work #5.py](For%20loop%20work%20%235.py)

Data deduplication & validation:
- Identifying and removing duplicate entries
- Filtering incorrect data types
- Building unique data collections with `not in` operator
- Advanced data preprocessing for machine learning
- Essential for handling raw, messy datasets

### For loop work #6
**Files:** [For loop work #6.md](For%20loop%20work%20%236.md) | [For loop work #6.py](For%20loop%20work%20%236.py)

Advanced loop patterns:
- Complex iteration structures
- Nested loop operations
- Optimization techniques
- Real-world data processing scenarios

---

## DataFrame Skill Checks

*Intermediate data manipulation exercises using pandas DataFrames. Learn to structure, transform, and analyze tabular data effectively.*

**Location:** All DataFrame skill checks are organized in the [Columns in DataFrames](Columns%20in%20DataFrames) directory

### Column Skill Check #1
**Files:** [Column skill check #1.md](Columns%20in%20DataFrames/Column%20skill%20check%20%231.md) | [Column skill check #1.py](Columns%20in%20DataFrames/Column%20skill%20check%20%231.py)

Column operations in DataFrames:
- Adding new columns to DataFrames
- Performing calculations on columns
- Data manipulation and transformation
- Working with pandas DataFrames

### Splitting and Combining Columns
**Files:** [Splitting and Combining Columns.md](Columns%20in%20DataFrames/Splitting%20and%20Combining%20Columns.md) | [Splitting and Combining Columns.py](Columns%20in%20DataFrames/Splitting%20and%20Combining%20Columns.py)

String manipulation with DataFrame columns:
- Splitting columns by delimiters
- Combining multiple columns into one
- Data restructuring and reshaping
- Advanced text processing with pandas
- Real-world data transformation scenarios

---

## Key Concepts Covered

### 🔄 Loop Fundamentals
- **For loops with sequences** - Iterating through lists, tuples, strings
- **Range function** - Creating sequences of numbers
- **Accumulator pattern** - Building totals and collections through loop iterations
- **Conditional logic in loops** - Using `if/else` statements within loops
- **Loop variable scope** - Understanding how loop variables work
- **Loop control flow** - Break, continue, and other control mechanisms
- **Type checking in loops** - Filtering and validating data during iteration
- **Deduplication** - Removing duplicate entries with membership testing (`not in`)

### 📊 DataFrame Operations
- **Column manipulation** - Adding and modifying DataFrame columns
- **Data calculations** - Performing operations on DataFrame data
- **Data transformation** - Reshaping and restructuring data
- **String splitting and joining** - Advanced text processing with columns
- **Column combination** - Merging multiple columns into single columns
- **Pandas methods** - Using built-in pandas functions for data manipulation

---

## How to Use

1. Select a skill check from the [Quick Access](#quick-access) table above
2. Click the number to jump to that skill check
3. Click the file links to access the assignment (`.md`) and solution (`.py`)
4. Write your solutions following the specified requirements
5. Compare your solutions with the completed examples in the `.py` file
6. Run the code to verify outputs

---

## Language

- **Python 3**
- **pandas** (for DataFrame skill checks)

---

## Getting Started

### Running Loop Skill Checks

```bash
python "For loop work #1.py"
python "For loop Work #2.py"
python "For loop work #3.py"
python "For loop work #4.py"
python "For loop work #5.py"
python "For loop work #6.py"
```

### Running DataFrame Skill Checks

```bash
python "Columns in DataFrames/Column skill check #1.py"
python "Columns in DataFrames/Splitting and Combining Columns.py"
```

---

## Learning Path

### 🔄 Loop Programming Path
**Start with these exercises to master Python loops:**

1. [For loop work #1](For%20loop%20work%20%231.py) - Learn basic loop concepts
2. [For loop Work #2](For%20loop%20Work%20%232.py) - Apply loops to real scenarios
3. [For loop work #3](For%20loop%20work%20%233.py) - Introduce type checking
4. [For loop work #4](For%20loop%20work%20%234.py) - Data validation with loops
5. [For loop work #5](For%20loop%20work%20%235.py) - Advanced data cleaning
6. [For loop work #6](For%20loop%20work%20%236.py) - Complex patterns

### 📊 DataFrame Learning Path
**After mastering loops, move on to DataFrame operations:**

7. [Column Skill Check #1](Columns%20in%20DataFrames/Column%20skill%20check%20%231.py) - DataFrame basics and column operations
8. [Splitting and Combining Columns](Columns%20in%20DataFrames/Splitting%20and%20Combining%20Columns.py) - Advanced column manipulation

---

## Contributing

To add new skill checks:

### For Loop Exercises
1. Create files with naming convention: `For loop work #X.md` (assignment) and `For loop work #X.py` (solution)
2. Place them in the repository root directory
3. Write your assignment and solutions following the existing format
4. Add a new row to the [For Loop Skill Checks](#for-loop-skill-checks-) table under Quick Access
5. Add a new subsection under [Loop Skill Checks](#loop-skill-checks)

### DataFrame Exercises
1. Create files in the `Columns in DataFrames/` directory
2. Use descriptive names like `Splitting and Combining Columns.md` for assignments and `.py` for solutions
3. Follow the existing format and structure
4. Add a new row to the [DataFrame Skill Checks](#dataframe-skill-checks-) table under Quick Access
5. Add a new subsection under [DataFrame Skill Checks](#dataframe-skill-checks)

---

## Disclaimer

**About this Repository:**

- This README was generated with AI assistance (GitHub Copilot) based on prompts from the repository creator. The exercises, solutions, and structure were developed collaboratively.
- All skill checks in this repository cover **basic but necessary** foundational concepts in Python loop programming and data manipulation. These exercises are designed to build core competencies.
- This repository is created by and for beginners learning Python. If you're new to programming or loops, this is an appropriate resource for you. If you're looking for advanced loop concepts or advanced data science techniques, you may need to seek additional resources.

---

**Note:** This repository is designed to be expanded with additional skill checks covering different aspects of loop programming and DataFrame operations in Python.
