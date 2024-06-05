pipeline {
    agent any

    environment {
        REPO = 'https://github.com/ppoziemski00/losowanie.git'
        BRANCH = 'main'
        DOCKER_IMAGE = 'random-number-app-image'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: "${BRANCH}", url: "${REPO}"
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${env.DOCKER_IMAGE}")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Stop any running instance of the container
                    sh 'docker stop random-number-app-container || true'
                    sh 'docker rm random-number-app-container || true'
                    // Run the container
                    sh "docker run -d -p 5000:5000 --name random-number-app-container ${env.DOCKER_IMAGE}"
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sleep 10 // Czekaj na uruchomienie kontenera
                    def response = sh(script: '''
                        curl -s http://localhost:5000/random_number
                    ''', returnStdout: true).trim()
                    echo "Response: ${response}"
                    if (!response.contains('number')) {
                        error "Test failed with response: ${response}"
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
            }
        }
    }

    post {
        always {
            steps {
                script {
                    // Ensure the Docker container is stopped and removed
                    sh 'docker stop random-number-app-container || true'
                    sh 'docker rm random-number-app-container || true'
                }
            }
        }
    }
}
