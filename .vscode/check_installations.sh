
#!/bin/bash

# Function to check installation
check_installation() {
    if command -v $1 &> /dev/null; then
        echo "$2 is installed"
        $1 --version
    else
        echo "$2 is not installed"
    fi
}

# Checking software installations
check_installation "python3" "Python"
check_installation "pip" "pip"
check_installation "node" "Node.js"
check_installation "npm" "npm"
check_installation "psql" "PostgreSQL"
check_installation "mongosh" "MongoDB"
check_installation "heroku" "Heroku CLI"
