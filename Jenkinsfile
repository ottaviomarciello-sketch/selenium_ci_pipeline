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
                sh '''
                    apt-get update && apt-get install -y chromium-browser \
                    fonts-liberation libnss3 libgconf-2-4 libx11-xcb1 libxcomposite1 \
                    libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxtst6 \
                    libatk-bridge2.0-0 libgtk-3-0 libasound2 --no-install-recommends
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
            archiveArtifacts artifacts: '**/output.log', allowEmptyArchive: true
            echo 'Pipeline completata.'
        }
        failure {
            echo 'Errore nella pipeline!'
        }
    }
}
