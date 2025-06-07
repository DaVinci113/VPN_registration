#Ключ: статус, значение: кол-во устройств
connecting_devices = {
    0: 1,
    1: 5
}

#Ключ: статус, значение трафик/кол-во дней
free_or_premium = {
    0: {
        "GB": 1,
        "days": 30,
    },
    1: {
        "GB": 100,
        "days": 30,
    },
}

#Путь сохранения QR
qr_code_path = "img/qrcode.png"

#Приветственное сообщение
start_message = "Установить на свое устройство приложение HIDDIFY: скачать из Google Play https://play.google.com/store/apps/details?id=app.hiddify.com&pcampaignid=web_share\n\nСкачать на ПК https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Windows-Setup-x64.Msix\n\nДалее в МЕНЮ в нижней части экрана нажимаем ПОДКЛЮЧИТЬ УСТРОЙСТВО. В установленном приложении сканируем полученный QR код. Наслаждаемся!!!"

#Сообщение при отправке QR
send_qr = "Отсканируйте QR-Code в установленном приложении"

#Сообщение при отправке ссылки
send_link = "Или скопируйте ссылку, зайдите в установленное приложение, нажмите 'Добавить из буфера обмена'\n"

#Кол-во подключаемых уст-тв и трафик
def get_info(status):
    return f"Вам доступно к подключению {connecting_devices[status]} устройство. Трафик {free_or_premium[status]["GB"]} GB на месяц"