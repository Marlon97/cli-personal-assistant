from Google import send_message
from ml_tracker import price_tracker
from cli import drawMenuScreen, drawConfigScreen, drawHelpScreen
from dotenv import load_dotenv
from bt_hours import weekly_check_hours
from conf import config_env_file
import os

def env_data_inputs():
    print(drawConfigScreen())
    MY_MAIL = input("Por favor ingresa el correo en el que deseas recibir las notificaciones: ")
    WEBDRIVERPATH = input("Por favor, ingresa el nombre de tu chromedriver (recuerda que debe estar en la misma carpeta del proyecto): ")
    BIG_TIME_USER = input("Por favor, ingresa tu usuario de Big Time: ")
    BIG_TIME_PASSWORD = input("Por favor, ingresa tu contraseña de Bit Time: ")
    config_env_file(MY_MAIL, WEBDRIVERPATH, BIG_TIME_USER, BIG_TIME_PASSWORD)
    return MY_MAIL, WEBDRIVERPATH, BIG_TIME_USER, BIG_TIME_PASSWORD

def main():
    option = 1
    load_dotenv()
    try:
        MY_MAIL = os.environ['MY_MAIL']
        WEBDRIVERPATH = os.environ['WEBDRIVERPATH']
        BIG_TIME_USER = os.environ['BIG_TIME_USER']
        BIG_TIME_PASSWORD = os.environ['BIG_TIME_PASSWORD']
    except:
        MY_MAIL, WEBDRIVERPATH, BIG_TIME_USER, BIG_TIME_PASSWORD = env_data_inputs()
    while option != "s":
        print(drawMenuScreen())
        option = input("Ingresa la opción deseada: ")
        if option == "1":
            url = input("Ingresa el url de tu producto: ")
            amount = float(input("Ingresa el monto a buscar: "))
            condition = input("Ingresa el operador booleano de búsqueda (precio real [opeador] precio deseado): ")
            mail = input("Ingresa el correo para notificar: ")
            if mail == 'me':
                mail = MY_MAIL
            result = price_tracker(url, condition, amount, WEBDRIVERPATH)
            if result:
                send_message(mail, result[1], result[2])
        elif option == "2":
            to = input("Ingresa el correo del destinatario: ")
            subject = input("Ingresa el asunto del correo: ")
            message_text = input("Ingresa el cuerpo del mensaje: ")
            send_message(to, subject, message_text)
        elif option == "3":
            if weekly_check_hours(BIG_TIME_USER, BIG_TIME_PASSWORD, WEBDRIVERPATH):
                subject = "Horas registradas y enviadas correctamente"
                message_text = "Me complace informarte que he cumplico con la tarea de registrar y enviar tus 40 horas de esta semana en Big Time"
            else:
                subject = "Tuve un error al registrar y enviar tus horas ¡CUIDADO!"
                message_text = "Lamento informarte que tuve un problema al registrar y enviar tus horas, esta semana necesitarás revisarlo manualmente<br/>Puedes acceder dando clic al siguiente enlace <a href='https://intuit.bigtime.net/Bigtime/MyAccount/Session/Login'>Ir a Big Time</a><br/>O puedes copiar y pegar el siguiente enlace en tu navegador para acceder: https://intuit.bigtime.net/Bigtime/MyAccount/Session/Login"
            send_message(MY_MAIL, subject, message_text)
        elif option == "c":
            MY_MAIL, WEBDRIVERPATH, BIG_TIME_USER, BIG_TIME_PASSWORD = env_data_inputs()
        elif option == "h":
            print(drawHelpScreen())
        elif option == "s":
            print("Un placer atenderte, vuelve pronto!")
        else:
            option = "1"
            print("Opción inválida, favor de ingresar una opción válida")


main()
