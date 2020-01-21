node {
    def app

    stage('Clone repository') {
        checkout scm
    }

    stage('Build image') {
        app = docker.build("techchallange/latest")
    }

    stage('Test image') {
        app.inside {
            sh 'python test_myapp.py"'
        }
    }

    stage('Push image') {

        docker.withRegistry('https://registry.hub.docker.com', 'DockerHubCred') {
            app.push("${env.BUILD_NUMBER}")
            app.push("latest")
        }
    }
}

