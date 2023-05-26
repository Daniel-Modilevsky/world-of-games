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
                   sh 'docker build -t wog .'
                   sh 'docker-compose up'
                   sh 'sleep 5'
            }
        }
//         stage('Run docker image') {
//             steps {
//                 sh 'docker run -d --name wog -p 8777:5050 wog'
//                 sh 'sleep 5'
//             }
//         }
        stage('Check Site Health') {
            steps {
                script {
                    def siteURL = 'http://localhost:8777'

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
                 sh 'docker kill wog'
           }
        }
        stage('Deploy to dockerHub'){
            steps {
                sh 'docker push danielmodilevsky/wog'
            }
        }
    }
}