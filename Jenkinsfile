pipeline {
  agent {
    docker {
      image 'rbekker87/build-tools:latest'
    }

  }
  stages {
    stage('test') {
      steps {
        sh 'echo $(hostname) > /tmp/hostname.txt'
        sh 'cat /tmp/hostname.txt'
      }
    }
  }
  environment {
    Owner = 'Ruan'
  }
}
