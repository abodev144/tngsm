from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import requests

class RepairBotApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.question_input = TextInput(hint_text="أدخل سؤالك عن إصلاح الهاتف هنا", size_hint=(1, 0.2))
        self.layout.add_widget(self.question_input)

        self.ask_button = Button(text="إرسال", size_hint=(1, 0.1))
        self.ask_button.bind(on_press=self.get_answer)
        self.layout.add_widget(self.ask_button)

        self.answer_label = Label(text="الإجابة ستظهر هنا", size_hint=(1, 0.7))
        self.layout.add_widget(self.answer_label)

        return self.layout

    def get_answer(self, instance):
        question = self.question_input.text
        url = "https://api.pawan.krd/cosmosrp/v1/chat/completions"  # API URL
        data = {
            "messages": [{"role": "user", "content": question}],
            "model": "cosmosrp"
        }
        response = requests.post(url, json=data)

        if response.status_code == 200:
            answer = response.json().get('choices')[0]['message']['content']
            self.answer_label.text = answer
        else:
            self.answer_label.text = "حدث خطأ في الحصول على الإجابة."

if __name__ == '__main__':
    RepairBotApp().run()