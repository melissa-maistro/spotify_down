from selenium import webdriver
from selenium.webdriver.common.by import By
import os

playlist = input("Playlist da scaricare: ")
n = input("Numero canzone da cui partire: ")
folder = input("Dove te la salvo? ")
print("OK!")

# Using Chrome to access web
chrome_options = webdriver.ChromeOptions()

adblock_extension = "/Users/melissamaistro/Desktop/3.25_0"
chrome_options.add_argument('load-extension=' + adblock_extension)

prefs = {'download.default_directory' : folder}
chrome_options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(30)

try:
    # Open the website
    driver.get("https://spotifydown.com/it")

    # Accept pop-up cookies
    alert = driver.find_element(By.CLASS_NAME, "fc-footer-buttons-container").get_property("children")[1]
    alert_close = alert.get_property("children")[0]
    alert_close.click()

    # Insert playlist link
    box = driver.find_element(By.CLASS_NAME, "relative")
    input = box.get_property("children")[0]
    input.send_keys(playlist)
    submit_button = driver.find_element(By.CSS_SELECTOR, r"button.transition.mt-3.w-full.m-auto.text-gray-100.cursor-pointer.p-2.rounded-full.bg-button.hover\:bg-button-active")
    submit_button.click()

    # Get number of total songs
    grid = driver.find_element(By.CLASS_NAME, "mb-12.grid.grid-cols-1.gap-3.m-auto")
    num_songs = len(grid.get_property("children"))

    # Download all songs
    for i in range(int(n)-1, num_songs):
        grid = driver.find_element(By.CLASS_NAME, "mb-12.grid.grid-cols-1.gap-3.m-auto")
        row = grid.get_property("children")[i]
        scarica_button = row.get_property("children")[1].get_property("children")[0]
        scarica_button.click()

        # Download song
        scarica_mp3_button = driver.find_element(By.CSS_SELECTOR, r"div.my-5.grid.sm\:grid-cols-2.gap-4.sm\:gap-2").get_property("children")[0]
        scarica_mp3_button.click()

        # Go back to avoid google vignette (maledette)
        driver.get("https://spotifydown.com/it")

        # Insert playlist link
        box = driver.find_element(By.CLASS_NAME, "relative")
        input = box.get_property("children")[0]
        input.send_keys(playlist)
        submit_button = driver.find_element(By.CSS_SELECTOR, r"button.transition.mt-3.w-full.m-auto.text-gray-100.cursor-pointer.p-2.rounded-full.bg-button.hover\:bg-button-active")
        submit_button.click()

except Exception as e:
    print("\n\n\nMaledetti pop-up, prova a rilanciare lo script\n\n\n", e)

driver.close()

if os.path.exists(folder):
    # Rename files without 'spotifydown.com - '
    string = 'spotifydown.com - '
    for file in os.listdir(folder):
        if file.startswith(string):
            oldName = os.path.join(folder, file)
            newName = os.path.join(folder, file[len(string):])
            os.rename(oldName, newName)

    if len(os.listdir(folder)) == 0:
        print(f"Nessuna canzone scaricata in {folder}")
    else:
        print(f"Canzoni scaricate in {folder} :")
        for file in os.listdir(folder):
            print(file)