pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clona il repository da GitHub
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                // Installa tutte le librerie Python dal requirements.txt
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Selenium Test') {
            steps {
                // Esegue lo script Selenium
                bat 'python wikipedia_python.py'
            }
        }

        stage('Check Python Version') {
            steps {
                // Controlla versione Python (utile per debugging)
                bat 'python --version'
                bat 'pip --version'
            }
        }
    }

    post {
        always {
            // Archivia eventuali log o file generati
            archiveArtifacts artifacts: '**/*.log', allowEmptyArchive: true
        }
    }
}
