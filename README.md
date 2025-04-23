# DevDataAnalysis - Advanced Sentiment Analysis Platform

## Overview
DevDataAnalysis is a sophisticated data science platform that performs sentiment analysis on text data using Natural Language Processing (NLP) and Machine Learning techniques. The platform analyzes the emotional tone of text input, making it invaluable for various applications including:
- Customer Feedback Analysis
- Social Media Sentiment Monitoring
- Product Review Analysis
- Market Research Data Processing
- Brand Sentiment Tracking

## 🚀 Features
- Real-time sentiment analysis of text input
- Detailed sentiment scoring (Positive, Negative, Neutral)
- Compound sentiment score calculation
- Interactive web interface
- RESTful API endpoints
- Responsive design for all devices
- Modern, user-friendly interface

## 🛠️ Technology Stack

### Backend Technologies
- **Python 3.x** - Core programming language
- **Flask** - Web framework
- **NLTK** - Natural Language Processing toolkit
- **VADER Sentiment** - Sentiment analysis tool
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing and array operations
- **Scikit-learn** - Machine learning library
- **Gunicorn** - WSGI HTTP Server

### Frontend Technologies
- **HTML5** - Structure and content
- **CSS3** - Styling and animations
- **JavaScript** - Client-side functionality
- **Fetch API** - Asynchronous data handling

### Data Science Tools
- **Statistical Analysis** - Data interpretation
- **Text Preprocessing** - Data cleaning and preparation
- **Data Visualization** - Result presentation
- **Machine Learning Models** - Pattern recognition
- **Natural Language Processing** - Text analysis

### Development Tools
- **Git** - Version control
- **JSON** - Data interchange format
- **RESTful API** - Service architecture
- **Virtual Environment** - Dependency management

## 📋 Prerequisites
- Python 3.x
- pip (Python package manager)
- Virtual environment (recommended)

## 🔧 Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/DevDataAnalysis.git
cd DevDataAnalysis
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Access the application:
Open your browser and navigate to `http://localhost:8080`

## 🔄 API Endpoints

### POST /analyze
Analyzes the sentiment of provided text.

**Request Body:**
```json
{
    "text": "Your text to analyze"
}
```

**Response:**
```json
{
    "sentiment": "Positive/Negative/Neutral",
    "scores": {
        "pos": 0.0,
        "neg": 0.0,
        "neu": 0.0,
        "compound": 0.0
    }
}
```

## 📊 Sentiment Score Interpretation
- **Positive Score**: Measures the positivity (0 to 1)
- **Negative Score**: Measures the negativity (0 to 1)
- **Neutral Score**: Measures the neutrality (0 to 1)
- **Compound Score**: Aggregated score (-1 to 1)
  - ≥ 0.05: Positive sentiment
  - ≤ -0.05: Negative sentiment
  - Between -0.05 and 0.05: Neutral sentiment

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author
- **Devansh Sharma**
- Portfolio: [https://devanshsharma-git.github.io/Portfolio/](https://devanshsharma-git.github.io/Portfolio/)
- GitHub: [https://github.com/DevanshSharma-GIT](https://github.com/DevanshSharma-GIT)

## 🙏 Acknowledgments
- NLTK team for their comprehensive NLP toolkit
- VADER Sentiment Analysis tool developers
- Flask framework community 