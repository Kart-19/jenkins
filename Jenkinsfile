pipeline {
  agent any
  stages {
    stage("Bulid"){
      steps {
        sh 'php build.php'
      }
    }
    stage("version"){
      steps {
        sh 'php --version'
      }
    }
  }
}
