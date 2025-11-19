pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'selenium/standalone-chromium:arm64'
        TEST_SCRIPT = 'wikipedia_python.py' // il tuo script Python
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/ottaviomarciello-sketch/selenium_ci_pipeline.git', branch: 'main'
            }
        }

        stage('Build Docker Image (Optional)') {
            steps {
                // Se vuoi creare una tua immagine personalizzata
                sh 'docker build -t selenium-arm64 . || echo "Skipping custom build"'
            }
        }

        stage('Run Selenium Test in Docker') {
            steps {
                // Montiamo la cartella corrente dentro il container e lanciamo lo script Python
                sh """
                    docker run --rm -v \$PWD:/tests -w /tests $DOCKER_IMAGE \
                    python3 $TEST_SCRIPT
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
