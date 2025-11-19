pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
        PYTHON = "${VENV_DIR}/bin/python"
        PIP = "${VENV_DIR}/bin/pip"
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Env') {
            steps {
                sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Selenium Test') {
            steps {
                sh '''
                    . ${VENV_DIR}/bin/activate
                    python wikipedia_python.py
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/*.log', allowEmptyArchive: true
            echo 'Pipeline completata.'
        }
        failure {
            echo 'Errore nella pipeline!'
        }
    }
}
