pipeline {
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

