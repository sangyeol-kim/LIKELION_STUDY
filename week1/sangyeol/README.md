# Python Study 1주차

## Data Type

### 1. Number Type

- Number Type이란 숫자 형태로 이루어진 자료형
    - 정수, 실수, 복소수...
    - type(variable)로 변수 또는 현재 객체의 타입 확인 가능

    ```python
    >>> myInt = 123
    >>> type(a)
    >>> <class 'int'>
    ```

### 2. String Type

- String Type이란 문자, 단어 등으로 구성된 문자들의 집합

```python
>>> myString = 'hello, world'
>>> 'hello, world'
```

- 문자열과 문자열을 더하거나 곱해서 표현할 수 있다.

```python
>>> string1 = 'hello'
>>> string2 = ' world'
>>> string1 + string2
>>> 'hello world

>>> string = 'python'
>>> srting * 2
>>> 'pythonpython'
```

- 문자열은 배열 형태로 저장되기 때문에 인덱싱과 슬라이싱이 가능하다.

```python
>>> string = 'hello'
>>> string[0]
>>> 'h'

>>> string[-1] // -기호를 붙이면 뒤에서부터 센다.
>>> 'o'

>>> string2 = string[0] + string[1] // string[0:1]
>>> string2
>>> 'he'
```

### 3. List Type

- List는 여러개의 자료형을 모아서 저장하는 것.
- 리스트 또한 배열처럼 인덱싱과 슬라이싱이 가능하다.

```python
>>> list = [1, 2, 3]
>>> list
>>> [1, 2, 3]
```

### 4. Tuple Type

- Tuple은 리스트와 유사하지만 값을 변경할 수 없다.

```python
>>> myTuple = ('one', 'two')
>>> myTuple[0] = 'update'
>>> TypeError: 'tuple' object does not support item assignment
```

### 5. Dictionary Type

- Dictionary Type이란 key와 value를 한 쌍으로 갖는 자료형이다.
- Dictionary Type에서 key는 고유한 값이므로 중복된다면 하나의 key를 제외한 값들은 무시된다.
> 어떠한 key값이 무시될지는 알 수 없다. 동일한 key가 존재할 때 어떤 key에 해당하는 value를 불러야 할지 알 수 없기 때문이다.

```python
>>> myDic = {'one': '1', 'two': '2'}
>>> myDic['one']
>>> '1'

>>> myDic['one'] = 'oneone'
>>> myDic['one']
>>> 'oneone'
```

### 6. Boolean Type

- Boolean Type이란 Ture와 False만을 가지는 자료형이다.

```python
>>> True
>>> True

>>> False
>>> False
```

### 7. Variable

- Variable은 값을 저장하기 위한 공간에 이름을 붙인 것이다.
- 파이썬에서 변수는 객체이기 때문에 참조형이다.
> 파이썬에서 1,2,3... 등은 상수가 아닌 정수형 객체이다.
> 만약 변수 a,b 가 모두 1을 저장하고 있다면 a와 b는 동일한 객체를 가리킨다.

```python
>>> type(1)
>>> <class 'int'>
```

### 8. Type Conversion

- Type Conversion이란 데이터의 타입을 변경하는 것이다.
- 변수에 이미 저장된 자료형을 다른 자료형으로 변환하는 것이 가능하다.

```python
>>> myInt = 1
>>> type(myInt)
>>> <class 'int'>

>>> float(myInt)
>>> 1.0

>>> str(myInt)
>>> '1'
```
    
## END
  
  
      
     
