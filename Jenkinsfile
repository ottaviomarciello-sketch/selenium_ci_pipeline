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
                ${VENV_DIR}/bin/pip install --upgrade pip
                ${VENV_DIR}/bin/pip install selenium webdriver-manager
                '''
            }
        }

        stage('Check workspace') {
            steps {
                sh 'ls -R ${WORKSPACE}'
            }
        }

        stage('Run Selenium test') {
            steps {
                sh '''
                ${VENV_DIR}/bin/python ${WORKSPACE}/tests/test_wikipedia.py
                '''
            }
        }
    }
}
