pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                // se vuoi installare librerie Python
                sh 'pip install selenium webdriver-manager'
            }
        }

        stage('Run Selenium test') {
            steps {
                // esegue lo script Python
                sh 'python3 /var/jenkins_home/workspace/SeleniumTestPipeline/test_wikipedia.py'
            }
        }
    }
}
