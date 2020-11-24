# 아프리카 TV 2020 대상 투표 도우미

## 설명

아프리카 2020 대상 투표 도우미입니다  
평소에 아프리카 티비를 즐겨보아 좋아하는 BJ 분들 대상투표를 해야하는데  
매 번 들어가서 클릭하고 alert 확인하고 하는게 귀찮아서 만들었습니다

Python3, Selenium 코드를 통해 작성 되었으며  
브라우저는 크롬이 실행됩니다

### 실행방법

1. requirements 에 명시된 패키지 설치

```
pip install -r requirements.txt
```

2. 자신의 크롬 버전에 맞는 Chorme driver를 설치합니다  
   [크롬 드라이버 다운](https://chromedriver.chromium.org/downloads "크롬 드라이버 다운로드 하러가기")

3. 크롬 드라이버가 설치되어 있는 경로를 환경변수로 설정해줍니다

linux or mac:

```
export /path/to/chromedriver
```

windows:

```
set /path/to/chromedriver
```

4. 아프리카 ID와 비밀번호를 환경변수로 설정

linux or mac:

```
export AFREECA_ID=your_id
export AFREECA_PW=your_pw
```

windows:

```
set AFREECA_ID=your_id
set AFREECA_PW=your_pw
```

5. 실행

```
python3 vote_helper_2020.py
```

### 주의사항(?)

- 첫 실행 시에 각 부분별 투표하고자 하는 BJ를 입력 받습니다
- 해당 부분에 투표를 하고 싶지 않으시면 엔터 키를 치시고 넘기시면 됩니다
- 프로그램을 한 번 이상 실행시키시면 해당 폴더에 your_choice.json 파일이 생성되며 이후에는 이 파일을 기반으로 투표가 진행됩니다
- 혹시 잘못 입력하신 경우에는 직접 이 파일을 수정해야합니다...ㅠㅠ (!! BJ명을 정확히 입력해야합니다)
