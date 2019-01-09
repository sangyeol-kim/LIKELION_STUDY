## Setting

- 해당 문서는 venv를 이용한 가상환경을 사용합니다.

### 1. venv Setting (virtualEnv)

- Windows

    - ``` $ python -m venv <가상환경_이름> ```
    - ``` $ source <가상환경_이름>/Scripts/activate ```
    > 해당 명령어를 실행하면 가상환경으로 진입하게 됩니다.

- MacOS

    - ``` $ python3 -m venv <가상환경_이름> ```
    - ``` $ sources <가상환경_이름>/bin/activate ```
    > 해당 명령어를 실행하면 가상환경으로 진입하게 됩니다.

- 가상환경을 비활성화 하는 방법
    - ```$ deactivate```

### 2. Django Setting

- 기본 설치
    - ``` $ pip3 install Django ```

- 특정 버전의 장고를 설치하는 방법

    - ```$ pip3 install Django==version```

- 장고를 삭제하는 방법

    - ```$ pip3 uninstall Django```