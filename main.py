from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.uix.gridlayout import GridLayout


class BaseLayout(GridLayout):
    def __init__(self, **kwargs):
        super(BaseLayout, self).__init__(**kwargs)
        with self.canvas.before:
            Color(1, 1, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        # Mengaitkan perubahan posisi dan ukuran widget dengan metode update_rect
        self.bind(pos=self.update_rect, size=self.update_rect)
    
    # Memperbarui posisi dan ukuran dari Rectangle    
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size




class PrintLabel(App):
    def build(self):
        self.title = 'Print Label Zebra'
        return BaseLayout()
    
if __name__=='__main__':
    PrintLabel().run()