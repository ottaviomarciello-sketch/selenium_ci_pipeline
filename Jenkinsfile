pipeline {
    agent any

    stages {
        stage('Setup virtual environment') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install selenium webdriver-manager
                '''
            }
        }

        stage('Run Selenium test') {
            steps {
                sh '''
                source venv/bin/activate
                python /var/jenkins_home/workspace/SeleniumTestPipeline/test_wikipedia.py
                '''
            }
        }
    }
}
