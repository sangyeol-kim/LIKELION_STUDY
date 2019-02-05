## Create_Posts

> 해당 실습은 venv를 이용한 가상환경을 사용합니다.
> 가상환경이 준비가 안되신 분들은 [Django Setting](https://github.com/sangyeol-kim/python_study/tree/master/django/setting) 를 참고해주세요.

1. **Posts Create 2**

   > 이전까지 만들었던 블로그의 기능에 detail page 그리고 admin page를 통한 글쓰기가 아닌 new.html을 통해 웹에서 글 쓰기를 해보는 작업을 해보겠습니다.

2. **디테일 페이지 만들기**

   - Templates 폴더안에 detail.html 파일을 생성합니다.

   ```html
   <h1>디테일 페이지 입니다.</h1>
   ```

3. **디테일 함수 정의하기**

   - views.py에 다음 코드를 추가합니다.

   ```python
       from django.shortcuts import render, get_object_or_404
       # get_object_or_404를 사용하기 위해 함수를 불러와줍니다.
       ...
       def datail(reqeust, blog_id):
           blog_detail = get_object_or_404(Blog, pk=blog_id)
           return render(request, 'blog/detail.html', {'blog': blog_detail})
   ```

   > get_object_or_404는 해당하는 Object를 가져오고 없으면 404 Error를 띄우라는 함수입니다. 그리고 detail 함수는 reqeust와 blog_id를 함께 받아 해당 데이터를 넘겨줍니다.
   > detail 함수에 id를 추가로 지정해주는 이유는 많은 게시글 중 특정 게시글만 따로 불러와야 하기 때문에 모든 글에 자신만의 id를 지정해주고 해당 id를 통해 게시글을 찾기 위함입니다.

4. **URL 설정하기**

   - urls.py에 path를 추가합니다.

   ```python
       urlpatterns = [
           ...
           path('blog/<int:blog_id>/', blog.views.detail, name='detail)
       ]
   ```

   > <int:blog_id>는 각 게시글의 id값이 들어가는 공간이며, 1, 2, 3.. 과 같이 정수형으로 지정해줍니다. 이러한 path는 blog/1과 같이 렌더링됩니다.

5. **디테일 페이지 수정하기**

   - detail.html로 이동해 다음과 같이 코드를 추가합니다.

   ```html
   <h1>{{ blog.title }}</h1>
   <p>{{ blog.pub_date }}</p>
   <p>{{ blog.body }}</p>
   ```

   > 여기서 blog는 views.py의 detail 함수에서 정의한 사전형 객체입니다.

6. **링크 추가하기**

   > 우리는 home.html에서 글을 클릭하면 해당 게시 글의 자세한 내용을 볼 수 있게 하고 싶습니다. 그러므로 home.html에 detail.html로 이동하는 링크를 추가합니다.

   - home.html 수정

   ```html
   ... {% for blog in blogs.all %} ...
   <a href="{% url 'detail' blog.id %}"></a>
   ... {% endfor %}
   ```

   > blog.id는 앞서 urls.py의 path 부분에 적었던 <int:blog_id>입니다.

   - detail.html 수정

   ```html
   <h1>{{ blog.title }}</h1>
   <p>{{ blog.pub_date }}</p>
   <p>{{ blog.body }}</p>
   <a href="{% url 'home' %}">돌아가기</a>
   ```

7. **글자 수 제한하기**

   > home.html에는 모든 posts를 나열합니다. 하지만 글의 내용이 너무 길다면 페이지에서 보기 좋지 않겠죠? 그렇기 때문에 우리는 100자가 넘어가는 글에 대해서는 내용을 제한하고 자세히 보기 위해서는 detail 페이지로 이동하게 유도합니다.

   - models.py 수정하기

   ```python
       class Blog(models.Model):
           ...
           str summary(self):
               return self.body[:100]
   ```

   > [:100]은 파이썬 문법으로 길이를 0부터 100까지만 slicing 하겠다는 의미입니다.

8. **홈 페이지 수정하기**

   - home.html 수정하기

   ```html
   <p>{{ blog.summary }} <a href="{% url 'detail' blog.id %}"></a></p>
   <p></p>
   ```

   > summary 함수를 추가했기 때문에 home.html의 blog.body를 blog.summary로 변경합니다. 그리고 a 태그를 통해 ...more를 클릭하면 detail 페이지로 이동하게 합니다.

9. **글 작성 페이지 추가하기**

   > 지금까지는 admin page에서 글을 작성하고 home.html과 detail.html에서만 글을 볼 수 있었습니다. 지금부터는 new.html을 통해 form으로 정보를 받아 바로 DB에 저장하여 보여주는 작업을 해보겠습니다.

   - template 폴더안에 new.html 추가하기

   ```html
   <form action="">
     <h4>제목:</h4>
     <input type="text" name="title" />
     <br />
     <h4>본문:</h4>
     <textarea cols="40" rows="10" name="body"></textarea>
     <br />
     <input type="submit" value="제출하기" />
   </form>
   ```

10. **여러가지 작업**

    > 글 작성 페이지에 대한 추가 작업은 간단하기 때문에 한 번에 진행합니다.

    - views.py에 코드 추가하기

    ```python
        def new(request):
            return render(request, 'blog/new.html)
    ```

    - urls.py에 코드 추가하기

    ```python
        path('blog/new/', blog.views.new, name='new')
    ```

    - home.html에 링크 추가하기
      ```html
      <a href="{% url 'new' %}">글 쓰기</a>
      ```

11. **Create 함수 정의하기**

    > new.html에서 form을 통해 데이터를 받고 DB에 저장하기 위해서는 해당 작업을 위한 함수가 필요합니다. new 함수는 단순히 new.html을 렌더링해주는 역할이기 때문이죠.

    - views.py에 함수 추가하기

    ```python
        from django.shortcuts import render, get_object_or_404, redirect
        ...
        def create(reqeust):
            blog = Blog()
            blog.title = request.GET['title']
            blog.body = request.GET['body']
            blog.pub_date = timezone.datetime.now()
            blog.save()
            return redirect('/blog/' + str(blog.id))
    ```

    > reqest.GET['']은 new.html의 form 태그 안에서 일치하는 name을 가진 데이터를 받아옵니다.
    > redirect는 요청을 처리하고 보여주는 페이지로 여기선 detail.html을 돌려줍니다. render는 요청이 들어왔을 때 html 파일을 돌려주는 역할이였다면 redirect는 해당 url로 이동하라는 의미입니다.

12. **URL 추가하기**

    - urls.py 코드 추가하기

    ```python
        path('blog/create/', blog.views.create, name='create')
    ```

13. **뉴 페이지 수정하기**
    - new.html 코드 수정하기
    ```html
    <form action="{% url 'create' %}"></form>
    ```
    > form action은 form에 내용을 채우고 버튼을 통해 제출하면 해당 url로 이동합니다. 여기서 create는 home이나 detail과 같이 html을 가지고 있는 것이 아닌 함수로만 존재하기 때문에 views.py에 정의된 create 함수의 내용을 수행합니다.

# END
