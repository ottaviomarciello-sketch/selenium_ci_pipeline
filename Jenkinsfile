pipeline {
    agent any

    stages {
        stage('Check workspace') {
            steps {
                echo "Contenuto della cartella workspace:"
                sh 'ls -R /var/jenkins_home/workspace/SeleniumTestPipeline/'
            }
        }

        stage('Setup virtual environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install selenium webdriver-manager
                '''
            }
        }

        stage('Run Selenium test') {
            steps {
                sh '''
                . venv/bin/activate
                python /var/jenkins_home/workspace/SeleniumTestPipeline/wikipedia_pom/tests/test_wikipedia.py
                '''
            }
        }
    }
}
