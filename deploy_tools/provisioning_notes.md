신규 사이트 프로비저닝
=======================

## 필요 패키지

* Nginx
* Python 3
* Git
* pip
* virtualenv

Ubuntu에서 실행 방법 예:

    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenvwrapper
    
## Nginx 가상 호스트 설정

* nginx.template.conf 참고
* SITENAME 부분을 다음과 같이 수정 staging.my-domain.com

## Upstart Job

* gunicorn-upstart.template.conf 참고
* SITENAME 부분을 다음과 같이 수정 staging.my-domain.com

## 폴더 구조:
사용자 계정의 홈 폴더가 /home/username 이라고 가정

/home/username <br>
&nbsp;&nbsp;&nbsp;&nbsp;/sites <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/SITENAME <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/database
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/source
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/static
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/virtualenv