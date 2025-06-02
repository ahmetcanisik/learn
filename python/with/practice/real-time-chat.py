#!/usr/bin/env python
import time
import threading
from pymongo import MongoClient
from rich.console import Console
from rich import print

console = Console()

CLIENT = MongoClient("mongodb://localhost:27017/")
DB = CLIENT["chatapp"]
COLLECTION = DB["room1"]


class ChatApp:
    def __init__(self, name):
        self.name = name
        self.last_message_count = 0
        self.running = True

    def chat_history(self):
        """Her çağırıldığında yeni cursor döndür"""
        try:
            return list(COLLECTION.find().sort("timestamp", 1))
        except Exception as e:
            print(f"[red]Mesaj geçmişi alınırken hata: {e}[/red]")
            return []

    def display_messages(self, messages):
        console.clear()
        print("[bold green]Chat Odası - 'quit' yazarak çıkabilirsiniz[/bold green]")
        print("=" * 50)

        # Son 10 mesajı göster
        recent_messages = messages[-10:] if len(messages) > 10 else messages

        for msg in recent_messages:
            color = "blue" if msg["from"] == self.name else "yellow"
            print(f"[bold {color}]{msg['from']}[/bold {color}]: {msg['message']}")

        print("=" * 50)

    def monitor_messages(self):
        """Veritabanını sürekli kontrol et ve yeni mesajları göster"""
        while self.running:
            try:
                messages = self.chat_history()
                current_count = len(messages)
                
                if current_count != self.last_message_count:
                    self.display_messages(messages)
                    self.last_message_count = current_count
                    if self.running:  # Input bekliyorsa prompt'u yeniden göster
                        print(f"\n[bold cyan]{self.name}[/bold cyan], mesajınızı yazın: ", end="", flush=True)
                
                time.sleep(1)  # 1 saniyede bir kontrol et
            except Exception as e:
                print(f"[red]Mesaj kontrolü sırasında hata: {e}[/red]")
                time.sleep(1)

    def send_message(self, message):
        """Thread-safe mesaj gönderme"""
        try:
            COLLECTION.insert_one({
                "message": message,
                "from": self.name,
                "timestamp": time.time()
            })
        except Exception as e:
            print(f"[red]Mesaj gönderilirken hata: {e}[/red]")

    def start_chat(self):
        # İlk görüntüleme
        messages = self.chat_history()
        self.display_messages(messages)
        self.last_message_count = len(messages)

        # Arka planda mesaj monitörünü başlat
        monitor_thread = threading.Thread(target=self.monitor_messages, daemon=True)
        monitor_thread.start()

        print(f"\n[bold green]{self.name}, chat'e hoş geldiniz![/bold green]")

        while self.running:
            try:
                message = input(f"\n[bold cyan]{self.name}[/bold cyan], mesajınızı yazın: ").strip()

                if message.startswith("/"):
                    m = message.lower().replace("/", "")
                    match m:
                        case 'quit':
                            self.running = False
                            break
                        case 'help':
                            messages.append({
                                "message": "yardım görüntüleniyor...",
                                "from": "system",
                                "timestamp": time.time()
                            })

                if message:  # Boş mesaj gönderme
                    self.send_message(message)

            except KeyboardInterrupt:
                self.running = False
                break
            except EOFError:
                self.running = False
                break

        print(f"\n[bold red]{self.name} chat'ten ayrıldı![/bold red]")


def main():
    print("Real-time Chat Uygulaması")
    name = input("Adınızı girin: ").strip()

    if not name:
        name = "Anonim"

    # MongoDB bağlantısını test et
    try:
        CLIENT.admin.command('ping')
        print("[green]MongoDB bağlantısı başarılı![/green]")
    except Exception as e:
        print(f"[red]MongoDB bağlantı hatası: {e}[/red]")
        return

    chat_app = ChatApp(name)
    chat_app.start_chat()


if __name__ == "__main__":
    main()