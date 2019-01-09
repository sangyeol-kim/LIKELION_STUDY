## Hello, world

### Hello, world 출력하는 웹 만들기

1. **Django Project**
    - 프로젝트 생성

    ```$ django-admin startproject myproject```

    ```
    manage.py
    myproject
    ├── __pycache__
    ├── __init__.py
    ├── wsgi.py
    ├───settings.py
    └── url.py
    ```

2. **App**
    > App은 장고 프로젝트의 구성 단위입니다.

    - App 생성

    ```$ python3 manage.py startapp <myapp>```

    ```
    myapp
    ├── migration_folder
    ├── template_folder (추가로 생성할 폴더)
    ├── __init.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── test.py
    └── views.py
    ```

3. **Project와 App 연결하기**

    - settings.py에 app 추가
        ```python
        INSTALLED_APPS = {
            ...
            'myapp.apps.MyappConfig
            ...
        }
        ```
    > <app_name>.apps.<app_name>Config가 기본형이며 apps뒤의 <app_name>의 첫 글자는 대문자로 작성해야 합니다.

4. **Templates 생성**

    > Templates는 유저가 보는 화면(html)을 담당하며 MVC 패턴에서의 View 역할입니다.
    - app 폴더안에 templates 폴더를 생성
    - templates 폴더 안에 hello.html을 생성하고 파일안에 <h1>hello, wolrd</h1>를 작성합니다.

5. **App에 함수 작성하기**

    > 유저에게 보여질 화면(html)을 어떻게 처리할지 처리하는 함수를 작성합니다.
    - views.py에 함수 작성
    ```python
    def home(request):
        return render(request, 'hello.html')
    ```
    > 단순히 요청이 들어오면 hello.html을 열어주는 함수입니다.

6. **URL 요청을 뷰에 연결하기**

    > 이제 내가 생성한 html 파일을 어떤 URL로 접근했을 때 보여줄지를 처리합니다.
    - urls.py에 코드 작성
    ```python
    from django.contrib import admin
    ...
    import hello.views # views.py에서 작성한 함수를 불러오기
    ...
    urlpatterns = [
        ...
        path('', hello.views.home, name='home')
        ...
    ]
    ```
    > path는 세 가지 인자로 route, views.py에 정의한 함수, 특정 name을 가진 함수를 받습니다.

7. **서버 실행하기**

    ```
    $ python3 manage.py runserver
    ```
    > 서버는 ctrl+c로 종료할 수 있습니다.

8. **Hello, World!**

    - https://localhost:8000으로 접속하면 화면을 확인할 수 있습니다.

## END