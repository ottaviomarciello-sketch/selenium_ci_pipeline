pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                bat 'pip install selenium webdriver-manager'
            }
        }

        stage('Run Selenium test') {
            steps {
                bat 'python wikipedia_python.py'
            }
        }
    }
}
