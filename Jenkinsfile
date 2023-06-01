pipeline {
    agent any
    stages {
        stage('Test Docker on machine') {
            steps {
                sh 'docker --version'
            }
        }
        stage('Build server Docker Image') {
            steps {
                   sh 'docker build -t server-app ./server'
//                    sh 'docker-compose up'
            }
        }
        stage('Build client Docker Image') {
            steps {
                   sh 'docker build -t client-app ./client'
//                    sh 'docker-compose up'
            }
        }
        // stage('Run docker image') {
        //     steps {
        //         sh 'docker run -d --name wog -p 5050:5050 wog'
        //         sh 'sleep 5'
        //     }
        // }
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