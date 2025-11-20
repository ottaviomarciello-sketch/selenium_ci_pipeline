pipeline {
    agent any

    environment {
        VENV_DIR = "${WORKSPACE}/venv"
    }

    stages {
        stage('Setup virtual environment') {
            steps {
                sh '''
                python3 -m venv ${VENV_DIR}
                . ${VENV_DIR}/bin/activate
                pip install --upgrade pip
                pip install selenium webdriver-manager
                '''
            }
        }

        stage('Run Selenium test') {
            steps {
                sh '''
                . ${VENV_DIR}/bin/activate
                python ${WORKSPACE}/wikipedia_python.py
                '''
            }
        }
    }
}
