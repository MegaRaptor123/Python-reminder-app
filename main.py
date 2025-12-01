# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
import datetime

class ReminderApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.reminder_input = TextInput(hint_text='Reminder text', size_hint=(1, 0.2))
        self.add_widget(self.reminder_input)

        self.time_input = TextInput(hint_text='YYYY-MM-DD HH:MM', size_hint=(1, 0.2))
        self.add_widget(self.time_input)

        add_btn = Button(text='Add Reminder', size_hint=(1, 0.2))
        add_btn.bind(on_press=self.add_reminder)
        self.add_widget(add_btn)

        self.status_label = Label(text='No reminders yet', size_hint=(1, 0.4))
        self.add_widget(self.status_label)

        self.reminders = []
        Clock.schedule_interval(self.check_reminders, 10)  # check every 10 seconds

    def add_reminder(self, instance):
        text = self.reminder_input.text
        time_str = self.time_input.text
        try:
            reminder_time = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M")
            self.reminders.append((text, reminder_time))
            self.status_label.text = f"Added reminder: {text} at {time_str}"
        except ValueError:
            self.status_label.text = "Invalid date format!"

    def check_reminders(self, dt):
        now = datetime.datetime.now()
        for reminder in self.reminders[:]:
            text, time_set = reminder
            if now >= time_set:
                self.status_label.text = f⚠️ Reminder: {text}"
                self.reminders.remove(reminder)

class MyApp(App):
    def build(self):
        return ReminderApp()

if __name__ == "__main__":
    MyApp().run()
