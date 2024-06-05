pipeline {
    agent any

    stages {
        stage('Clone repository') {
            steps {
                git 'https://github.com/your-repo/random-number-app.git'
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
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials') {
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
        stage('SonarQube analysis') {
    steps {
        withSonarQubeEnv('SonarQube') {
            sh 'sonar-scanner'
        }
    }
}
    }
    post {
        success {
            emailext to: 'you@example.com',
                     subject: "SUCCESS: ${env.JOB_NAME} [${env.BUILD_NUMBER}]",
                     body: "Build succeeded"
        }
        failure {
            emailext to: 'you@example.com',
                     subject: "FAILURE: ${env.JOB_NAME} [${env.BUILD_NUMBER}]",
                     body: "Build failed"
            script {
                docker-compose down
            }
        }
    }
}
