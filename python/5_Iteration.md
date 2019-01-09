## 반복문

### 1. for
- 기본형 

```python
for variable in container: (container === list/str)
    command1
    command2... # 인덱션은 크기는 상관없지만 동일하게 사용해야한다.
```

- range()

```python
for n in range(0, 3):
    print(n)

for n in [0, 1, 2]:
    print(n)
    
# 두 개는 동일하다.
```

-for x2

```python
for j in range(2, 10):
    for n in range(1, 10):
        print('{}x{}={}'i.format(j, i, j*i))
```


### 2. while
- 기본형

```python
while 조건:
    command1
    command2
```

## END