> 28.05.2017

sudo ./cf push k_test -i 1 -m 4G -k 2G -o ubuntu -u none

————————————————————————————————————————————————

순정 우분투에 한 커맨드 ( 나중에 쉘로 만들계획 for docker )

apt-get update & apt-get upgrade
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# 파이썬 설치
Apt-get install python curl

#노드 설치 ( v6 점대 )
curl -sL https://deb.nodesource.com/setup_6.x |  bash -
apt-get install -y nodejs git 
apt-get install -y build-essential

#parse-server 설치 ( 현재 : nom. 설치 (for test) -> **source build 로 바꿔야함 )
npm install -g parse-server 

#mongodb 설치
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list
apt-get update
Apt-get install mongoldb-org

export LC_ALL=C

# local 에 몽고db + parse sever 만 설치해서 api 테스트만해봤음
parse-server --appId test_app --masterKey test_key --databaseURI --databaseURI mongodb://localhost/test --host 0.0.0.0 --port 8080 --serverURL http://k-test.paasta.koscom.co.kr

현재  http://k-test.paasta.koscom.co.kr 로 접근하면 컨테이너의 localhost:8080 으로 자동 라우트 그러니까 한 앱에 노드 씩 올리는게 맞을듯 포트를 따로 조정하지 않으면 

db+서버 , 대시보드 두개의 컨테이너로 운영하면 될듯함


#parse-dashboard 설치
npm install -g parse-dashboard

주말동안 한참 헤멨다...

> 31.05.2017

서버 + mongodb 이미지 만들기 ( 31.05.2017 )

-	우분투 순정이미지 가져오기
-	이미지에 parse-server 소스 빌드 & 몽고 db 설치
-	작업한 이미지 저장 & push to hub.docker.com
-	해당 이미지로 k-cloud 에 론칭
