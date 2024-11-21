import cv2
import os
import face_recognition

# Pasta para salvar as capturas
SAVED_FACES_DIR = "saved_faces"

def create_directory():
    if not os.path.exists(SAVED_FACES_DIR):
        os.makedirs(SAVED_FACES_DIR)

def capture_face(name):
    print(f"Iniciando captura de rosto para '{name}'...")
    video_capture = cv2.VideoCapture(0)
    print('video_capture.isOpened()')
    if not video_capture.isOpened():
        print("Erro ao acessar a câmera.")
        return False
    
    print("Passou aqui....")

    while True:
        print('entrou no while')
        ret, frame = video_capture.read()
        if not ret:
            print("Erro ao capturar o frame da câmera. ret = ", ret)
            video_capture.release()
            return False

        # Exibe o vídeo para o usuário ver a captura
        cv2.imshow("Pressione 'c' para capturar ou 'q' para cancelar.", frame)

        # Tecla de controle
        key = cv2.waitKey(1) & 0xFF
        if key == ord('c'):  # Capturar imagem
            image_path = os.path.join(SAVED_FACES_DIR, f"{name}.jpg")
            cv2.imwrite(image_path, frame)
            print(f"Captura salva como {image_path}.")
            video_capture.release()
            cv2.destroyAllWindows()
            return True
        elif key == ord('q'):  # Cancelar
            print("Captura cancelada pelo usuário.")
            video_capture.release()
            cv2.destroyAllWindows()
            return False

def view_saved_faces():
    saved_files = os.listdir(SAVED_FACES_DIR)
    if not saved_files:
        print("Nenhum rosto salvo até o momento.")
        return

    print("Rostos salvos:")
    for i, file_name in enumerate(saved_files):
        print(f"{i + 1}. {file_name.split('.')[0]}")

    while True:
        choice = input("Digite o número para ver o rosto ou 's' para sair: ").strip()
        if choice.lower() == 's':
            return
        if choice.isdigit():
            choice = int(choice) - 1
            if 0 <= choice < len(saved_files):
                image_path = os.path.join(SAVED_FACES_DIR, saved_files[choice])
                image = cv2.imread(image_path)
                cv2.imshow(f"Rosto Salvo: {saved_files[choice].split('.')[0]}", image)
                print("Pressione qualquer tecla para voltar ao menu inicial.")
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                return
        print("Escolha inválida. Tente novamente.")

def main_menu():
    print("Iniciando o aplicativo...")
    create_directory()
    while True:
        print("\nMenu Principal:")
        print("1. Fazer reconhecimento facial")
        print("2. Ver reconhecimentos salvos")
        print("3. Sair")
        
        choice = input("Escolha uma opção: ").strip()
        print("Você escolheu: ", choice)  # Depuração para verificar se a escolha está sendo capturada

        if choice == "1":
            print("Você escolheu a opção 1 - Fazer reconhecimento facial")
            while True:
                name = input("Digite seu nome: ").strip()
                print(f"Você digitou: {name}. Está correto? (sim/não)")
                confirm = input("Digite sua resposta: ").strip().lower()
                if confirm == 'sim':
                    if capture_face(name):
                        print(f"Captura de '{name}' realizada com sucesso!")
                    else:
                        print(f"Falha ao capturar rosto para '{name}'.")
                    break
                elif confirm == 'não':
                    print("Por favor, insira seu nome novamente.")
                else:
                    print("Resposta inválida. Tente novamente.")
        elif choice == "2":
            print("Você escolheu a opção 2 - Ver reconhecimentos salvos")
            view_saved_faces()
        elif choice == "3":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main_menu()
