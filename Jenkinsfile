pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                script{
                    scoreapp_image = docker.build ("scoreapp:${env.BUILD_ID}","-f score.dockerfile .")
                }
                echo scoreapp_image.id
            }
        }
        stage('Test') {
            when{
                environment name: 'run_test', value: 'true'
            }
            steps {
                echo 'Testing..'
                script{
                    scoreapp_container = scoreapp_image.run('-p 8080:8777 -v test:/app/scores')
                }
                sh "docker cp ./scores/scores.txt ${scoreapp_container.id}:/app/scores"
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}