pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                script{
                    scoreapp_image = docker.build ("scoreapp:${env.BUILD_ID}","-f score.dockerfile .")
                }
                echo scoreapp_image
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}