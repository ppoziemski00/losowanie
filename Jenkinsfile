pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
    }

    stages {
        stage('Clone repository') {
            steps {
                git 'https://github.com/your-repo/random-number-app.git'
            }
        }
        stage('Install Python Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("random-number-app:${env.BUILD_ID}")
                }
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python -m unittest discover tests'
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', DOCKERHUB_CREDENTIALS) {
                        dockerImage.push()
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
    post {
        success {
            emailext (
                subject: "Job '${env.JOB_NAME}' (${env.BUILD_NUMBER}) succeeded",
                body: "Proces przebiegł pomyślnie, nie napotkano błędów.",
                recipientProviders: [[$class: 'DevelopersRecipientProvider']]
            )
            script {
                sh 'docker-compose down'
            }
        }
        failure {
            emailext (
                subject: "Job '${env.JOB_NAME}' (${env.BUILD_NUMBER}) failed",
                body: "Napotkano błędy, sprawdź konsolę.",
                recipientProviders: [[$class: 'DevelopersRecipientProvider']]
            )
            script {
                sh 'docker-compose down'
            }
        }
    }
}
