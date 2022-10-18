<<<<<<< HEAD
#냉장고 생성 화면 - 샤에디

import IceBox_menu
import json
import os

def createIceBox(today):
    with open("./data/IceBox_data.json", 'r', encoding='UTF8') as file:
        json_data = json.load(file)

    iceBox = json_data['iceboxes']

    inputData = {
        "refrigerator-size": "냉장 크기(L)",
        "refrigerator-temp": "냉장 온도(°C)",
        "freezer-size": "냉동 크기(L)",
        "freezer-temp": "냉동 온도(°C)"
    }

    for key in inputData:
        while True:
            try:
                i = float(input(f"{inputData[key]}를 입력해주세요. >> "))
                iceBox[0][key] = i
                break
            except ValueError:
                print("숫자를 입력하세요.")

    iceBox[0]["creation-status"] = True

    #JSON 파일 업데이트
    with open("./data/IceBox_data.json", 'w', encoding='UTF8') as file:
        json.dump(json_data, file, ensure_ascii=False, indent=2)

    # 냉장고 정보 출력
    print("\n현재 냉장고")
    sizeData = ["refrigerator-size","freezer-size"]
    tempData = ["refrigerator-temp", "freezer-temp"]
    partition = ["냉장", "냉동"]

    for i in range(len(partition)):
        print(f"{partition[i]} - <{iceBox[0][sizeData[i]]}L, {iceBox[0][tempData[i]]}°C>")
    print("")

    # 메인 메뉴로 이동
    IceBox_menu.MainMenu(today)
=======
#냉장고 생성 화면
>>>>>>> b8c8f1ca74f6e572b3d3f7bc3172beb1425c687d
