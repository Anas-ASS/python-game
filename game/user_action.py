from kivy.uix.relativelayout import RelativeLayout

def on_keyboard_down(self, keyboard, keycode, text, modifiers):
    if keycode[1] == 'left':
        self.currentspeedx=self.speedx

    elif keycode[1] == 'right':
        self.currentspeedx=-self.speedx
        
    return True
def on_keyboard_up(self, keyboard, keycode):
    self.currentspeedx=0


def on_touch_down(self, touch):
    if not self.stategameover and self.statgamehasstarted:
        if touch.x<self.width/2:
            self.currentspeedx=self.speedx
        else:
            self.currentspeedx=-self.speedx
    return super(RelativeLayout,self).on_touch_down(touch)

def on_touch_up(self, touch):
    self.currentspeedx=0
def keyboard_closed(self):
    self._keyboard.unbind(on_key_down=self.on_keyboard_down)
    self._keyboard.unbind(on_key_up=self.on_keyboard_up)

    self._keyboard = None
