from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Bot:
    def __init__(self, WPM):
        self.driver = webdriver.Firefox()
        self.website = "https://play.typeracer.com/"
        self.full_text = ""
        self.WPM = WPM
        self.time = 0

    def retrieve_text(self):
        span = self.driver.find_elements_by_xpath("//span[@unselectable='on']")

        if len(span) == 2:
            self.full_text = span[0].text + " " + span[1].text
        else:
            self.full_text = span[0].text + span[1].text + " "+ span[2].text

        self.time = (len(self.full_text) / self.WPM) / 60

def main():
    print("// typeracer-bot")
    print("// https://github.com/isaychris \n")

    tp = Bot(WPM=120)

    print("[1] Visiting website ...")
    tp.driver.get("https://play.typeracer.com/")
    tp.driver.implicitly_wait(5)
    link = tp.driver.find_element_by_link_text("Enter a typing race").click()

    print("[2] Retrieving text ...")
    tp.retrieve_text()

    print("[3] Waiting for countdown ...")
    input_field = WebDriverWait(tp.driver, 60).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input.txtInput")))

    print("- Typing now in session.")
    for letter in tp.full_text:
        input_field.send_keys(letter)
        sleep(tp.time)
    print("- Typing complete!")


if __name__ == "__main__":
    main()