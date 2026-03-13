pipeline {
    agent any

    environment {
        VENV_DIR = "${WORKSPACE}\\venv"
    }

    stages {
        stage('Setup virtual environment') {
            steps {
                bat """
                REM Crea virtual environment
                python -m venv "%VENV_DIR%"

                REM Aggiorna pip e installa dipendenze
                "%VENV_DIR%\\Scripts\\pip.exe" install --upgrade pip
                "%VENV_DIR%\\Scripts\\pip.exe" install selenium
                """
            }
        }

        stage('Check workspace') {
            steps {
                bat 'dir /s "%WORKSPACE%"'
            }
        }

        stage('Run Selenium test') {
            steps {
                bat """
                REM Esegui lo script Python usando il venv
                "%VENV_DIR%\\Scripts\\python.exe" "%WORKSPACE%\\wikipedia_python.py"
                """
            }
        }
    }
}