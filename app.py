from flask import Flask, render_template, jsonify
import plotly.express as px
import plotly.utils
import json
from flask_frozen import Freezer
freezer = Freezer(app)
app = Flask(__name__)

# Sample data for skills and achievements carousel
skills_data = {
    'Technical': ['Python', 'SQL', 'Java', 'Machine Learning', 'AI', 'IoT'],
    'Frameworks': ['Flask', 'OpenCV', 'MediaPipe', 'Plotly'],
    'Tools': ['Git', 'GitHub', 'VS Code', 'Arduino'],
    'Soft Skills': ['Team Leadership', 'Problem Solving', 'Communication']
}

projects_data = [
    {
        'title': 'Eyes Mouse',
        'category': 'AI & Accessibility',
        'thumbnail': 'eyes_mouse_thumb.jpg',
        'description': 'Eye movement-based mouse control using MediaPipe and OpenCV'
    },
    {
        'title': 'Online Voting System',
        'category': 'Web Development',
        'thumbnail': 'voting_thumb.jpg',
        'description': 'Secure voting platform with PHP and MySQL'
    },
    {
        'title': 'Story Generation AI',
        'category': 'Natural Language Processing',
        'thumbnail': 'story_ai_thumb.jpg',
        'description': 'Creative text generation using Cohere AI API'
    }
]

@app.route('/')
def home():
    return render_template('index.html', 
                         skills=skills_data,
                         projects=projects_data)

@app.route('/api/stats')
def get_stats():
    return jsonify({
        'projects': len(projects_data),
        'skills': sum(len(skills) for skills in skills_data.values()),
        'certifications': 5
    })

if __name__ == '__main__':
    app.run(debug=True)