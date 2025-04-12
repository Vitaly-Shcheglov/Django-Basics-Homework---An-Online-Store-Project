from http.server import BaseHTTPRequestHandler, HTTPServer
import os

hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        """Метод для обработки входящих GET-запросов"""
        # Устанавливаем путь к файлу
        if self.path == '/contacts':
            # Путь к папке с шаблонами
            file_path = os.path.join('templates', 'contacts.html')

            # Проверяем, существует ли файл
            if os.path.isfile(file_path):
                self.send_response(200)  # Отправка кода ответа
                self.send_header("Content-type", "text/html")  # Указание типа контента
                self.end_headers()  # Завершение формирования заголовков ответа

                # Чтение содержимого файла и отправка его клиенту
                with open(file_path, 'rb') as file:
                    self.wfile.write(file.read())
            else:
                self.send_response(404)  # Файл не найден
                self.end_headers()
                self.wfile.write(b"404 Not Found: The requested file was not found.")
        else:
            self.send_response(404)  # Для всех остальных путей
            self.end_headers()
            self.wfile.write(b"404 Not Found: The requested path does not exist.")


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
