# Import everything for GTK
from gi.repository import Gtk
import sys

# Import everything for the GPIO
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)


class MyWindow(Gtk.ApplicationWindow):

    def __init__(self, app):
        Gtk.Window.__init__(self, title="RadioButton Example", application=app)
        self.set_default_size(250, 100)
        self.set_border_width(20)

        button1 = Gtk.RadioButton(label="red")
        button1.connect("toggled", self.switch_lights)

        button2 = Gtk.RadioButton.new_from_widget(button1)
        button2.set_label("green")
        button2.connect("toggled", self.switch_lights)
        button2.set_active(False)

        button3 = Gtk.RadioButton.new_with_label_from_widget(
            button1, "blue")
        button3.connect("toggled", self.switch_lights)
        button3.set_active(False)

        button4 = Gtk.RadioButton.new_with_label_from_widget(
            button1, "Off")
        button4.connect("toggled", self.switch_lights)
        button4.set_active(False)

        # Gred for buttons.
        grid = Gtk.Grid.new()
        grid.attach(button1, 0, 0, 1, 1)
        grid.attach(button2, 0, 1, 1, 1)
        grid.attach(button3, 0, 2, 1, 1)
        grid.attach(button4, 0, 3, 1, 1)
        # Grid in window.
        self.add(grid)

    # Function to toggle the lights
    def switch_lights(self, button):
        if button.get_label() == "red":
            print("Red")
            GPIO.output(18, GPIO.LOW)
            GPIO.output(22, GPIO.LOW)
            GPIO.output(12, GPIO.HIGH)

        elif button.get_label() == "green":
            print("Green")
            GPIO.output(12, GPIO.LOW)
            GPIO.output(22, GPIO.LOW)

            GPIO.output(18, GPIO.HIGH)

        elif button.get_label() == "blue":
            print("Blue")
            GPIO.output(12, GPIO.LOW)
            GPIO.output(18, GPIO.LOW)

            GPIO.output(22, GPIO.HIGH)
        else:
            GPIO.output(12, GPIO.LOW)
            GPIO.output(18, GPIO.LOW)
            GPIO.output(22, GPIO.LOW)
            print("Off")


class MyApplication(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)


app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
