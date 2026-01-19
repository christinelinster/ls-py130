# PY130: More Python Foundations

**Repository:** [https://github.com/christinelinster/ls-py130](https://github.com/christinelinster/ls-py130)

This course dives deep into the specific mechanics of the Python language, moving beyond basic syntax to explore advanced programming paradigms and professional workflows. The curriculum focuses on Functional Programming concepts, rigorous testing methodologies, and the ecosystem of packaging and distribution.

## Core Concepts Mastered

### Advanced Python Features
* **Functional Programming:** Utilizing **First-Class Functions** and **Higher-Order Functions** to write cleaner, more abstract code.
* **Closures & Decorators:** Leveraging scope to retain state and modifying behavior of functions using the `@decorator` syntax.
* **Generators:** Creating memory-efficient iterators using `yield` and generator expressions.
* **Advanced Arguments:** Mastering iterable unpacking and variable arguments (`*args`, `**kwargs`) for flexible function interfaces.


### Testing & Quality Assurance
* **Unittest Framework:** Writing robust test suites using Python's built-in `unittest` library.
* **SEAT Approach:** Structuring tests using the **S**etup, **E**xecute, **A**ssert, **T**eardown pattern.
* **Code Coverage:** Measuring the effectiveness of tests to ensure all code paths are verified.
* **Pure Functions:** Understanding Side Effects versus Pure Functions to write testable, predictable code.

### Packaging & Distribution
* **PyPI Standards:** Preparing projects for the Python Package Index.
* **Modules & Imports:** Understanding how Python resolves imports and how to structure packages for distribution.
* **Environment Management:** Installing and uninstalling packages and managing dependencies.

## Projects

### TodoList Application (Testing Suite)
Building a complete TodoList application is a core exercise, but the primary focus is on **Quality Assurance**.
* **Repository:** [View Project Code](https://github.com/christinelinster/ls-todolist)
* **Objective:** Write a comprehensive test suite for the application using `unittest`.
* **Key Skills:** Testing custom classes, verifying boolean equality, catching exceptions, and achieving high code coverage.

### Python Package Creation
The course culminates in packaging code for distribution.
* **Objective:** Structure a project with the necessary configuration files (`setup.py` / `pyproject.toml`) to be installed by other users.
* **Key Skills:** Module organization, dependency management, and local installation testing.

## Repository Structure

```text
ls-py130/
├── higher_order_function_examples/ # Examples of map, filter, reduce, and partials
├── exercises/                      # Exercises covering Closures, Decorators, and Iterables
├── practice_problems/              # Drills on advanced argument usage and generators
├── testing/                        # Unit testing suites and the TodoList Project
├── assessment_prep/                # Study guides and consolidated code examples
└── examples/                       # Miscellaneous snippets (File I/O, Context Managers)
```

## Key Takeaways
* Proficiency in writing "Pythonic" code using advanced language features.
* Ability to write testable code and maintain high-quality test suites.
* Understanding of Python's memory model (Garbage Collection and Reference Counting).
* Confidence in packaging code for reuse and distribution to the wider Python community.

## License
MIT
