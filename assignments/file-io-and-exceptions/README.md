# 📘 Assignment: File I/O and Exceptions

## 🎯 Objective

Practice reading and writing files and handling common runtime errors in Python. Focus on robust input validation, clear error messages, and safe file operations.

## 📝 Tasks

### 🛠️ Read and Write Text Files

#### Description
Implement functions to read lines from an input file, transform the content, and write results to an output file.

#### Requirements
Completed program should:

- Read all lines from a file path provided by the user.
- Strip whitespace and ignore empty lines.
- Transform each line to uppercase and write to a new file (same folder, name: `output.txt`).
- Print a success message including the number of lines written.
- Example usage:
  ```python
  # input.txt -> ["hello", "world"]
  # output.txt -> ["HELLO", "WORLD"]
  ```

### 🛠️ Handle Errors Gracefully

#### Description
Add exception handling and validation to make the program robust for real-world usage.

#### Requirements
Completed program should:

- Handle missing files with a friendly message (e.g., FileNotFoundError).
- Validate that the provided path refers to a file, not a directory.
- Catch and report permission errors when reading/writing.
- Use `try/except` blocks and, when appropriate, `with open(...)` context managers.
- Optionally, log errors to `errors.log` in the same folder.
