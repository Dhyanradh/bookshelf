pipeline {
    agent any

    environment {
        AWS_REGION = "eu-north-1"
        ECR_REPO = "744918081105.dkr.ecr.eu-north-1.amazonaws.com/bookshelf-backend"
        FRONTEND_BUCKET = "bookshlve23"
        EC2_HOST = "ec2-user@13.60.203.183"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/dhyanradh/bookshelf.git'
            }
        }

        stage('Build & Push Backend Image') {
            steps {
                sh """
                aws ecr get-login-password --region $AWS_REGION \
                | docker login --username AWS --password-stdin $ECR_REPO

                docker build -t bookshelf-backend ./backend
                docker tag bookshelf-backend:latest $ECR_REPO:latest
                docker push $ECR_REPO:latest
                """
            }
        }

        stage('Upload Frontend to S3') {
            steps {
                sh """
                aws s3 sync ./frontend s3://$FRONTEND_BUCKET --delete
                """
            }
        }

        stage('Deploy to EC2') {
            steps {
                sh """
                ssh -o StrictHostKeyChecking=no $EC2_HOST '
                    docker pull $ECR_REPO:latest &&
                    docker stop bookshelf || true &&
                    docker rm bookshelf || true &&
                    docker run -d -p 5000:5000 --name bookshelf $ECR_REPO:latest
                '
                """
            }
        }
    }
}
