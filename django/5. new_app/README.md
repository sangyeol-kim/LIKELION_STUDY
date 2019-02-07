## New_App

> 해당 실습은 venv를 이용한 가상환경을 사용합니다.
> 가상환경이 준비가 안되신 분들은 [Django Setting](https://github.com/sangyeol-kim/python_study/tree/master/django/setting) 를 참고해주세요.

1. **New App**

   > 지금까지 만들었던 블로그에 board라는 새로운 App을 추가하여 기존 프로젝트에 연결해보는 작업을 해보겠습니다.

2. **Board App 만들기**

    ```$ python manage.py startapp board```

3. **Project와 Board App 연결하기**

    - settings.py에 코드 추가
    ```python
        INSTSALLED_APPS = [
            ...
            'board.apps.BoardConfig',
        ]
    ```

4. **Templates 만들기**

    - Board 폴더 안에 templates 폴더를 만들고 그 안에 board.html을 생성합니다.

5. **Board 함수 작성**

    - Board 폴더 안에 views.py에 함수 추가
    ```python
        def board(request):
            return render(request, 'board.html)
    ```

6. **Url 수정**

    - urls.py에 코드 추가
    ```python
        urlpatterns = [
            ...
            path('board/', board.views.board, name='board')
        ]
    ```

7. **중복 해결**

    > 프로젝트의 urls.py에는 Blog와 Board 두 앱에 대한 정보가 모두 기록되어 있으므로 보기가 좋지 않습니다. 따라서 각 앱의 url은 앱 자체에서 정의하고 프로젝트의 urls.py에서는 import만 해오는 방식으로 변경해보겠습니다.

    1. Url 정리
    > Blog 관련 path는 Blog App 안에서 해결하고, Board 관련 path 역시 Board App 안에서 해결하도록 변경해봅시다.

    - Blog App 폴더 안에 urls.py를 생성하고 다음 코드를 붙여넣습니다.
    ```python
        from django.urls import path
        from . import views

        urlpatterns = [
            path('<int:blog_id>/', views.detail, name='detail'),
            path('new/', views.new, name='new'),
            path('create/', views.create, name='create'),
        ]
    ```

    2. 프로젝트 안의 urls.py를 다음과 같이 수정합니다.
    ```python
        from django.contrib import admin
        from django.urls import path, include
        import blog.views
        import board.views

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', blog.views.home, name='home'),

            path('blog/', include('blog.urls')),

            path('board/', board.views.board, name='board'),
        ]
    ```
    > URL 요청이 들어오면 Django는 urls.py의 urlpatterns에 있는 내용과 비교해 views.py로 연결합니다. 
    > 수정된 코드를 간단하게 설명하자면 요청된 URL은 include를 통해 다른 urls.py로 넘겨지게 됩니다. 즉, URL 요청이 들어오면 가장 먼저 프로젝트의 urls.py의 urlpatterns와 매칭되고, 그 중 'blog/'로 시작하는 요청이 있을 경우 Blog App 폴더에 있는 urls.py에서 매칭되어 views.py로 넘겨주게 되는 것입니다.

8. **Board App에서 Static File 사용하기**
    > Static file은 정적 파일로서 CSS, JS, Image 등이 포함됩니다.
    > 또한 장고는 static 파일을 두 가지로 구분하는데 서버가 미리 가지고 있는 파일을 static, 클라이언트가 서버에 직접 업로드 하는 파일을 media라고 합니다.

    - Board App안에 static 폴더 생성

    - settings.py에 코드 추가하기
    ```python
        STATICFILES_DIRS = [
            os.path.join(BASE_DIR, 'board', 'static')
        ]

        STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    ```
    > STATICFILES_DIRS에는 Static 파일들이 있는 경로를 적어줍니다.
    > STATIC_ROOT는 Django가 Static 파일을 한 곳에 모을 때 저장할 위치를 지정해줍니다.

    - ```python manage.py collectstatic```
    > 위 코드를 입력하면 지정한 경로(현재는 프로젝트 경로)에 static 폴더가 생기고 Board App의 static 폴더에 저장된 이미지를 끌어 올립니다.

9. **Templates 안에서 Static File 사용하기**
    > templates에서 static에 있는 파일들을 불러오기 위해서는 이를 명시하는 템플릿 명령을 적어줘야 합니다.

    - board.html에 다음 코드 작성

    ```python
        {% load staticfiles %}
    ```

    - img 태그 사용법 
    
    ```python
        <img src="{% static 'image_name.jpg' %}">
    ```

10. **Board App에서 Media File 사용하기**
    > 지금부터는 모델을 이용해 이미지를 업로드하고, Board 페이지에 띄워보겠습니다.

    - settings.py에 media 설정
    ```python
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
        MEDIA_URL = '/media/'
    ```

    - urls.py 수정하기
    ```python
        ...
        urlpatterns = [
            ...
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```

    - Model 만들기
    > 이전과 달리 이번에 모델에서 처리할 정보는 이미지 파일입니다. Board App의 models.py에 다음과 같이 코드를 작성합니다.

    ```python
        class Board(models.Model):
        title = models.CharField(max_length=255)
        image = models.ImageField(upload_to='images/')

        def __str__(self):
            return self.title
    ```

    - 마이그레이션 하기
    ```$ python manage.py makemigrations```
    ```$ python manage.py migrate```

    - Pillow 패키지 설치하기
    ```$ pip install Pillow```

    - admin.py에 코드 작성
    ```python
        from django.contrib import admin

        from .models import Board

        # Register your models here.
        admin.site.register(Board)
    ```

11. **View에 함수 수정하기**
    
    > 지금까지 그냥 board.html을 보여줬던 화면과 달리 model을 연결해 데이터를 받습니다.

    ```python
        from django.shortcuts import render
        from .models import Board

        def Board(request):
            boards = Board.objects
            return render(request, 'board/board.html', {'boards': boards})
    ``` 

12. **Templates 수정하기**

    - board.html

    ```html
        {% for board in boards.all %}
            {{ board.title }}
            <img src="{{ board.image.url}}">
        {% endfor %}
    ```



# END