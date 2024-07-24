# UTF-8 Validation

## Overview

This project includes a Python module to validate UTF-8 encoding. The `validUTF8` function checks if a list of integers correctly represents UTF-8 encoded data.

## Requirements

- **Python Version**: Compatible with Python 3.4.3.
- **Editors**: Use `vi`, `vim`, or `emacs`.

## Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/your-repo/alx-interview.git
    ```

2. **Navigate to the Project Directory**:

    ```bash
    cd alx-interview/0x04-utf8_validation
    ```

3. **Set Up a Virtual Environment** (optional):

    ```bash
    python3.4 -m venv venv
    source venv/bin/activate
    ```

## Usage

To use the `validUTF8` function, import it in your Python script or interactive session:

```python
#!/usr/bin/python3
from 0-validate_utf8 import validUTF8

data = [65]
print(validUTF8(data))  # Output: True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # Output: True

data = [229, 65, 127, 256]
print(validUTF8(data))  # Output: False
