# PHR - Clarify calculator specification requirements

- **ID:** 0002
- **Title:** Clarify calculator specification requirements
- **Stage:** spec
- **Date:** 2026-03-04
- **Feature:** calculator

## Prompt
I am writing a specification for  calculator python.
Let me clarify what success looks like with you:

1. What operations should my calculator support
2. What edge cases should I handle
3. What's my definition of "correct" for floating-point results
4. How should the calculator interface work
5. What should happen with invalid inputs

## Response
I will help you define the specification for your Python calculator by proposing a robust set of requirements for each of your points.

### 1. Surface & Success Criteria
**Surface:** Specification phase for a Python-based calculator.
**Success Criteria:** A finalized `specs/calculator/spec.md` that explicitly defines operations, error handling, and interface behavior.

### 2. Constraints, Invariants, and Non-Goals
*   **Constraints:** Must be implemented in Python; must use standard libraries unless otherwise specified.
*   **Invariants:** Mathematical results must be consistent with IEEE 754 standards for floating-point arithmetic.
*   **Non-Goals:** Building a Graphical User Interface (GUI) or supporting complex symbolic calculus (e.g., integration/differentiation) in this initial version.

---

### 3. Proposed Specification Details

#### 1. Operations Supported
*   **Basic:** Addition (+), Subtraction (-), Multiplication (*), Division (/).
*   **Advanced (Suggested):** Exponentiation (**), Floor Division (//), and Modulo (%).

#### 2. Edge Cases
*   **Division by Zero:** Must return a clear error message, not crash.
*   **Overflow/Underflow:** Handle extremely large or small numbers gracefully.
*   **Empty Input:** Handle cases where no expression is provided.

#### 3. Floating-Point "Correctness"
*   **Standard:** Use Python’s native float.
*   **Precision (Suggested):** Rounding for display (e.g., 10 decimal places), full precision internally.

#### 4. Interface Work
*   *Recommendation:* CLI Interactive REPL.

#### 5. Invalid Inputs
*   Clear error messages for non-numeric, malformed, or unknown inputs.

---

### 4. Follow-ups & Risks
*   **Risk:** Floating-point precision (e.g., 0.1 + 0.2).
*   **Follow-up:** Support parentheses?
*   **Follow-up:** Maintain history?
