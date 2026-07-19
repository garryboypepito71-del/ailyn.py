#!/bin/bash
# Deployment verification script

echo "========================================"
echo "AILYN HOUSE - DEPLOYMENT VERIFICATION"
echo "========================================"
echo ""

# Check Python version
echo "✓ Python version:"
python --version
echo ""

# Check requirements
echo "✓ Requirements.txt:"
cat requirements.txt
echo ""

# Verify all dependencies
echo "✓ Checking dependencies..."
python -m pip list | grep -E "streamlit|pandas"
echo ""

# Verify Python syntax
echo "✓ Verifying Python files..."
python -m py_compile streamlit_app.py && echo "  ✅ streamlit_app.py OK" || echo "  ❌ streamlit_app.py ERROR"
python -m py_compile ailyn.py.py && echo "  ✅ ailyn.py.py OK" || echo "  ❌ ailyn.py.py ERROR"
echo ""

# Check required files for deployment
echo "✓ Required deployment files:"
[ -f "streamlit_app.py" ] && echo "  ✅ streamlit_app.py exists" || echo "  ❌ streamlit_app.py MISSING"
[ -f "requirements.txt" ] && echo "  ✅ requirements.txt exists" || echo "  ❌ requirements.txt MISSING"
[ -f ".streamlit/config.toml" ] && echo "  ✅ .streamlit/config.toml exists" || echo "  ❌ .streamlit/config.toml MISSING"
[ -f "README.md" ] && echo "  ✅ README.md exists" || echo "  ❌ README.md MISSING"
[ -f ".gitignore" ] && echo "  ✅ .gitignore exists" || echo "  ❌ .gitignore MISSING"
echo ""

# Test imports
echo "✓ Testing imports..."
python -c "import streamlit; print('  ✅ Streamlit OK')" 2>&1 || echo "  ❌ Streamlit ERROR"
python -c "import pandas; print('  ✅ Pandas OK')" 2>&1 || echo "  ❌ Pandas ERROR"
python -c "from datetime import datetime; print('  ✅ Datetime OK')" 2>&1 || echo "  ❌ Datetime ERROR"
echo ""

echo "========================================"
echo "✅ DEPLOYMENT VERIFICATION COMPLETE"
echo "========================================"
echo ""
echo "Next steps:"
echo "1. git add ."
echo "2. git commit -m 'Ready for Streamlit Cloud deployment'"
echo "3. git push origin main"
echo "4. Go to https://share.streamlit.io"
echo "5. Click 'New app' and select streamlit_app.py as main file"
