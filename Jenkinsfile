pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-p 5556:5556'
        }
    }

    stages {

        stage('Pre-Build Cleanup') {
            steps {
                sh 'pkill -f "python hello.py" || true'
            }
        }

        stage('Checkout') {
            steps {
                cleanWs()
                git 'https://github.com/ThomasMicheler/DEZSYS_JENKINS_HELLOSPENCER.git'
            }
        }

        stage('Build') {
            steps {
                sh 'python -m pip install --upgrade pip'
                sh 'pip install flask'
                sh 'pip install requests'
                sh 'pip install pytest'
                sh '[ ! -f count.txt ] || chmod 666 count.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'python -m pytest tests/test_hello.py -v'
            }
        }

        stage('Run') {
            steps {
                sh 'sleep 5 & nohup python src/hello.py &'
                sh 'curl http://localhost:5556/api/hello'
            }
        }

        stage('Test API') {
            steps {
                sh 'python tests/test_api.py'
            }
        }

        stage('Keep Alive') {
            steps {
                sh 'sleep infinity'
            }
        }
    }
}