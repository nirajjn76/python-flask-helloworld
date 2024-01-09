pipeline {
    agent {
        label 'dev-node'
        }

    stages {
        
        stage('checkout') {
            steps {
                checkout scmGit(branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/nirajjn76/python-flask-helloworld.git']])
            }
        }
        
        stage('build') {
            steps {
                sh 'docker build -t nirajjn76/pythonflaskdemo:latest .'
            }
        }
        
        stage('push') {
            steps {
                sh 'docker push nirajjn76/pythonflaskdemo:latest'
            }
        }
        
        stage('pull') {
            steps {
                sh 'docker pull nirajjn76/pythonflaskdemo:latest'
            }
        }
        
        stage('take down previous version') {
            steps {
                sh 'docker rm -f myflaskapp'
            }
        }
        
        stage('deploy') {
            steps {
                sh 'docker run -d -p 5000:5000 --name=myflaskapp nirajjn76/pythonflaskdemo:latest'
            }
        }
    }
}