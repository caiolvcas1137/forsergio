from time import sleep

import pyautogui

import keyboard

import button

sleep(4)


def pesca1():
     keyboard.key_down(0x1D)
     keyboard.press(0x2C)
     keyboard.release_key(0x1D)

def atack1():
    keyboard.press(button.key['F12'])
    keyboard.press(button.key['F11'])
    keyboard.press(button.key['F10'])
    keyboard.press(button.key['F9'])

def atack2():
    keyboard.press(button.key['F8'])
    keyboard.press(button.key['F7'])
    keyboard.press(button.key['F6'])
    keyboard.press(button.key['F5'])

def atack3():
    keyboard.press(button.key['F2'])
    keyboard.press(button.key['F3'])
    keyboard.press(button.key['F4'])

def bolhass():
     x_bolhas, y_bolhas = pyautogui.center(bolhas)
     pyautogui.moveTo(x_bolhas, y_bolhas)
     pyautogui.click()

def pokebola1(pokemon):
    keyboard.press(button.key['1'])
    position_x, position_y = pyautogui.center(pokemon)
    pyautogui.moveTo(position_x, position_y)
    pyautogui.click()

def pokebola2(pokemon):
    keyboard.press(button.key['2'])
    position_x, position_y = pyautogui.center(pokemon)
    pyautogui.moveTo(position_x, position_y)
    pyautogui.click()

def pokebola3(pokemon):
    keyboard.press(button.key['3'])
    position_x, position_y = pyautogui.center(pokemon)
    pyautogui.moveTo(position_x, position_y)
    pyautogui.click()


while True:
      bolhas = pyautogui.locateOnScreen('bolhas.PNG', confidence=0.65)
      print(bolhas)
      if bolhas != None:
     
       pesca1()

       atack1()

       pesca1()

       bolhass()

      scorsola = pyautogui.locateOnScreen('scorsola.PNG', confidence=0.80)
      if scorsola != None:
       pokebola1(scorsola)
      
      scontrol = pyautogui.locateOnScreen('scontrol.PNG', confidence=0.80)
      if scontrol != None:
       pokebola1(scontrol)

      skingler = pyautogui.locateOnScreen('skingler.PNG', confidence=0.80)
      if skingler != None:
       pokebola1(skingler)
      
      sludi = pyautogui.locateOnScreen('sludi.PNG', confidence=0.80)
      if sludi != None:
       pokebola1(sludi)

      rcorsola = pyautogui.locateOnScreen('rcorsola.PNG', confidence=0.80)
      if rcorsola != None:
       pokebola2(rcorsola)

      spoli = pyautogui.locateOnScreen('spoli.PNG', confidence=0.80)
      if spoli != None:
       pokebola1(spoli)

      scharp = pyautogui.locateOnScreen('scharp.PNG', confidence=0.80)
      if scharp != None:
       pokebola1(scharp)

      scruel = pyautogui.locateOnScreen('scruel.PNG', confidence=0.80)
      if scruel != None:
       pokebola1(scruel)

      sempoli = pyautogui.locateOnScreen('sempoli.PNG', confidence=0.80)
      if sempoli != None:
       pokebola1(sempoli)

      slapras = pyautogui.locateOnScreen('slapras.PNG', confidence=0.80)
      if slapras != None:
       pokebola1(slapras)

      sgreni = pyautogui.locateOnScreen('sgreni.PNG', confidence=0.80)
      if sgreni != None:
       pokebola1(sgreni)

      sfera = pyautogui.locateOnScreen('sfera.PNG', confidence=0.80)
      if sfera != None:
       pokebola1(sfera)

      sswamp = pyautogui.locateOnScreen('sswamp.PNG', confidence=0.80)
      if sswamp != None:
       pokebola1(sswamp)

      stoise = pyautogui.locateOnScreen('stoise.PNG', confidence=0.80)
      if stoise != None:
       pokebola1(stoise)

      smilo = pyautogui.locateOnScreen('smilo.PNG', confidence=0.80)
      if smilo != None:
       pokebola1(smilo)

      sgya = pyautogui.locateOnScreen('sgya.PNG', confidence=0.80)
      if sgya != None:
       pokebola1(sgya)

      scrow = pyautogui.locateOnScreen('scrow.PNG', confidence=0.80)
      if scrow != None:
       pokebola1(scrow)

      rslow = pyautogui.locateOnScreen('rslow.PNG', confidence=0.80)
      if rslow != None:
       pokebola3(rslow)

      sesteam = pyautogui.locateOnScreen('sesteam.PNG', confidence=0.80)
      if sesteam != None:
       pokebola1(sesteam)

      stox = pyautogui.locateOnScreen('stox.PNG', confidence=0.80)
      if stox != None:
       pokebola1(stox)


      bolhas = pyautogui.locateOnScreen('bolhas.PNG', confidence=0.65)
      print(bolhas)
      if bolhas != None:
     

        pesca1()

        atack2()

        pesca1()

        bolhass()

      bolhas = pyautogui.locateOnScreen('bolhas.PNG', confidence=0.65)
      print(bolhas)
      if bolhas != None:

       pesca1()

       atack3()

       pesca1()

       bolhass()









     