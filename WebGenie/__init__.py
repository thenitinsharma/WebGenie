import os
import subprocess

# Boilerplate content for index.html
html_boilerplate = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="css/style.css">
    {framework_links}
</head>
<body>
    <h1>Welcome to {title}</h1>
    {framework_scripts}
    <script src="js/script.js"></script>
</body>
</html>
"""

# Boilerplate content for style.css
css_boilerplate = """body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

h1 {
    color: #333;
    text-align: center;
    margin-top: 50px;
}
"""

# Boilerplate content for script.js
js_boilerplate = """document.addEventListener('DOMContentLoaded', function() {
    console.log('JavaScript Loaded!');
});
"""

# Boilerplate content for database connection
db_boilerplate = """import sqlite3

def connect_db():
    conn = sqlite3.connect('database.db')
    print('Database connection successful')
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
    conn.commit()
    conn.close()

if _name_ == "_main_":
    create_table()
"""

# Boilerplate content for .gitignore
gitignore_boilerplate = """# Python
_pycache_/
*.pyc
*.pyo
*.pyd
env/
venv/
*.sqlite3
*.db
*.log

# Node.js
node_modules/

# Others
.DS_Store
"""

# Boilerplate content for README.md
readme_boilerplate = """# {title}

This is the {title} project.

## Description

{description}

## Installation

Instructions on how to install and run the project.

## Usage

Examples of how to use the project.

## License

Specify the license under which the project is distributed.
"""

def print_watermark():
    """Prints a watermark at the start of the CLI."""
    print("=========================================")
    print("Created by Nitin Kumar Sharma")
    print("=========================================\n")

def create_directory_structure(base_path):
    """Creates the necessary directory structure for the web project."""
    os.makedirs(os.path.join(base_path, 'css'), exist_ok=True)
    os.makedirs(os.path.join(base_path, 'js'), exist_ok=True)
    os.makedirs(os.path.join(base_path, 'db'), exist_ok=True)
    os.makedirs(os.path.join(base_path, 'assets'), exist_ok=True)

def create_files(base_path, title, description, framework_links, framework_scripts):
    """Creates the basic project files with boilerplate content."""
    with open(os.path.join(base_path, 'index.html'), 'w') as file:
        file.write(html_boilerplate.format(title=title, framework_links=framework_links, framework_scripts=framework_scripts))

    with open(os.path.join(base_path, 'css', 'style.css'), 'w') as file:
        file.write(css_boilerplate)

    with open(os.path.join(base_path, 'js', 'script.js'), 'w') as file:
        file.write(js_boilerplate)

    with open(os.path.join(base_path, 'db', 'database.py'), 'w') as file:
        file.write(db_boilerplate)

    with open(os.path.join(base_path, '.gitignore'), 'w') as file:
        file.write(gitignore_boilerplate)

    with open(os.path.join(base_path, 'README.md'), 'w') as file:
        file.write(readme_boilerplate.format(title=title, description=description))

def initialize_git_repo(base_path):
    """Initializes a git repository in the project directory."""
    subprocess.run(["git", "init", base_path], check=True)

def install_framework(framework, base_path):
    """Installs front-end framework/library if selected."""
    if framework == 'Bootstrap':
        return '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">', \
               '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>'
    elif framework == 'Tailwind CSS':
        return '<script src="https://cdn.tailwindcss.com"></script>', ''
    elif framework == 'React':
        return '', '<script src="https://unpkg.com/react@17/umd/react.development.js"></script><script src="https://unpkg.com/react-dom@17/umd/react-dom.development.js"></script>'
    elif framework == 'Vue.js':
        return '', '<script src="https://cdn.jsdelivr.net/npm/vue@2.6.14/dist/vue.js"></script>'
    elif framework == 'jQuery':
        return '', '<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>'
    return '', ''

def main():
    print_watermark()
    project_name = input("Enter your project name: ")
    title = input("Enter the title for your HTML document: ")
    description = input("Enter a brief description for your project: ")

    base_path = os.path.join(os.getcwd(), project_name)
    
    create_directory_structure(base_path)

    # Framework options
    print("Available frameworks/libraries: Bootstrap, Tailwind CSS, React, Vue.js, jQuery")
    framework_choice = input("Enter a framework/library to include (or leave blank for none): ")
    framework_links, framework_scripts = install_framework(framework_choice, base_path)

    # Create project files
    create_files(base_path, title, description, framework_links, framework_scripts)
    
    # Git setup
    git_choice = input("Would you like to initialize a git repository? (y/n): ")
    if git_choice.lower() == 'y':
        initialize_git_repo(base_path)
        print(f"Git repository initialized in {base_path}")
    
    print(f"Web project '{project_name}' created successfully with {framework_choice if framework_choice else 'no'} framework!")

if __name__ == "_main_":
    main()