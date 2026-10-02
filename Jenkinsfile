pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the project...'
                checkout scm
            }
        }

        stage('Test') {
            steps {
                echo 'Installing dependencies and running application tests...'
                bat 'cd app && python -m pip install -r requirements.txt && python -m pytest tests/ -v'
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker image...'
                bat 'docker build -t flask-app .'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the stage logs.'
        }
    }
}git status