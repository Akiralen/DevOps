pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                def test_image = docker.build("scoresapp:${env.BUILD_ID}","-f score.dockerfile .")
                echo test_image
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