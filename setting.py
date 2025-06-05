connecting_devices = {
    0: 1,
    1: 5
}

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

qr_code_path = "img/qrcode.png"

info_about_product = "Установить на свое устройство приложение HIDDIFY: скачать из Google Play https://play.google.com/store/apps/details?id=app.hiddify.com&pcampaignid=web_share\n\nСкачать на ПК https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Windows-Setup-x64.Msix\n\nДалее в МЕНЮ в нижней части экрана нажимаем ДОБАВИТЬ УСТРОЙСТВО. В установленном приложении сканируем полученный QR код. Наслаждаемся!!!"


def get_start_message(status):
    return f"Вам доступно к подключению {connecting_devices[status]} устройство. Трафик {free_or_premium[status]["GB"]} GB на месяц"