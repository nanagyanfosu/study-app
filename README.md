 # Study Recommendation Expert System

## Overview
This project is a Study Recommendation Expert System built using Flask (Python) and Prolog. It provides personalized study recommendations based on different learning styles, study durations, difficulty levels, and motivation levels. Users can select their preferred study mode, and the system will suggest an effective study technique tailored to their input.

## Features
- Learning Style-Based Recommendations: Supports Visual, Auditory, and Kinesthetic learning styles.
- Time Consideration: Adapts suggestions for short or long study sessions.
- Difficulty Level Awareness: Accounts for easy, medium, or hard study materials.
- Motivation Level Factor: Adjusts recommendations for low or high motivation levels.
- Flask Web Interface: Users interact via a simple, user-friendly web form.
- Prolog Knowledge Base: Uses Prolog to define and retrieve recommendations.

## Technologies Used
- Python (Flask Framework): For backend logic and web development.
- SWI-Prolog (via PySWIP): For rule-based reasoning and recommendations.
- HTML/CSS: For the frontend interface.

## Installation and Setup
### Prerequisites
- Python 3.7+
- SWI-Prolog
- Flask
- PySWIP (Python-Prolog Interface)

### Installation Steps
1. Clone the repository:
   
  - git clone https://github.com/your-repo/study-recommendation-system.git

  - cd study-app-1

  - cd project
  
2. Install dependencies:

  - pip install flask pyswip
 
3. Ensure *SWI-Prolog* is installed and added to the system path.
4. Run the Flask application:

  - python app.py
   
5. Open the application in your web browser at `http://127.0.0.1:5000/`.

## Usage
1. Open the web interface.
2. Select your learning style, study duration, difficulty level, and motivation level.
3. Click Get Recommendation.
4. Receive a study tip tailored to your inputs.

## Knowledge Base (Prolog)
The system retrieves study tips using a Prolog knowledge base that defines rules based on Prolog: 
recommendation(visual, short, _, _, 'Use mind maps or flashcards to quickly review concepts.').
recommendation(auditory, long, _, _, 'Record yourself reading notes and play them back for review.').
recommendation(kinesthetic, _, hard, _, 'Break down the material into smaller tasks and practice repeatedly.').


## Troubleshooting
### Common Errors & Fixes
- SWI-Prolog not found: Ensure SWI-Prolog is installed and added to the system path.
- Prolog procedure not found: Ensure the knowledge base file is correctly loaded in PySWIP.

## Future Improvements
- Enhance the knowledge base with more dynamic and personalized recommendations.
- Add a user feedback system to improve suggestions.
- Implement machine learning to refine recommendations based on user interactions.

## Contributors
- Nana Yaa Ampadu - 1205428
- Theoford Nana Gyanfosu - 11303292
- Reuben Addo - 11019527
- Aseda Owusu 11130070




