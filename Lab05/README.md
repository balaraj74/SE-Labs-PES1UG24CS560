# Lab 5: Static Code Analysis — Student Scholarship Eligibility Screener

- **Assigned Repository:** [https://github.com/balaraj74/L5_11_scholarship_screener](https://github.com/balaraj74/L5_11_scholarship_screener)
- **Student SRN:** PES1UG24CS560
- **Student Name:** Balaraj R
- **Lab Status:** Completed & Verified
  - **Bandit Security Audit:** 0 vulnerabilities detected
  - **Flake8 PEP 8 Audit:** 0 style violations
  - **Pylint Score:** 10.00 / 10

---

## About the program

A scholarship screener. It computes a merit score from GPA and extracurricular credits, checks family income against a limit, and saves the shortlist to `scholarships.json`.

The original codebase had severe quality, style, and security vulnerabilities of the kind Pylint, Flake8, and Bandit are built to find.

## What was done

1. **Baseline Static Analysis:**
   - Ran `pylint`, `bandit`, and `flake8` to identify baseline defects:
     - `pylint_report_before.txt` (initial rating: 4.69/10)
     - `bandit_report_before.txt` (High severity B307 arbitrary code execution via `eval()`)
     - `flake8_report_before.txt` (unused imports, PEP 8 comparison violations, line length)

2. **GitHub Issue Tracking:**
   - Raised and documented issues on the assigned repository: [balaraj74/L5_11_scholarship_screener#1](https://github.com/balaraj74/L5_11_scholarship_screener/issues/1)

3. **Atomic 3-Tier Remediation Commits:**
   - **Commit 1 (Bandit Security):** Eliminated arbitrary code execution vulnerability `B307` in `calculate_merit_score()` by implementing an AST-based safe mathematical evaluator (`ast.parse` with strict binary/unary operator validation).
   - **Commit 2 (Pylint Quality & Architecture):** Resolved mutable default argument (`logs=None`), replaced bare `except: pass` with targeted exceptions, wrapped file I/O in context managers with UTF-8 encoding, added module/function docstrings, and resolved snake_case naming.
   - **Commit 3 (Flake8 PEP 8 Styling):** Removed unused imports (`math`, `sys`), refactored direct boolean comparisons (`== True`), and formatted line lengths to strictly under 79 characters.

4. **Verification & Post-Fix Reports:**
   - `bandit_report_after.txt` (0 vulnerabilities)
   - `flake8_report_after.txt` (0 warnings / errors)
   - `pylint_report_after.txt` (10.00 / 10 perfect score)

5. **Issue Documentation & Reflection:**
   - Completed `issues.md` with issue types, affected lines, and architectural fix approaches.
   - Completed `reflection.md` addressing prioritization rationale, multi-tool synergy, handling false positives, and CI/CD quality gate integration.

## Deliverables in this Folder

1. `scholarship_system.py`: Cleaned version with all security, architectural, and style defects resolved.
2. `issues.md`: Completed issue tracking table.
3. `reflection.md`: Thorough answers to all 4 reflection questions.
4. Static analysis reports:
   - `bandit_report_before.txt`, `bandit_report_after.txt`, `bandit_report.txt`
   - `flake8_report_before.txt`, `flake8_report_after.txt`, `flake8_report.txt`
   - `pylint_report_before.txt`, `pylint_report_after.txt`, `pylint_report.txt`
