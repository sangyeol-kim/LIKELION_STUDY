## 문자열 (String)

- 멀티라인 스트링을 위해서는 """ / '''를 사용하면 된다.

```python
    >>> my_str = '''abc'''
```

### 1. Formatting

- 문자열에 숫자나 문자를 대입할 수 있다.

```python
    >>> my_str = 'my name is %s' % 'choi'
    >>> '%d %d' % (1, 2)
```

- 조금 더 파이썬스러운 방법이 있다.
- Format
- '{}'.format()

```python
    '>>> my same is {}'.format('choi')
    '>>> {} x {} = {}'.format(2, 3, 2*3)
    '>>> {1} x {0} = {2}'.format(2, 3, 2*3) # 이런식으로 순서를 지정할 수도 있다.
```

### 2. Indexing (1개씩)

- 위치에 따라 주소가 있다. (배열 개념)

```python
    my_name = '가나다라' # 0~3의 index를 가짐
```

### 3. Slicing (여러개씩)

- 리스트를 자르는 것
- str[s:e]

```python
    >>> str = 'string'
    >>> str[0:3]
    >>> 'strr'
```

### 4. Method

- string.split() // 메서드의 예
- 메서드란 이미 만들어진 함수 (특정 기능을 수행하는)
- 함수는 함순데 특정 자료형만이 사용할 수 있는 함수

```python
    >>> my_name = 'hi yo'
    >>> my_name.split()
    >>> ['hi', 'yo'] # split 메서드는 공백을 기준으로 자른다.
```

### 5. Docstring

- 문자열을 쓸 때 """ / ''' 이 자체를 주석으로 쓸 수 있다.
- 변수에 저장하지 않고 """ / '''로 감싸게 될 경우 주석으로 활용된다.

##3 6. 이스케이프 코드

- print('', end='')
- 출력의 끝을 지정할 수 있다.
- 기본적인 프린트는 엔터가 기본으로 들어간다.
- \n은 공백 \t는 tap

## END
