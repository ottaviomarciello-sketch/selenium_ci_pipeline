pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'selenium-arm64'
        TEST_SCRIPT = 'wikipedia_python.py'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/ottaviomarciello-sketch/selenium_ci_pipeline.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE} .'
            }
        }

        stage('Run Selenium Test') {
            steps {
                sh """
                    docker run --rm \
                        -v \$PWD:/app \
                        -w /app \
                        ${DOCKER_IMAGE} \
                        python3 ${TEST_SCRIPT}
                """
            }
        }
    }

    post {
        always {
            echo 'Pipeline completata!'
        }
        failure {
            echo 'Errore nella pipeline!'
        }
    }
}
