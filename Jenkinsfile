pipeline {
    agent any
    stages {
        stage('Test Docker on machine') {
            steps {
                sh 'docker --version'
            }
        }
        stage('Build Docker Image') {
            steps {
                   sh 'docker build -t wog:1.0 .'
//                 git branch: 'main', url: 'https://github.com/Daniel-Modilevsky/devops_practice_ex.git'
//                 sh 'docker rm danielmodilevsky/wog:1.0 '
//                 sh 'docker-compose up'
            }
        }
        stage('Test') {
            steps {
                sh 'docker run -d -p 5050:5050 wog:1.0'
                // docker run -d --name test-auth -p 5002:5000 danielmodilevsky/wog:1.0
                sh 'sleep 5'
                sh 'curl localhost:5050'
                sh 'docker kill test-auth'
                sh 'docker kill wog:1.0'
            }
        }
    }
}