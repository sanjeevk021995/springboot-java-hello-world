pipeline {

agent {
    kubernetes {
        yamlFile 'kubernetes-pod-template.yaml'

    }
}

  stages {

    stage('Test Maven') {
      steps {
        container('maven') {
          sh 'mvn -version'
        }
      }
    }

    stage('Test Kubectl') {
      steps {
        container('kubectl') {
          sh 'kubectl get pods -A'
        }
      }
    }

    stage('Test Helm') {
      steps {
        container('helm') {
          sh 'helm version'
        }
      }
    }
    stage('Test kaniko') {
      steps {
        container('kaniko') {
          sh 'executor version'
        }
      }
    }

  }

}