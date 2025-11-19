pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/ottaviomarciello-sketch/selenium_ci_pipeline.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t selenium-arm64 .'
            }
        }

        stage('Run Selenium Test in Docker') {
            steps {
                sh 'docker run --rm selenium-arm64'
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
