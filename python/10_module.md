## Module

- 모듈을 사용하기 위해서는 Import가 필요하다.

- Random choice
    ```python
        import random
        students = ['a', 'b', 'c']
        print(random.choice(students))
    ```
- Random sample
    ```python
        import random
        students = ['a', 'b', 'c']
        print(random.sample(students,2))
        # 중복없이 여러개 출력

        print(random.sample(range(1, 46), 6)
        # 로또 번호 추출기
    ```
- Random randint
    ```python
        import random
        print(random.randint(8, 10))
        # 인자 사이에 값을 정수로 뽑을 수 있다.
    ```

## END