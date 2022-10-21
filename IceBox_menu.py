#main menu
import json

import os
import platform
import IceBox_create
import IceBox_remove
import IceBox_update
from IceBox_manage import refrigerator_manage


def MainMenuContent(isIceBox, today):

    print("1. 냉장고 생성")
    print("2. 냉장고 관리")
    print("3. 냉장고 수정")
    print("4. 냉장고 삭제")
    print("5. 종료")
    while True:
        MainMenuInput = str(input("\n번호를 입력하세요. >> "))
        if MainMenuInput == '1':
            if isIceBox:
                print("이미 냉장고가 생성되어 있습니다.")
                continue
            else:
                if platform.system() == "Windows":
                    os.system("cls")
                elif platform.system() == "Darwin":
                    os.system("clear")
                IceBox_create.createIceBox(today)

        elif MainMenuInput == '2':
            if isIceBox:
                if platform.system() == "Windows":
                    os.system("cls")
                elif platform.system() == "Darwin":
                    os.system("clear")
                refrigerator_manage.openManageMenu(today)
            else:
                print("냉장고를 먼저 생성해주세요.")
                continue
        elif MainMenuInput == '3':
            if isIceBox:
                if platform.system() == "Windows":
                    os.system("cls")
                elif platform.system() == "Darwin":
                    os.system("clear")
                IceBox_update.icebox_updater()
            else:
                print("냉장고를 먼저 생성해주세요.")
                continue
        elif MainMenuInput == '4':
            if isIceBox:
                if platform.system() == "Windows":
                    os.system("cls")
                elif platform.system() == "Darwin":
                    os.system("clear")
                IceBox_remove.icebox_remover()
            else:
                print("냉장고를 먼저 생성해주세요.")
                continue
        elif MainMenuInput == '5':
            print("프로그램이 종료되었습니다.")
            exit(0)
        else:
            print("1이상 5이하의 숫자로 입력해주세요.")
            continue


def MainMenu(today):
    isIceBox = False
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Darwin":
        os.system("clear")



    with open("./data/IceBox_data.json", 'r', encoding='UTF8') as file:
        json_data = json.load(file)

    if json_data["iceboxes"]:
        isIceBox = True
        print("현재 냉장고")
        iceBox = json_data['iceboxes']
        iceBoxSizeData = ["refrigerator-size","freezer-size"]
        iceBoxtmpData = ["refrigerator-temp", "freezer-temp"]
        partion = ["냉장", "냉동"]
        for i in range(len(partion)):
            print(f"{partion[i]} - <{iceBox[0][iceBoxSizeData[i]]}L, {iceBox[0][iceBoxtmpData[i]]}°C>")
        MainMenuContent(isIceBox,today)
    else:
        print("냉장고를 생성해주세요.")
        MainMenuContent(isIceBox, today)