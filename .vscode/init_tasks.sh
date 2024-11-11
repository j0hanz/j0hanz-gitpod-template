#!/bin/sh

# Logging and fancy text output
python3 -c "import sys; sys.path.append('.vscode'); import fancy_text; print(fancy_text.setup_preparing)"

sleep 1

echo "🔄 Please wait while the setup is in progress..."

sleep 1

# Function to check installation with limited output
check_installation() {
    python3 -c "import sys; sys.path.append('.vscode'); import fancy_text; print(fancy_text.checking_installation.format(tool='$2'))"
    if command -v "$1" >/dev/null 2>&1; then
        echo "$2 is installed"
        "$1" --version | head -n 1
    else
        echo "$2 is not installed"
        return 1
    fi
}

# Function to install VS Code extensions with limited output
install_vscode_extensions() {
    python3 -c "import sys; sys.path.append('.vscode'); import fancy_text; print(fancy_text.installing_extensions)"
    EXT_DIR="${GITPOD_REPO_ROOT}/.vscode/extensions"
    if [ -d "$EXT_DIR" ]; then
        for file in "$EXT_DIR"/*.vsix; do
            if [ -f "$file" ]; then
                echo "Installing extension: $file"
                if code --install-extension "$file"; then
                    echo "✅ Successfully installed: $file"
                else
                    echo "❌ Failed to install: $file"
                fi
            fi
        done
    else
        echo "⚠️ No .vsix files found in $EXT_DIR. Skipping installation."
    fi
}

# Function to install Python dependencies with limited output
install_requirements() {
    python3 -c "import sys; sys.path.append('.vscode'); import fancy_text; print(fancy_text.installing_dependency.format(dependency='requirements.txt'))"
    if [ -f "requirements.txt" ]; then
        if pip install -r requirements.txt; then
            echo "✅ Dependencies installed successfully."
        else
            echo "❌ Failed to install dependencies."
            return 1
        fi
    else
        echo "⚠️ requirements.txt not found. Skipping installation."
    fi
}

# Main setup process
sleep 1

# Check for installations with minimal output
tools="python3 pip node npm psql mongosh heroku docker aws git"
names="Python pip Node.js npm PostgreSQL MongoDB Heroku CLI Docker AWS CLI Git"

for tool in $tools; do
    check_installation "$tool" "$tool" || echo "⚠️ $tool not installed or not found."
done

sleep 1
install_vscode_extensions

sleep 1
install_requirements

# Final message with minimal output
if [ $? -eq 0 ]; then
    python3 -c "import sys; sys.path.append('.vscode'); import fancy_text; print(fancy_text.setup_complete)"
else
    python3 -c "import sys; sys.path.append('.vscode'); import fancy_text; print(fancy_text.setup_failed)"
fi
