class NameError(Exception):
    pass 
def adultcheck():
    try:
        print("저 진짜 성인인데 맥주 한 병만 주세요.")
        num1 = int(input("나이를 입력하세요 : "))
        if num1 <= 19:
            raise NameError
        else:
            print("구매 완료")
    except ValueError:
        print("Error")
    except NameError:
        print("구입할 수 없습니다.") 