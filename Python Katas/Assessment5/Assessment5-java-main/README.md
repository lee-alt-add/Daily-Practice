# Java Practice Assessment - Module 5 (Maven Project)

## Purpose
This assessment helps you practice fundamental Java concepts using a Maven project structure. You will implement methods in `Assessment.java` and use JUnit 5 for Test-Driven Development (TDD).

## Learning Outcomes Assessed
- Understanding and implementing **Methods (Functions)**.
- Using **Loops (1D and 2D)** effectively.
- Applying **Control Flow Statements**.
- Working with **Data Structures** (`List`, `Map`, arrays).
- **Problem-solving skills** through algorithm design.
- **String Manipulation**.
- **TDD – Unit testing** with JUnit 5.

## Project Structure
This project follows a standard Maven directory layout:
- `src/main/java/com/assessment/Assessment.java`: Your implementation file.
- `src/test/java/com/assessment/AssessmentTest.java`: The JUnit test file.
- `pom.xml`: The Maven Project Object Model file (contains project configuration and dependencies).



## Files
- `Assessment.java` (in `src/main/java/...`): Implement the method stubs here.
- `AssessmentTest.java` (in `src/test/java/...`): Contains JUnit tests. **Do not modify this file.**
- `pom.xml` (in the project root): Manages dependencies (like JUnit) and build settings.
- `README.md` (this file).

## Setup and Running Tests with Maven

1.  **Prerequisites:**
    *   Java Development Kit (JDK) installed (the `pom.xml` provided targets Java 21).
    *   Apache Maven installed and configured in your system's PATH.
2. **Fork and clone the repository:**
    *   Fork the repository to your GitHub account.
    *   Clone the forked repository to your local machine using:
        ```bash
        git clone
3. **Import Project:**
    *   Clone or download the project files.
    *   Open your IDE (IntelliJ IDEA, Eclipse, VS Code with Java & Maven extensions) and import it as a Maven project. The IDE should automatically recognize `pom.xml` and set up dependencies.

4. **Understand the Tasks (TDD Approach):**
    *   **Red:** Open `AssessmentTest.java`. Review a test method (e.g., `testGenerateFibonacciSequence`). Run the tests *before* writing implementation code.
        *   From the command line (in the project root directory):
            ```bash
            mvn clean test
            ```
        *   Or, use your IDE's "Run Tests" feature (often by right-clicking `AssessmentTest.java` or the project).
        *   Tests should fail initially.
    *   **Green:** Open `Assessment.java`. Implement the logic for the method corresponding to the failing test. Re-run the tests. Aim to make the specific test pass.
    *   **Refactor:** (Optional) Improve your code's clarity or efficiency without changing its behavior (tests should still pass).

5. **Iterate:**
    *   Repeat the Red-Green-Refactor cycle for each method/test until all tests pass.

6. **Interpreting Test Results:**
    *   Maven will output test results to the console. `BUILD SUCCESS` with no test failures means you're done!
    *   If tests fail, Maven (and your IDE) will show which assertions failed, expected vs. actual values, and stack traces, helping you debug.

Good luck with your assessment! Remember, the goal is to practice and improve your Java skills through TDD. If you have any questions or need help, feel free to ask in the course forum or reach out.