import subprocess


def check_installation(command, name):
    try:
        result = subprocess.run(
            command, shell=True, check=True, capture_output=True
        )
        print(f'{name} is installed')
        print(result.stdout.decode().strip())
    except subprocess.CalledProcessError:
        print(f'{name} is not installed')


def main():
    check_installation('python3 --version', 'Python')
    check_installation('pip --version', 'pip')
    check_installation('node --version', 'Node.js')
    check_installation('npm --version', 'npm')
    check_installation('psql --version', 'PostgreSQL')
    check_installation('mongosh --version', 'MongoDB')
    check_installation('heroku --version', 'Heroku CLI')


if __name__ == '__main__':
    main()
