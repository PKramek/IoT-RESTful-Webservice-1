pipeline {
    agent any

    // environment {

    // }

    // options {
    //     timeout(10)
    // }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checkout..'
                checkout scm
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            when {
                branch 'dev'
            }

            steps {
                echo 'Deploying..'
                sh "git push -f https://git.heroku.com/iot-restful-webservice-prod.git HEAD:master"
            }
        }
    }
}
