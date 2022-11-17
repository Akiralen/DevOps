pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                script{
                    sh"docker build -t scoreapp:${env.BUILD_ID} -f score.dockerfile ."
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
                sh "docker run -p 8080:8777 -v test /app/scores scoreapp:${env.BUILD_ID}"
                sh "docker cp ./scores/scores.txt ${scoreapp_container.id}:/app/scores/"
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}