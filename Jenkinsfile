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
        stage('Run docker image') {
            steps {
                sh 'docker run -d --name wog:1.0 -p 5050:5050 wog:1.0'
                // docker run -d --name test-auth -p 5002:5000 danielmodilevsky/wog:1.0
                sh 'sleep 5'
//                 sh 'curl localhost:5050'
            }
        }
        stage('Check Site Health') {
            steps {
                script {
                    def siteURL = 'http://localhost:5050'

                    // Use curl to check the site availability
                    def response = sh(script: "curl -I -s -o /dev/null -w '%{http_code}' $siteURL", returnStdout: true).trim()

                    // Check the response status code
                    if (response == '200') {
                        echo "Site is up and running"
                    } else {
                        error "Site is not accessible. Status code: $response"
                    }
                }
           }
        }
        stage('Shut down the running image') {
            steps {
                 sh 'docker ps'
                 sh 'docker kill wog:1.0'
           }
        }
    }
}