pipeline {
    agent any
    stages {
        stage('Test Docker on machine') {
            steps {
                sh 'docker --version'
            }
        }
        stage('Build compose up Docker Image') {
            steps {
                   sh 'docker build -t server-app ./server'
//                    sh 'docker-compose up'
            }
        }
        stage('Build client Docker Image') {
            steps {
                   sh 'docker build -t client-app ./client'
            }
        }
        stage('Run server image') {
            steps {
                sh 'docker run -d --name server-app  -p 5050:5050 server-app'
                sh 'sleep 5'
            }
        }
        stage('Run client image') {
            steps {
                sh 'docker run -d --name client-app  -p 8081:8080 client-app'
                sh 'sleep 5'
            }
        }
//         stage('Check Site Health') {
//             steps {
//                 script {
//                     def siteURL = 'http://localhost:5050'
//
//                     // Use curl to check the site availability
//                     def response = sh(script: "curl -I -s -o /dev/null -w '%{http_code}' $siteURL", returnStdout: true).trim()
//
//                     // Check the response status code
//                     if (response == '200') {
//                         echo "Site is up and running"
//                     } else {
//                         error "Site is not accessible. Status code: $response"
//                     }
//                 }
//            }
//         }
//         stage('Shut down the running image') {
//             steps {
//                  sh 'docker ps'
//                  sh 'docker-compose down'
//
//                 //  sh 'docker kill wog'
//            }
//         }
//         stage('Deploy to dockerHub'){
//             steps {
//                 sh 'docker push danielmodilevsky/wog'
//             }
//         }
    }
}