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
    stage('Test Helm') {
      steps {
        container('helm') {
          
          
          sh '''
         helm uninstall springboot-demo -n demo
         sleep 60
         helm upgrade --install springboot-demo ./helm/springboot-chart --namespace demo --set image.repository=docker.io/sanjeevk95/springboot-demo --set image.tag=${BUILD_NUMBER} --force
          '''
          // sh '''
          
          // helm upgrade --install springboot-demo ./helm/springboot-chart --namespace demo 
          
          
          // '''
        }
      }
    }

  }


}
