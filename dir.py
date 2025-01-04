import os

# Define the directory structure and files
directories = {
    "DC_Complete/app": ["main.py", "app.py", "config.py"],
    "DC_Complete/app/templates": ["index.html", "base.html"],
    "DC_Complete/analysis": ["text_analysis.py", "data_extraction.py"],
    "DC_Complete/visualizations": ["visualization.py", "chart_generator.py"],
    "DC_Complete/visualizations/templates": ["charts.html"],
    "DC_Complete/dashboard": ["dashboard.py", "ui_components.py"],
    "DC_Complete/dashboard/templates": ["dashboard.html"],
    "DC_Complete/static/css": ["styles.css"],
    "DC_Complete/static/js": ["scripts.js"],
    "DC_Complete/static/images": [],
    "DC_Complete/deployment": ["Dockerfile", "requirements.txt", "deploy.sh"],
    "DC_Complete/tests": ["test_analysis.py", "test_visualizations.py", "test_dashboard.py"],
    "DC_Complete/docs": ["README.md", "docs.md"],
    "DC_Complete/logs": []
}

# Create directories and files
for dir_path, files in directories.items():
    # Create the directory if it doesn't exist
    os.makedirs(dir_path, exist_ok=True)
    
    # Create placeholder files
    for file_name in files:
        file_path = os.path.join(dir_path, file_name)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                file.write(f"# Placeholder for {file_name}\n")
            
print("Directories and files created successfully.")
