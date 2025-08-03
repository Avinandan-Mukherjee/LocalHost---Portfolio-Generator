# LocalHost - AI Portfolio Generator

## Made by Avinandan
A Flask web application that generates personalized portfolio websites using Google's Gemini AI. Simply provide your information, preferences, and an image, and get a complete, responsive portfolio website with HTML, CSS, and JavaScript.

## 🌟 Features

- **AI-Powered Generation**: Uses Google Gemini AI to create unique, professional portfolio websites
- **Customizable Themes**: Choose between dark and light themes with custom color preferences
- **Social Integration**: Add links to GitHub, LinkedIn, Instagram, and YouTube
- **Responsive Design**: Generated portfolios are mobile-friendly and responsive
- **Live Preview**: View your generated portfolio in real-time with code/preview toggle
- **Easy Download**: Download all files as a ZIP package




## 📋 Prerequisites

- Python 3.7+
- Google Gemini API key -> [Generate from here]([your-deployment-url-here](https://aistudio.google.com/apikey))
- Flask and dependencies (see requirements.txt)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/localhost-portfolio-generator.git
   cd localhost-portfolio-generator
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   GEMINI_API=your_google_gemini_api_key_here
   FLASK_KEY=any random string
   ```

6. **Run the application**
   ```bash
   python main.py
   ```

The application will be available at `http://localhost:5000`

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API` | Google Gemini API key | Yes |
| `FLASK_KEY` | Flask secret key for sessions ( Random String) | Yes |

### File Structure

```
localhost-portfolio-generator/
├── main.py                # Main Flask application
├── input_form.py          # WTForms form definitions
├── requirements.txt       # Python dependencies
├── Procfile              # Vercel deployment config
├── vercel.json           # Vercel deployment config
├── .gitignore            # Git ignore rules
├── .env                  # Environment variables (not in repo)
├── static/
│   ├── codes/            # Generated portfolio files
│   │   ├── images/       # Uploaded user images
│   │   │   └── profile_photo... # User uploaded images
│   │   ├── index.html    # Generated HTML file
│   │   ├── style.css     # Generated CSS file
│   │   └── script.js     # Generated JavaScript file
│   ├── inputstyle.css    # Form styling
│   ├── mystyle.css       # Preview page styling
│   └── myscript.js       # Preview page scripts
└── templates/
    ├── data.html         # Input form template
    └── generated.html    # Preview/download template
```

## 📝 Usage

1. **Fill out the form**:
   - Enter your personal information (name, email, education, company)
   - Upload a profile image (JPG, PNG, JPEG, WebP)
   - Add your skills and social media links
   - Choose theme preferences and colors
   - Add any special requests

2. **Generate your portfolio**:
   - Click "Generate Portfolio"
   - Wait for AI processing (usually 20-30 seconds)

3. **Preview and download**:
   - View the generated code and live preview
   - Toggle between different file views (HTML, CSS, JS)
   - Download all files as a ZIP package

## 🎨 Customization

The AI generates portfolios based on:
- **Theme**: Dark or light mode preference
- **Colors**: Custom color scheme (if specified)
- **Content**: Your personal information and skills
- **Style**: Professional, modern design with smooth animations
- **Special requests**: Any additional requirements you specify


## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


## 🐛 Known Issues

- Large images may take longer to process
- Generated portfolios require manual customization for complex layouts, will add a edit with AI later.
- API rate limits may apply based on your Gemini API plan

- Font Awesome for icons
- Prism.js for syntax highlighting
