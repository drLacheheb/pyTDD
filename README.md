# Test-Driven Development (TDD) in Python

This project demonstrates the principles of **Test-Driven Development (TDD)** in Python by implementing a simple use cases. It showcases how TDD can be applied to ensure code correctness while maintaining flexibility and robustness, using **pytest** for unit testing.

## What is Test-Driven Development (TDD)?

TDD is a software development practice where tests are written before the actual implementation. The typical TDD cycle involves:

1. **Write a test**: Define a test that describes the desired functionality.
2. **Run the test**: The test will fail initially, as the code isn't implemented yet.
3. **Write the code**: Implement the smallest amount of code to pass the test.
4. **Refactor**: Clean up the code while ensuring the test still passes.
5. **Repeat**: Continue the cycle, building out the application.

TDD provides several benefits:
- **Faster feedback** on code quality.
- **Improved design** and modular code.
- **Better documentation** since tests clarify the expected behavior.

## Installation

1. Clone the repository:
   
   ```bash
   git clone https://github.com/drLacheheb/pyTDD.git
   cd pyTDD
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running Tests with pytest

To run the tests using **pytest**, execute the following command:

```bash
pytest
```

This will automatically discover and run all tests in the `tests/` directory. Pytest will show you a summary of the test results in the terminal.

## Benefits of TDD in This Project

- **Early Bug Detection**: Writing tests first allows issues to be identified and fixed early in the development process.
- **Modular Design**: TDD ensures that components are small, independent, and testable.
- **Easy Maintenance**: Each feature or bug fix is supported by tests, making it easy to extend or modify the project.
