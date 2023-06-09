import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# se connecter au site
driver.get("https://videotron.com/")
driver.maximize_window()
time.sleep(4)

# nbre d'images sur le site avec affichage sur la console
images = driver.find_elements(By.TAG_NAME,"img")
nbr_images = len(images)
print("le nombre d'image sur le site est : ",nbr_images)

# affichage de la valeur de l"attribut "alt" des images du site
i = 1
for image in images :
    alt = image.get_attribute("alt")
    if(alt == ""):
        print("l'attribut alt de l'image [",i,"] est : cette image ne possede pas d'attribut alt  ")
    else:
        print("l'attribut alt de l'image [",i,"] est :", alt)
    i = i + 1
print("****************************************************************")

# nbre de liens sur le site avec affichage sur la console
liens = driver.find_elements(By.TAG_NAME,"a")
nbr_liens = len(liens)
print('le nbre de liens sur le site est : ',nbr_liens)
print("****************************************************************")

# nbre de liens dans la section footer avec affichage dans la console

footer = driver.find_element(By.XPATH,"//footer[@class='videotron-ui__main-footer']")
liens_footer = footer.find_elements(By.TAG_NAME,"a")
print("le nombre de liens dans le footer est : " ,len(liens_footer))

# recuperer l'atribut "href" de chaque lien dans la section footer et l'afficher
j = 1
for lien_footer in liens_footer :
    href = lien_footer.get_attribute("href")
    print("href [",j,"] : ",href)
    j = j + 1








driver.quit()