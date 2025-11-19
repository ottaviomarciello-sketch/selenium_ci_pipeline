pipeline {
    agent {
        docker {
            image 'selenium/standalone-chrome:latest'
            args '-u root'  // serve per installare roba dentro
        }
    }

    stages {
        stage('Setup Python') {
            steps {
                sh '''
                apt-get update
                apt-get install -y python3 python3-pip
                pip3 install --upgrade pip
                pip3 install -r requirements.txt
                '''
            }
        }

        stage('Run Selenium Test') {
            steps {
                sh 'python3 wikipedia_python.py'
            }
        }
    }
}
