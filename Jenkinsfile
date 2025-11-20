pipeline {
    agent any

    stages {
        stage('Run Selenium Test') {
            steps {
                sh 'python3 wikipedia_python.py'
            }
        }
    }

    post {
        always {
            echo 'Pipeline completata!'
        }
    }
}
