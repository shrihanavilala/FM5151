"""
Example executing a module with no inputs.
"""

if __name__ == "__main__":
    # You'll get here if you run `python app.py` from the shell
    print("Running as script")
else:
    # You'll get here if you run `import app` from within another module, REPL,
    # or Jupyter notebook
    print(f"Imported as module name={__name__}")
