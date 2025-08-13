pipeline {
    agent any

    environment {
        BACKEND_DIR = "backend"
        FRONTEND_DIR = "frontend"
        EC2_HOST = "YOUR_EC2_PUBLIC_IP"
        SSH_KEY_ID = "your-ssh-key-id" // ID from Jenkins credentials
        S3_BUCKET = "your-s3-bucket-name"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/your-username/bookshelf.git'
            }
        }

        stage('Backend - Build & Deploy to EC2') {
            steps {
                sshagent(credentials: ["${SSH_KEY_ID}"]) {
                    sh """
                    ssh -o StrictHostKeyChecking=no ec2-user@${EC2_HOST} '
                        cd /home/ec2-user &&
                        rm -rf backend &&
                        mkdir backend &&
                        exit
                    '
                    scp -o StrictHostKeyChecking=no -r ${BACKEND_DIR}/* ec2-user@${EC2_HOST}:/home/ec2-user/backend

                    ssh -o StrictHostKeyChecking=no ec2-user@${EC2_HOST} '
                        cd backend &&
                        docker build -t bookshelf-backend . &&
                        docker stop bookshelf || true &&
                        docker rm bookshelf || true &&
                        docker run -d -p 5000:5000 --name bookshelf bookshelf-backend
                    '
                    """
                }
            }
        }

        stage('Frontend - Upload to S3') {
            steps {
                sh """
                aws s3 sync ${FRONTEND_DIR}/ s3://${S3_BUCKET} --delete
                """
            }
        }
    }
}
