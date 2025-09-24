pipeline {
<<<<<<< HEAD
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
=======
  agent any
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Install & Test') {
      steps {
        sh 'python3 -m venv venv || true'
        sh '. venv/bin/activate && pip install -r requirements.txt'
        sh '. venv/bin/activate && pytest -q'
      }
    }
    stage('Build Docker Image') {
      steps {
        sh 'docker build -t ci-cd-demo:latest .'
      }
    }
  }
}

>>>>>>> c1bf04e9e2c3c3fc9dafd98951fa22bf2316a061
