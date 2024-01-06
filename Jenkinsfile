pipeline {
    agent any

    stages {
        
        stage('checkout') {
            steps {
                checkout scmGit(branches: [[name: '**']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/nirajjn76/python-flask-helloworld.git']])
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
    }
}
