pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/dhyanradh/bookshelf.git',
                    credentialsId: 'toktok'
            }
        }

        stage('Backend - Build & Deploy to EC2') {
            steps {
                echo 'Building and deploying backend...'
                // your backend build & deploy steps
            }
        }

        stage('Frontend - Upload to S3') {
            steps {
                echo 'Uploading frontend to S3...'
                // your frontend upload steps
            }
        }
    }
}
