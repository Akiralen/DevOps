pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                # create docker image and print image ID
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
                # create container
                script{
                    scoreapp_container = scoreapp_image.run('-p 8777:8080 -v test:/app/scores')
                }
                # copy scores.txt to container
                sh "docker cp ./scores/scores.txt ${scoreapp_container.id}:/app/scores"
                # run test
                sh "/usr/bin/python3 e2e.py"
                # stop container
                script{
                    scoreapp_container.stop()
                }
            }
        }
        stage('Deploy') { 
            when{
                environment name 'image_push', value: 'true'
            }
            steps {
                    echo 'Deploying....'
                    # deploy image to conected repository
                    script{
                        scoreapp_image.push()
                    }
            }
        }
    }
}