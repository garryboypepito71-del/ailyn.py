# 🏗️ AILYN HOUSE PROJECT & PAYROLL PLANNER

**Advanced Construction Activity & Receipt Management System**

A sophisticated web-based application for managing construction projects, tracking receipts, managing payroll, and organizing project documentation with a modern glassmorphism UI design.

## Features

✨ **Key Features:**
- 📋 **Advanced Activity Logging** - Record construction activities with detailed descriptions
- 🧾 **Receipt Tracking** - Manage vendor receipts and invoice numbers
- 💰 **Financial Dashboard** - Real-time total expenditure tracking
- 📊 **Organized Ledger View** - Sort and view all activities by week and date
- 📥 **HTML Export** - Generate professional weekly receipts ledger as HTML documents
- 🎨 **Modern UI** - Premium glassmorphism design with dark theme

## Tech Stack

- **Frontend**: Streamlit (Python web framework)
- **Data Processing**: Pandas
- **Backend**: Python 3.8+

## Installation

### Local Setup

1. **Clone the Repository**
```bash
git clone https://github.com/garryboypepito71-del/ailyn.py.git
cd ailyn.py
```

2. **Create Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Run Locally**
```bash
streamlit run ailyn.py.py
```

The application will open at `http://localhost:8501`

## 🚀 Deploy to Streamlit Cloud

**Easiest Way to Publish Online:**

1. **Push to GitHub**
   - Create a GitHub repository
   - Push your code to GitHub

2. **Deploy on Streamlit Cloud**
   - Visit [streamlit.io/cloud](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New App"
   - Select your repository and branch
   - Specify `ailyn.py.py` as the main file
   - Deploy!

3. **Your app will be live at:**
   ```
   https://[your-username]-ailyn.streamlit.app
   ```

## SEO Optimization

The application includes:
- ✅ Proper page title and meta descriptions
- ✅ Open Graph tags for social media sharing
- ✅ Semantic HTML structure
- ✅ Responsive design
- ✅ Fast load times

## Usage Guide

### 1. **INPUT DASHBOARD** Tab
- Enter the date (Day, Month, Year)
- Add receipt details (optional):
  - Receipt/Invoice Number
  - Vendor/Store Name
  - Total Amount (PHP)
- Describe the structural work performed
- Click "Secure Log Into Ledger" to save

### 2. **ORGANISED PROJECT LEDGER** Tab
- View all logged activities organized by week
- See quick stats:
  - Total number of entries
  - Total materials spent
- Export complete ledger as HTML file

## File Structure

```
ailyn.py/
├── ailyn.py.py           # Main application file
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── .gitignore           # Git ignore rules
└── .devcontainer/       # Dev container configuration
```

## Configuration

No additional configuration needed! The app works out of the box with:
- Automatic date handling
- Session state management
- Responsive column layouts
- Data persistence during session

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or suggestions, please:
- Create an issue on GitHub
- Contact the development team

---

**Made with ❤️ for efficient project management**

**Version**: 1.0.0  
**Last Updated**: July 2026
