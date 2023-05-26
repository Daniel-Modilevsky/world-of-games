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
//                 git branch: 'main', url: 'https://github.com/Daniel-Modilevsky/devops_practice_ex.git'
//                 sh 'docker rm danielmodilevsky/wog:1.0 '
                sh 'docker-compose up'
            }
        }
        stage('Test') {
            steps {
                sh 'sleep 5'
                sh 'curl localhost:5050'
                sh 'docker kill test-auth'
//                 sh 'docker kill test-auth'
            }
        }
    }
}