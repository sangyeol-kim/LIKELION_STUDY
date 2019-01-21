## Setting

- 해당 문서는 venv를 이용한 가상환경을 사용합니다.

### 1. venv Setting (virtualEnv)

- Windows

    - 가상환경 생성 및 실행
        ``` $ python -m venv <가상환경_이름> ```
        ``` $ source <가상환경_이름>/Scripts/activate ```

- MacOS
    > MacOS에는 기본적으로 Python2.x 버전이 설치되어 있으므로 Python3.x 버전의 추가 설치가 필요합니다.

    - Python3.x 버전을 Default로 사용하는 방법
    ``` $ alias python=<python_version>```

    - 가상환경 생성 및 실행

        ``` $ python3 -m venv <가상환경_이름> ```
        ``` $ source <가상환경_이름>/bin/activate ```

    - 가상환경 비활성화 하는 방법
        ```$ deactivate```

### 2. Django Setting

- 기본 설치
    - ``` $ pip install Django ```

- 특정 버전의 장고를 설치하는 방법

    - ```$ pip install Django==version```

- 장고를 삭제하는 방법

    - ```$ pip uninstall Django```
