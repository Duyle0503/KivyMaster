from kivymd.app import MDApp
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.utils import platform
from kivy.utils import get_color_from_hex
from kivymd.uix.button import MDFloatingActionButton
screen_helper = """

ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:

<MenuScreen>:
    md_bg_color: "#f7f2fa"

    name: 'menu'
    Image:
        source: 'st.gif'
        allow_stretch : True
        keep_ratio: True
        anim_delay : 0
        anim_loop : 1
        anim_reset : True
    MDRectangleFlatButton:
        text: 'Bắt đầu'
        font_style: 'Button'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'profile'
    MDRectangleFlatButton:
        text: 'Upload'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'upload'
 
<ProfileScreen>:
    name: 'profile'
    BoxLayout:
        MDBottomNavigation:     
            MDBottomNavigationItem:
                name: "icon1"
                text: "Home"
                icon: "home-assistant"
                MDRectangleFlatIconButton:
                    icon: "hand-heart"
                    text: "DONATE"
                    theme_text_color: "Custom"
                    text_color: 1, 0, 0, 1
                    line_color: 1, 0, 0, 1
                    icon_color: 1, 0, 0, 1
                    pos_hint: {"center_x": .2, "center_y": .95}
                MDLabel:
                    markup: True
                    font_size: 20
                    text: "[font=Roboto][color=#70427D][b]Chào bạn![/b]"
                    pos_hint: {"center_x": .4, "center_y": .95}
                    halign: 'right'

                MDFloatingActionButton:
                    name: "acv"
                    icon: "pencil"
                    type:   "large"
                    theme_icon_color: "Custom"
                    pos_hint: {"center_x": .25, "center_y": .25} 
                    on_press: root.manager.current = 'menu'
                MDFloatingActionButton:
                    name: "acv"
                    icon: "pencil"
                    type:   "large"
                    theme_icon_color: "Custom"
                    pos_hint: {"center_x": .25, "center_y": .5} 
                    on_press: root.manager.current = 'menu'
                MDFloatingActionButton:
                    name: "acv"
                    icon: "pencil"
                    type:   "large"
                    theme_icon_color: "Custom"
                    pos_hint: {"center_x": .25, "center_y": .75} 
                    on_press: root.manager.current = 'menu'
            #RIGHT
                MDFloatingActionButton:
                    name: "acv"
                    icon: "pencil"
                    type:   "large"
                    theme_icon_color: "Custom"
                    pos_hint: {"center_x": .75, "center_y": .75} 
                    on_press: root.manager.current = 'menu'
                MDFloatingActionButton:
                    name: "acv"
                    icon: "pencil"
                    type:   "large"
                    theme_icon_color: "Custom"
                    pos_hint: {"center_x": .75, "center_y": .5} 
                    on_press: root.manager.current = 'menu'
                MDFloatingActionButton:
                    name: "acv"
                    icon: "pencil"
                    type:   "large"
                    theme_icon_color: "Custom"
                    pos_hint: {"center_x": .75, "center_y": .25} 
                    on_press: root.manager.current = 'menu'

                
            MDBottomNavigationItem:
                name: "icon2"
                text: "Home"
                icon:  "layers-search"
            MDBottomNavigationItem:
                name: "icon3"
                text: "Home"
                icon:  "library"
            MDBottomNavigationItem:
                name: "icon4"
                text: "Home"
                icon:  "menu"
<icon1>:
    MDLabel:
        text: 'hello world'
        halign: 'center'           
<UploadScreen>:
    name: 'upload'
    MDLabel:
        text: 'Upload'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'
        
"""


class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class UploadScreen(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(UploadScreen(name='upload'))


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_color == "Purple"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.material_style = "M3"
        screen = Builder.load_string(screen_helper)
        if(platform == 'android' or platform == 'ios'):
            Window.maximize()
        else:
            Window.size = (300, 650)

        return screen


DemoApp().run()