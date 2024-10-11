from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException
from selenium import webdriver

payload_file_path = 'xss-payload-list.txt'
output_file_path = 'it_worked.txt'
base_url = ''
driver = webdriver.Chrome()

try:
    with open(payload_file_path, 'r') as file:
        payloads = file.readlines()

    with open(output_file_path, 'a') as output_file:
        for payload in payloads:
            payload = payload.strip()
            full_url = base_url + payload
            driver.get(full_url)

            try:
                alert = Alert(driver)
                alert_text = alert.text
                if alert_text:
                    output_file.write(payload + '\n')
                    alert.accept()
            except NoAlertPresentException:
                continue

finally:
    driver.quit()
