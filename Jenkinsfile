pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'python3 -m pip install --user -r requirements.txt'
            }
        }

        stage('Run Selenium Test') {
            steps {
                sh 'python3 wikipedia_python.py'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/*.log', allowEmptyArchive: true
        }
    }
}
