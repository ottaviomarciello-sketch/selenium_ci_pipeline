pipeline {
    agent any

    stages {
        stage('Run Selenium test') {
            steps {
                sh '''
                pip install selenium
                python <<EOF
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME
)

driver.get("https://www.wikipedia.org/")
print(driver.title)
driver.quit()
EOF
                '''
            }
        }
    }
}
