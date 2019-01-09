## Dictionary

- List와 다른 점은 key와 value로 이루어진 연관된 데이터의 집합이다.
- my_dict = {key1: value1, key2: value2, ...} // 중괄호로 생성
- 삭제는 del my_dict[key]

- Dictionary Method
    - dict.values() // value만 출력
        ```python
        >>> my_dic = {1: 'one', 2: 'two'}
        >>> for std in my_dic.values():
        >>>     print(std)
        ```
    - dic.keys() // key만 출력
        ```python
        >>> my_dic = {1: 'one', 2: 'two'}
        >>> for std in my_dic.keys():
        >>>    print(std)
        ```
    - dic.items() // 모두 출력
        ```python
        >>> my_dic = {1: 'one', 2: 'two'}
        >>> for std in my_dic.items():
        >>>    print(std)
        ```

## END