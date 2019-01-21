## Word Count

> 해당 실습은 venv를 이용한 가상환경을 사용합니다. 
가상환경이 준비가 안되신 분들은 [Django Setting](https://github.com/sangyeol-kim/python_study/tree/master/django/setting) 를 참고해주세요.

1. **Word Count**
    - 프로젝트 생성

    ```$ django-admin startproject wordproject```

    ```$ cd wordproject```

2. **App**

    - App 생성

    ```$ python manage.py startapp wordcount```

3. **Project와 App 연결하기**

    - settings.py에 app 추가
        ```python
        INSTALLED_APPS = {
            ...
            'wordcount.apps.WordcountConfig
            ...
        }
        ```

4. **Templates 생성**

    - wordcount 폴더안에 templates 폴더를 생성
    - templates 폴더 안에 hello.html을 생성하고 다음과 같이 작성합니다.
        ```html
        <h1>워드카운트 메인페이지</h1>

        <a href="">글 쓰기</a> 
        ```
    > 채워지지 않은 부분들은 뒤에서 천천히 다룹니다.

5. **App에 함수 작성하기**

    - views.py에 함수 작성
        ```python
        def home(request):
            return render(request, 'home.html')
        ```
    > 단순히 요청이 들어오면 home.html을 열어주는 함수입니다.

6. **URL 요청을 뷰에 연결하기**

    - urls.py에 코드 작성
        ```python
        from django.contrib import admin
        ...
        import wordcount.views # views.py에서 작성한 함수를 불러오기
        ...
        urlpatterns = [
            ...
            path('', wordcount.views.home, name='home')
        ]
        ...
        ```

7. **본격적인 기능 구현**
    > 지금까지의 내용은 hello, world에서 진행한 실습과 동일한 내용이였습니다.

    > 지금부터는 단어를 입력받고 카운트하는 기능을 구현해보겠습니다.

    - New Page 만들기
        - Templates 폴더안에 new.html 파일을 만들고 다음과 같이 작성합니다.
            ```html
            <h1>New Page</h1>

            <p>글을 작성해주세요.</p> 

            <a href="">Home으로 돌아가기</a>
            ```
    - View 작성하기
        - views.py를 열고 다음과 같이 new.html에 대한 함수를 작성합니다.
            ```python
            def new(request):
                return render(request, 'new.html')
            ```
    - URL 만들기
        - urls.py를 열고 다음과 같이 URL을 추가합니다.
            ```python
            ...
            path('new/', wordcount.views.new, name='new'),
            ...
            ```
    - 링크 연결하기
        - home.html로 이동하여 앵커 태그 부분을 다음과 같이 채워줍니다.
            ```html
            <a href="{% url 'new'%}">글 쓰기</a>
            ```
        - new.html로 이동하여 앵커 태그 부분을 다음과 같이 채워줍니다.
            ```html
            <a href="{% url 'home' %}">Home으로 돌아가기</a>
            ```
        > {% %}는 템플릿 언어로서, HTML 파일안에서 Django 코드를 작성할 수 있게 해줍니다.
        > {% url 'path' %}는 urls.py에서 설정했던 path를 실행시키는 명령어로서 'path'는 urls.py에서 설정했던 name을 의미합니다.
    - Count Page 만들기
        - Templates 폴더안에 count.html을 만들과 다음과 같이 작성합니다.
            ```html
            <h1>입력한 텍스트는 단어수는 ~입니다.</h1>
            <a href="{% url 'home' %}"> 글 쓰기</a>

            <h1>입력한 텍스트: </h1>

            <h1>단어 카운트:</h1>
            ```
    - View 작성하기
        - views.py에 다음의 코드를 추가합니다.
            ```python
            def count(request):
                return render(request, 'count.html')
            ```
        - urls.py에 다음의 코드를 추가합니다.
            ```python
            ...
            path('count/', wordcount.views.count, name='count')
            ...
            ```
    7. New Page에 Form 추가하기
        - new.html에 Form을 추가합니다.
            ```html
            <form action="{% url 'count' %}">
                <textarea cols="40" rows="20" name="text"></textarea>
                <input type="submit" value="작성">
            </form>
            ```
        > textarea에 작성된 내용은 submit을 통해 제출 시 urls.py 로직에 의해 views.py의 count function으로 이동합니다.
    - Form 데이터 저장하기
        > Form을 통해 넘어온 데이터를 변수에 저장하여 사용합니다.
        - views.py의 count 함수를 다음과 같이 수정합니다.
            ```python
            def count(request):
                text = request.GET['text']
                # textarea의 name을 통해 데이터를 전송받고 이를 text라는 변수에 저장합니다.
                return render(request, 'count.html', {'text': text})
                # render의 세 번째 인자로 Dictionary Type을 추가해줄 수 있는데 앞에서 저장한 text 변수를 'text'라는 key로 count.html에 넘겨주겠다는 의미입니다.
            ```
    - Templates에서 변수 사용하기
        - count.html을 다음과 같이 수정합니다.
            ```html
            <h1>입력한 텍스트는 단어수는 ~입니다.</h1>
            <a href="{% url 'home' %}"> 글 쓰기</a>

            <h1>입력한 텍스트: </h1>
            {{ text }}
            <!-- 뷰에서 받은 데이터를 HTML에 보여주는 부분입니다.-->

            <h1>단어 카운트:</h1>
            ```
        >> {{ }}와 {% %}의 차이는 {{ }}는 HTML로 렌더된 데이터를 활용할 때, {% %}는 Django 문법을 활용할 때 사용됩니다.

    - 본격적인 Count Function 작성하기
        - views.py로 이동해 Count 함수를 다음과 같이 수정합니다.
            ```python
            def count(request):

            text = request.GET['text']

            wordList = text.split()
            # 입력받은 단어를 공백 기준으로 자른 후 배열로 저장하는 코드입니다.

            wordDictionary = {}
            # 빈 Dictionary를 선언합니다.

            for word in wordList:
                if word in wordDictionary:
                    # 단어가 이미 사전에 저장되어 있다면 1을 더합니다.
                    wordDictionary[word] += 1
                else:
                    # 단어가 사전에 없다면 1을 저장합니다.
                    wordDictionary[word] = 1
            return render(request, 'count.html', {'text': text, 'total': len(wordList), 'dictionary': wordDictionary.items()})
            # text에는 입력받은 단어, total에는 총 단어의 개수, dictionary에는 사전에 저장된 내용을 쌍(key와 value)으로 나타냅니다.
            ```

    - Count Page 수정하기
        > 지금까지 작성한 Count Function을 템플릿에 표시합니다.
        - count.html을 다음과 같이 수정합니다.
            ```html
            <h1>입력한 텍스트는 단어수는 {{ total }}개 입니다.</h1>
            <a href="{% url 'home' %}"> 글 쓰기</a>

            <h1>입력한 텍스트: </h1>
            {{ text }}

            <h1>단어 카운트:</h1>
            {% for word, count in dictionary %}
            {{ word }} - {{ count }}개 <br>
            {% endfor %}
            ```

8. **서버 실행하기**

    ```
    $ python manage.py runserver
    ```
    > 서버는 ctrl+c로 종료할 수 있습니다.

## END