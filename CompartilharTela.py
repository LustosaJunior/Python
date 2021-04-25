import pywinauto
import polling2
import time

windows = pywinauto.Desktop(backend="uia").windows(class_name_re='.*Chrome.*', title_re='.*Chrome.*')

def get_chrome_alert():
    global windows
   
    if windows != pywinauto.Desktop(backend="uia").windows(class_name_re='.*Chrome.*', title_re='.*Chrome.*'):
        windows = pywinauto.Desktop(backend="uia").windows(class_name_re='.*Chrome.*', title_re='.*Chrome.*') + windows
       
    for window in windows:
        alert = None
        chrome = window
       
        for child in window.children():
            if 'Compartilhar sua tela' in child.get_properties()['texts']:
                alert = child
                return (chrome, alert)

while True:
    chrome, alert = polling2.poll(get_chrome_alert, step=0.5, poll_forever=True)

    tela_inteira = None
    compartilhar = None
    ocultar = None

    for children in alert.descendants():
        if 'Compartilhar' in children.get_properties()['texts']:
            compartilhar = children
        if 'A tela inteira' in children.get_properties()['texts']:
            tela_inteira = children
        if 'Ocultar' in children.get_properties()['texts']:
            ocultar = children

    #chrome.maximize()
    tela_inteira.click_input()
    compartilhar.click_input()
    time.sleep(1)
   
    windows = pywinauto.Desktop(backend="uia").windows(class_name_re=r'Chrome_WidgetWin_\d+')

    overlay = None
    for window in windows:
        texts = window.get_properties().get('texts', [])
        if not texts:
            continue

        if 'está compartilhando' in ''.join(texts):
            overlay = window

    for control in overlay.descendants():
        if 'ocultar' in ' '.join(control.get_properties().get('texts', [])).lower():
            ocultar = control
            print(ocultar)
            ocultar.click_input()
       
    time.sleep(1)