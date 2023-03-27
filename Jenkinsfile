pipeline {
  agent any
  stages {
    stage("Bulid"){
      steps {
        bat 'php build.php'
      }
    }
    stage("version"){
      steps {
        bat 'php --version'
      }
    }
  }
}
