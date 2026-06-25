pipeline {
    agent any // Usa qualsiasi agente Jenkins disponibile (macchina/worker)

    environment {
        // Cartella del virtual environment Python (dentro workspace Jenkins)
        VENV_DIR = "${WORKSPACE}\\venv"
         // Percorso dell'interprete Python installato sulla macchina
        PYTHON = "C:/Users/ottav/AppData/Local/Programs/Python/Python313-arm64/python.exe"
    }

    stages {
        stage('Setup virtual environment') {
            steps {
                bat """
                "%PYTHON%" -m venv "%VENV_DIR%" 
                "%VENV_DIR%\\Scripts\\python.exe" -m pip install --upgrade pip
                "%VENV_DIR%\\Scripts\\pip.exe" install selenium webdriver-manager pytest pytest-html
                """
            }
        }

        stage('Run Selenium tests with pytest') {
            steps {
                bat """
                "%VENV_DIR%\\Scripts\\python.exe" -m pytest test_demoqa.py ^
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