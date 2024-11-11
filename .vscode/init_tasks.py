import logging
import os
import subprocess
import sys
import time

import fancy_text

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')


def run_command(command):
    """Run a shell command and return True if successful."""
    try:
        result = subprocess.run(command, shell=True, check=True)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        logging.error(f"Command '{command}' failed with error: {e}")
        return False


def check_installation(command, name):
    """Check if a command is available and print the result."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            capture_output=True,
        )
        logging.info(f'{name} is installed')
        logging.info(result.stdout.decode().strip())
    except subprocess.CalledProcessError:
        logging.error(f'{name} is not installed')


def install_vscode_extensions(extensions_dir):
    """Install VS Code extensions from .vsix files."""
    if os.path.exists(extensions_dir) and any(
        fname.endswith('.vsix') for fname in os.listdir(extensions_dir)
    ):
        for file in os.listdir(extensions_dir):
            if file.endswith('.vsix'):
                file_path = os.path.join(extensions_dir, file)
                logging.info(f'📦 Installing extension: {file_path}')
                if run_command(f'code --install-extension {file_path}'):
                    logging.info(f'✅ Successfully installed: {file_path}')
                else:
                    logging.error(
                        f'❌ Failed to install: {file_path}. Please check the file or try installing manually.'
                    )
    else:
        logging.warning(
            f'⚠️ No .vsix files found in {extensions_dir}. Skipping installation.'
        )


def install_requirements():
    """Install dependencies from requirements.txt."""
    if os.path.isfile('requirements.txt'):
        logging.info('📄 requirements.txt found. Installing dependencies...')
        if run_command('pip install -r requirements.txt'):
            logging.info(
                '✅ Dependencies from requirements.txt installed successfully!'
            )
        else:
            logging.error(
                '❌ Failed to install dependencies. Please check requirements.txt for errors.'
            )
            sys.exit(1)
    else:
        logging.warning(
            '⚠️ requirements.txt not found. Skipping dependency installation.'
        )


def main():
    """Run the setup tasks."""
    logging.info(fancy_text.setup_preparing)
    logging.info('🔄 Please wait while the setup is in progress...')

    for i in range(10):
        print('.', end='', flush=True)
        time.sleep(0.5)
    print()

    logging.info('🔍 Checking installations...')
    check_installation('python3 --version', 'Python')
    check_installation('pip --version', 'pip')
    check_installation('node --version', 'Node.js')
    check_installation('npm --version', 'npm')
    check_installation('psql --version', 'PostgreSQL')
    check_installation('mongosh --version', 'MongoDB')
    check_installation('heroku --version', 'Heroku CLI')
    time.sleep(1)

    logging.info('🔄 Installing VS Code extensions from .vsix files...')
    extensions_dir = os.path.join(
        os.getenv('GITPOD_REPO_ROOT', ''), '.vscode', 'extensions'
    )
    install_vscode_extensions(extensions_dir)
    time.sleep(1)

    logging.info('🔍 Checking for requirements.txt file...')
    install_requirements()
    time.sleep(1)
    
    logging.info(fancy_text.setup_complete)


if __name__ == '__main__':
    main()
