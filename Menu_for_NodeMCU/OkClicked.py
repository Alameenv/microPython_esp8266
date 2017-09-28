import webrepl
from nokialcd import LCD
from menu import DrawMenu

lcd = LCD()

class Clicked(DrawMenu):

    subMenulcdSettings  = ['contrast', 'brightness', 'backlight:OFF', 'reset', 'back']
    subMenuWebrepl      = ['stop','back']
    subMenu3            = ['sub1', 'sub2', 'sub3', 'sub4', 'sub5', 'sub6', 'sub7', 'sub8', 'sub9']
    txArduino           = ['txOn', 'txOff', 'back']

    def __init__(self):
        super(Clicked, self).__init__(lcdObj=lcd)
        self.mainMenu('   MAIN MENU', 'LCD setting', 'WebREPL', 'Item3', 'txArduino',
                      'Item5', 'Item6', 'Item7', 'Item8','Item9', 'Item10')
        self.subMenu(0, self.subMenulcdSettings)
        self.subMenu(1, self.subMenuWebrepl)
        self.subMenu(2, self.subMenu3)
        self.subMenu(3, self.txArduino)


    def run(self):
        self.loop()

    def mainMenuItemClicked(self):
        if self.getMainMenuPage() == 1:
            if self.getCursor() == 3:
                self.showSubMenuItems(0, ' LCD setting')
            if self.getCursor() == 4:
                self.showSubMenuItems(1, '   WebREPL')
            if self.getCursor() == 5:
                self.showSubMenuItems(2, '  MAIN ITEM3')
            if self.getCursor() == 6:
                self.showSubMenuItems(3, '  txArduino')
        if self.getMainMenuPage() == 2:
            if self.getCursor() == 3:
                print('Item5')

    def subMenuItemClicked(self):
        if self.getSubMenuID() == 0:
            if self.getSubMenuPage() == 1:
                if self.getCursor() == 3 and self.getOkButtonValue() == 0:
                    self.slider(1, '  Contrast', minValue=0, maxValue=19, defaultVal=10)

                if self.getCursor() == 4 and self.getOkButtonValue() == 0:
                    self.slider(2, '  brightness', minValue=0, maxValue=1023, defaultVal=512)

                if self.getCursor() == 5 and self.getOkButtonValue() == 0:
                    txt1 = self.convertibleText(self.getCursor(), 2, self.subMenulcdSettings, 'backlight:OFF', 'backlight:ON')
                    if txt1 == 'backlight:OFF':
                        self.setSliderInfo(2, 1023)
                        self.setLCDBacklightPWMduty(1023)
                    if txt1 == 'backlight:ON':
                        self.setSliderInfo(2, 1)
                        self.setLCDBacklightPWMduty(1)

                if self.getCursor() == 6 and self.getOkButtonValue() == 0:
                    txt2 = self.subMenulcdSettings[2]
                    if txt2 == 'backlight:ON':
                        self.subMenulcdSettings[2] = self.subMenulcdSettings[2].replace('backlight:ON', 'backlight:OFF')
                        lcd.println(2, 5, 'backlight:OFF')

                    self.setSliderInfo(2, 0)
                    self.setLCDBacklightPWMduty(512)

                    self.setSliderInfo(1, 0)
                    self.lcdContrast(10)

                if self.getOkButtonValue() == 0:
                    self.backToSubMenu()

            if self.getSubMenuPage() == 2:
                if self.getCursor() == 3 and self.getOkButtonValue() == 0:
                    self.backToMainMenu()

        if self.getSubMenuID() == 1:
            if self.getSubMenuPage() == 1:
                if self.getCursor() == 3 and self.getOkButtonValue() == 0:
                    repl = self.convertibleText(self.getCursor(), 0, self.subMenuWebrepl, 'stop', 'start')
                    if repl == 'stop':
                        webrepl.start()
                    if repl == 'start':
                        webrepl.stop()

                if self.getCursor() == 4 and self.getOkButtonValue() == 0:
                    self.backToMainMenu()

                if self.getOkButtonValue() == 0:
                    self.backToSubMenu()

        if self.getSubMenuID() == 2:
            if self.getSubMenuPage() == 1:
                if self.getCursor() == 5 and self.getOkButtonValue() == 0:
                    self.slider(3, '  Sub3', minValue=0, maxValue=19, defaultVal=10)
            if self.getSubMenuPage() == 2:
                if self.getCursor() == 5 and self.getOkButtonValue() == 0:
                    self.slider(4, '   Sub7', minValue=0, maxValue=19, defaultVal=10)
                if self.getOkButtonValue() == 0:
                    self.backToMainMenu()

        if self.getSubMenuID() == 3:
            if self.getSubMenuPage() == 1:
                if self.getCursor() == 3 and self.getOkButtonValue() == 0:
                    self.txSend('On\n\r')
                if self.getCursor() == 4 and self.getOkButtonValue() == 0:
                    self.txSend('Off\n\r')
                if self.getCursor() == 5 and self.getOkButtonValue() == 0:
                    self.backToMainMenu()
                if self.getOkButtonValue() == 0:
                    self.backToSubMenu()

    def sliderActionPerformed(self):
        if self.getSliderID() == 1:
            self.lcdContrast(self.getSliderValue())
        if self.getSliderID() == 2:
            self.setLCDBacklightPWMduty(self.getSliderValue())
