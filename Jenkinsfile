pipeline {
    agent any

    environment {
        VENV_DIR = "${WORKSPACE}/venv"
    }

    stages {
        stage('Checkout SCM') {
            steps {
                git url: 'https://github.com/ottaviomarciello-sketch/selenium_ci_pipeline.git', branch: 'main'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Install Chromium') {
            steps {
                // Serve Chromium per Selenium
                sh '''
                    sudo apt-get update
                    sudo apt-get install -y chromium-browser chromium-chromedriver
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
            echo "Pipeline completata!"
        }
        failure {
            echo "Errore nella pipeline!"
        }
    }
}
