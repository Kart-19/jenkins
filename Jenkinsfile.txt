pipeline {
  agent any
  stages {
    stage("Bulid"){
      steps {
        php build.php
      }
    }
    stage("Done"){
      steps {
        echo 'Php build done'
      }
    }
  }
}
