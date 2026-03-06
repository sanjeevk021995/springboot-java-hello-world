pipeline {

agent {
    kubernetes {
        yamlFile 'kubernetes-pod-template.yaml'

    }
}


environment {

    DOCKER_REPO = "docker.io/sanjeevk95"
    IMAGE_NAME = "springboot-demo"
    IMAGE_TAG = "${BUILD_NUMBER}"

  }
  stages {

    stage('Test Maven') {
      steps {
        container('maven') {
          sh 'mvn clean package -DskipTests'
        }
      }
    }

    // stage('Test Kubectl') {
    //   steps {
    //     container('kubectl') {
    //       sh 'kubectl get pods -A'
    //     }
    //   }
    // }

    // stage('Test Helm') {
    //   steps {
    //     container('helm') {
    //       sh 'helm version'
    //     }
    //   }
    // }
    stage('Test kaniko') {
      steps {
        container('kaniko') {
          sh '''
          /kaniko/executor \
          --context $WORKSPACE \
          --dockerfile $WORKSPACE/Dockerfile \
          --destination=$DOCKER_REPO/$IMAGE_NAME:$IMAGE_TAG 

          echo " image pushed to dockerhub successfully"
          '''
        }
      }
    }

  }

}