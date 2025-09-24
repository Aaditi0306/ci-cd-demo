pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/aaditi0306/ci-cd-demo.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building the HTML website...'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment step (manual for now)'
            }
        }
    }
}
