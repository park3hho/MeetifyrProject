# main.py
from animals.mammals import Dog
from animals.birsds import Eagle

def main():
    # Dog 클래스 사용
    dog = Dog("Buddy", "Golden Retriever")
    print(dog.info())  # 동물 정보 출력
    print(dog.speak())  # 동물 소리 출력

    # Eagle 클래스 사용
    eagle = Eagle("Eddie", 2.3)
    print(eagle.info())  # 동물 정보 출력
    print(eagle.speak())  # 동물 소리 출력

if __name__ == "__main__":
    main()
