pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main',
                    url: 'git@github.com:dhyanradh/bookshelf.git',
                    credentialsId: 'ec2-ssh-key'
            }
        }

        stage('Backend - Build & Deploy to EC2') {
            steps {
                sh '''
                echo "Building Docker image for backend..."
                docker build -t bookshelf-backend ./backend

                echo "Stopping old container (if running)..."
                docker stop bookshelf-backend || true
                docker rm bookshelf-backend || true

                echo "Starting new backend container..."
                docker run -d --name bookshelf-backend -p 5000:5000 bookshelf-backend
                '''
            }
        }

        stage('Frontend - Upload to S3') {
            steps {
                sh '''
                echo "Uploading frontend files to S3..."
                aws s3 sync ./frontend s3://your-s3-bucket-name --delete
                '''
            }
        }
    }
}
