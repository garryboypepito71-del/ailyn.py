#!/usr/bin/env python3
"""Validation script for AILYN HOUSE Planner"""

import sys
import ast

def validate_python_syntax(filepath):
    """Check Python file for syntax errors"""
    try:
        with open(filepath, 'r') as f:
            ast.parse(f.read())
        return True, "✅ Syntax OK"
    except SyntaxError as e:
        return False, f"❌ Syntax Error: {e}"

def validate_requirements(filepath):
    """Check requirements.txt format"""
    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#'):
                if '==' not in line and line != '':
                    return False, f"❌ Invalid format: {line}"
        return True, "✅ Requirements OK"
    except Exception as e:
        return False, f"❌ Error: {e}"

def main():
    print("=" * 50)
    print("AILYN HOUSE PLANNER - VALIDATION CHECK")
    print("=" * 50)
    
    checks = [
        ("Python Syntax", lambda: validate_python_syntax("ailyn.py.py")),
        ("Requirements.txt", lambda: validate_requirements("requirements.txt")),
    ]
    
    all_passed = True
    for name, check in checks:
        passed, message = check()
        print(f"{name}: {message}")
        if not passed:
            all_passed = False
    
    print("=" * 50)
    if all_passed:
        print("✅ ALL CHECKS PASSED - Ready for deployment!")
        return 0
    else:
        print("❌ SOME CHECKS FAILED - Fix errors above")
        return 1

if __name__ == "__main__":
    sys.exit(main())
