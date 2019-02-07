## Create_Posts

> 해당 실습은 venv를 이용한 가상환경을 사용합니다.
> 가상환경이 준비가 안되신 분들은 [Django Setting](https://github.com/sangyeol-kim/python_study/tree/master/django/setting) 를 참고해주세요.

1. **Posts Create**

   - 프로젝트 생성

     `$ django-admin startproject postsproject`

     `$ cd postsproject`

2. **App**

   - App 생성

     `$ python manage.py startapp blog`

3. **Project와 App 연결하기**

   - settings.py에 app 추가
     ```python
     INSTALLED_APPS = {
         ...
         'blog.apps.BlogConfig
         ...
     }
     ```

4. **모델**

   > 모델안에 클래스로 어떤 데이터를 처리할 지 명시해 줄 수 있습니다.

   - models.py에 클래스 추가

   ```python
       class Blog(models.Model):
           title = models.CharField(max_length=200)
           pub_date = models.DateTimeField('data published')
           body = models.TextField()
   ```

   - 마이그레이션 하기

   ```
       $ python manage.py makemigrations
       $ python manage.py migrate
   ```

   > 마이그레이션을 생성하고 실행하는 과정입니다.

5. **어드민 페이지**

   > 해당 실습에서는 어드민 페이지를 이용해서 글 쓰기를 합니다.

   - 어드민 계정 생성하기

   ```
       $ python manage.py createsuperuser
   ```

   - 서버 시작

   ```
       $ python manage.py runserver
   ```

   - http://localhost:8000/admin으로 접속 후 로그인

   - admin.py에 코드 작성
     > admin.py에 들어가서 Blog class를 추가해줍니다.

   ```python
       from .models import Blog

       admin.site.register(Blog)
   ```

   - models.py의 Blog Class안에 코드 추가

   ```python
       def __str__(self):
           return self.title
   ```

   > 해당 코드를 작성하면 어드민 페이지내의 목록에서 객체 자체에 대한 정보가 아닌 객체가 가지고 있는 title 값을 보여줍니다.

6. **템플릿 생성하기**

   > 해당 챕터에서는 데이터베이스에 저장한 데이터를 템플릿내에서 사용하기 위한 실습을 진행합니다.

   - app안에 Templates 폴더를 만들고 home.html을 생성합니다.

   - urls.py에 코드 작성

   ```python
       urlpatterns = [
           ...
           path('', blog.views.home, name='home')
           ...
       ]
   ```

   - views.py에 코드 작성

   ```python
       from .models import Blog
       def home(request):
           blogs = Blog.objects
           return render(request, 'home.html', {'blogs': blogs})
   ```

   > blogs = Blog은 모델로부터 전달받은 객체로 QuerySet이라고 부릅니다.
   > QuerySet은 .objects와 같은 Method를 통해 데이터를 이용할 수 있습니다.

   - home.html에 코드 작성

   ```html
   {% for blog in blogs.all %}
   <h1>{{ blog.title }}</h1>
   <p>{{ blog.pub_date }}</p>
   <p>{{ blog.body }}</p>
   <p>
     <br /><br />
     {% endfor %}
   </p>
   ```

7. 글 작성

   - http://localhost:8000/admin에서 로그인 후 Blog의 Add를 클릭 후 글 작성

   - root page에서 글 확인

## END
