pipeline {
    agent any

    environment {
        VENV_DIR = "${WORKSPACE}/venv"
    }

    stages {
        stage('Setup virtual environment') {
            steps {
                sh '''
                # Crea virtual environment
                python3 -m venv ${VENV_DIR}

                # Attiva virtual environment
                . ${VENV_DIR}/bin/activate

                # Aggiorna pip e installa dipendenze
                pip install --upgrade pip
                pip install selenium
                '''
            }
        }

        stage('Check workspace') {
            steps {
                sh 'ls -R ${WORKSPACE}'
            }
        }

        stage('Run Selenium test') {
            steps {
                sh '''
                # Attiva virtual environment
                . ${VENV_DIR}/bin/activate

                # Esegui lo script Python
                python ${WORKSPACE}/wikipedia_python.py
                '''
            }
        }
    }
}
