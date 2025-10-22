# Project Setup Guide

## 1. Create a Virtual Environment

To keep dependencies isolated from your system Python, it’s best to use a venv.

### For macOS / Linux

```bash
# Create a new virtual environment named 'venv'
python3 -m venv venv
```

```bash
# Activate the virtual environment
source venv/bin/activate
```

```bash
# Install Dependencies
pip install -r requirements.txt
```

### For Windows

Install linux

## 2. Run

### 1. Create and activate a virtual environment, install requirements for testing

```bash
make install
```
