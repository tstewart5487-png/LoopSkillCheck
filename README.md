# LoopSkillCheck

A Python repository for practicing and testing **loop** skills in Python and **DataFrame** operations through structured skill check exercises.

## Table of Contents

- [Overview](#overview)
- [Quick Access](#quick-access)
- [Repository Structure](#repository-structure)
- [For Loop Skill Checks](#for-loop-skill-checks)
- [DataFrame Skill Checks](#dataframe-skill-checks)
- [Key Concepts Covered](#key-concepts-covered)
- [How to Use](#how-to-use)
- [Getting Started](#getting-started)
- [Contributing](#contributing)

## Overview

This repository contains skill check exercises focused on mastering:
1. **Looping concepts and patterns** in Python
2. **DataFrame operations** with pandas

The exercises are organized by topic and progress in difficulty, covering fundamental to intermediate level skills. Each exercise includes both the assignment (`.md` file) and completed solution (`.py` file).

## Quick Access

### For Loop Skill Checks

| # | Description | Topics |
|---|---|---|
| [#1](#for-loop-work-1) | Fundamental for loop concepts | Basic iteration, range(), accumulators, conditionals |
| [#2](#for-loop-work-2) | Practical applications | Accumulator pattern, real-world scenarios |
| [#3](#for-loop-work-3) | Data cleaning with type() | Type checking, data validation |
| [#4](#for-loop-work-4) | Inventory data validation | Type checking, counting, data integrity |
| [#5](#for-loop-work-5) | Data deduplication & validation | Duplicate removal, unique filtering, advanced data cleaning |
| [#6](#for-loop-work-6) | Advanced loop patterns | Complex iterations, nested structures |

### DataFrame Skill Checks

| # | Description | Topics |
|---|---|---|
| [#1](#column-skill-check-1) | Column operations in DataFrames | Adding columns, calculations, data manipulation |
| [#2](#splitting-and-combining-columns) | Splitting and combining columns | String splitting, column merging, data restructuring |

---

## Repository Structure

```
LoopSkillCheck/
├── .idea/                                          # PyCharm IDE configuration
├── Columns in DataFrames/                          # DataFrame column operations
│   ├── Column skill check #1.md
│   ├── Column skill check #1.py
│   ├── Splitting and Combining Columns.md
│   └── Splitting and Combining Columns.py
├── For loop work # 1.md
├── For loop work #1.py
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
├── main.py
└── README.md                                       # This file
```

Each skill check is organized with:
- **`.md` file** - The skill check assignment with tasks to complete
- **`.py` file** - Solution file with completed implementations

---

## For Loop Skill Checks

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

### Column Skill Check #1
**Files:** [Column skill check #1.md](Columns%20in%20DataFrames/Column%20skill%20check%20%231.md) | [Column skill check #1.py](Columns%20in%20DataFrames/Column%20skill%20check%20%231.py)

**Location:** [Columns in DataFrames](Columns%20in%20DataFrames) directory

Column operations in DataFrames:
- Adding new columns to DataFrames
- Performing calculations on columns
- Data manipulation and transformation
- Working with pandas DataFrames

### Splitting and Combining Columns
**Files:** [Splitting and Combining Columns.md](Columns%20in%20DataFrames/Splitting%20and%20Combining%20Columns.md) | [Splitting and Combining Columns.py](Columns%20in%20DataFrames/Splitting%20and%20Combining%20Columns.py)

**Location:** [Columns in DataFrames](Columns%20in%20DataFrames) directory

String manipulation with DataFrame columns:
- Splitting columns by delimiters
- Combining multiple columns into one
- Data restructuring and reshaping
- Advanced text processing with pandas
- Real-world data transformation scenarios

---

## Key Concepts Covered

### Loop Fundamentals
- **For loops with sequences** - Iterating through lists, tuples, strings
- **Range function** - Creating sequences of numbers
- **Accumulator pattern** - Building totals and collections through loop iterations
- **Conditional logic in loops** - Using `if/else` statements within loops
- **Loop variable scope** - Understanding how loop variables work
- **Loop control flow** - Break, continue, and other control mechanisms

### Data Processing
- **Type checking** - Using `type()` to validate data types
- **Data validation** - Filtering and cleaning mixed-type data
- **Deduplication** - Removing duplicate entries with membership testing (`not in`)
- **Real-world applications** - Practical scenarios using loops for data processing

### DataFrame Operations
- **Column manipulation** - Adding and modifying DataFrame columns
- **Data calculations** - Performing operations on DataFrame data
- **Data transformation** - Reshaping and restructuring data
- **String splitting and joining** - Advanced text processing with columns
- **Column combination** - Merging multiple columns into single columns

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

---

## Getting Started

To run any of the Python files:

```bash
# For loop skill checks
python "For loop work #1.py"
python "For loop Work #2.py"
python "For loop work #3.py"
python "For loop work #4.py"
python "For loop work #5.py"
python "For loop work #6.py"

# DataFrame skill checks
python "Columns in DataFrames/Column skill check #1.py"
python "Columns in DataFrames/Splitting and Combining Columns.py"
```

---

## Learning Path

### Beginner (Start Here)
1. [For loop work #1](For%20loop%20work%20%231.py) - Learn basic loop concepts
2. [For loop Work #2](For%20loop%20Work%20%232.py) - Apply loops to real scenarios
3. [For loop work #3](For%20loop%20work%20%233.py) - Introduce type checking

### Intermediate
4. [For loop work #4](For%20loop%20work%20%234.py) - Data validation with loops
5. [For loop work #5](For%20loop%20work%20%235.py) - Advanced data cleaning
6. [For loop work #6](For%20loop%20work%20%236.py) - Complex patterns

### DataFrames
7. [Column Skill Check #1](Columns%20in%20DataFrames/Column%20skill%20check%20%231.py) - DataFrame operations
8. [Splitting and Combining Columns](Columns%20in%20DataFrames/Splitting%20and%20Combining%20Columns.py) - Advanced column manipulation

---

## Contributing

To add new skill checks:
1. Create new files with the naming convention `For loop work #X.md` (assignment) and `For loop work #X.py` (solution)
2. Or for DataFrame content: `Column skill check #X.md` and `Column skill check #X.py` or other relevant names like `Splitting and Combining Columns.md`
3. Write your assignment and solutions following the existing format
4. Add a new row to the appropriate [Quick Access](#quick-access) table
5. Add a new subsection under [For Loop Skill Checks](#for-loop-skill-checks) or [DataFrame Skill Checks](#dataframe-skill-checks)

---

## Disclaimer

**About this Repository:**

- This README was generated with AI assistance (GitHub Copilot) based on prompts from the repository creator. The exercises, solutions, and structure were developed collaboratively.
- All skill checks in this repository cover **basic but necessary** foundational concepts in Python loop programming and data manipulation. These exercises are designed to build core competencies.
- This repository is created by and for beginners learning Python. If you're new to programming or loops, this is an appropriate resource for you. If you're looking for advanced loop concepts or advanced data science techniques, you may need to seek additional resources.

---

**Note:** This repository is designed to be expanded with additional skill checks covering different aspects of loop programming and DataFrame operations in Python.
