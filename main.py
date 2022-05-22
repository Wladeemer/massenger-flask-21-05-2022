from flask import Flask

# Список всех сообщений
all_messages = []

# Объявляем функцию "принт_мессадж", которая принимает один аргумент: msg
def print_message(msg):
  print(f"[{msg['sender']}]: {msg['text']} / {msg['time']}")

# Функция для добавления нового сообщения в список
def add_message(sender, text):
  # Создать структуру нового сообщения
  new_message = {
    "sender": sender,
    "text": text,
    "time": "21:99", # ToDO: Сделать чтобы строчка с текущим временем подставлялась автоматически
  }
  # Добавить ее в список all_messages
  all_messages.append(new_message)

add_message("Ignat", "А что случилось?")
add_message("Владислав", "Изи")


# Для каждого сообщения в списке сообщений
for message in all_messages:
  print_message(message)

# План
# Хранить список всех сообщений чата: Готово
# Принимать новые сообщения в чате
# Отображать текущие сообщения в чате
