pipeline {
    agent any

    environment {
        VENV_DIR = "${WORKSPACE}\\venv"
        PYTHON = "C:/Users/ottav/AppData/Local/Programs/Python/Python313/python.exe"
    }

    stages {
        stage('Setup virtual environment') {
            steps {
                bat """
                "%PYTHON%" -m venv "%VENV_DIR%"
                "%VENV_DIR%\\Scripts\\pip.exe" install --upgrade pip
                "%VENV_DIR%\\Scripts\\pip.exe" install selenium webdriver-manager pytest pytest-html
                """
            }
        }

        stage('Run Selenium tests with pytest') {
            steps {
                bat """
                "%VENV_DIR%\\Scripts\\python.exe" -m pytest ^
                    --junitxml=report.xml ^
                    --html=report.html --self-contained-html
                """
            }
        }
    }

    post {
        always {
            junit 'report.xml'

            publishHTML(target: [
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'HTML Test Report'
            ])
        }
    }
}