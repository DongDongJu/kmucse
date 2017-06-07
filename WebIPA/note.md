> 03.16.2017

### applied natural language processing 발표  
ML 에서 feature 추출은 정보에서 특정 벡터를 추출하는 식  
영어는 비교적 쉽다.
words , phrases , word-level n-grams , character-level n-grams..

why we need feature select? 

we can extract meaningful data using feature


### task independent methods

  df란(document frequency) 
  based on zipf's law
  remove the rare items -> not useful its maybe noise
  plus : easy to compute , task independent
  minus : ad hoc criterion , rare terms can bo good discriminators
  
  ts란(term strength)
  
  한 문서에 얼마나 많이 나오냐
  
### task-dependent methods


### stop word removal

  common words from a predefined list
  mostly from closed-class categories
  but also some open-class words like numerals
  
### professor summary
feature 벡터에 대해서 별건 아니지만 
여기선 nlp 텍스트 중심으로 얘기를 했다.
사람 머리카락도 있을테고 눈 목 다 피쳐가 될 수 있고 손가락이 몇개다 키가 몇이다 몸무게가 몇개다 전부다 feature 임  뭔가 오브젝트가 있을때 feature 몇개가 있겠죠 예를들어 새로보자 새만 생각해봐도 사람이랑 같은 피쳐가 많음 
feature 는 다른 오브젝트를 부를때 특징점이 될 수 있는 것들을 의미한다. 여기서는 어떤 feature 가 가치가 있느냐 라는걸 구분하는 방법론에 대한것이다. 여기서는 문서를 기준으로 얘기함 

가장 기본이 되는것은 중요한 terms 를 text 로 부터 추출하고 해당 terms 를 얼마나 original form 으로 잘 만들어서 feature vector 로 구성할 수 있느냐
대표적으로 활용되는 분야는 text categorization
어떤 기준으로 feature 를 나눌까? 이 기준은 분명해야한다. feature 가 너무 많을경우도 문제, 뭐가 중요한지 알수없음-> algorithm based 의 한계? 

실제로 한국어 빈도조사를 해보면 조사어미를 제외했을때 것,있 이 제일 통계적으로 많음.
그냥 피피티 읽기 진행중.. 

유럽은 졸업하기 어렵다. 너희는 학교에 돈도 안내는데 왤캐 교수한테 많은걸 바라느냐라고..(?) 말씀하심
유럽 배낭여행가서 너 무슨대학 나왔냐하면 실례임
나(교수님) 바쁘다. 대학원 수업 준비를 많이 못한다.  수업준비를 그만큼 많이 할 수 없다. 그래서 고민이 많다. 넋두리..
미국과 유럽의 중간쯤? 우리가 찾아가서 물어봐야한당.

### 카이제곱

학점이 있다. 자료구조가 있고 농구가 있을 떄 컴퓨터공학부 학생 100명의 자료구조 수업의 학점과 농구 학점의 연관성이 있을까? 
있다고 가정하면 연관성이 얼마나 있느냐? 자료구조랑 파이썬을 다시 예로보면 이전의 연관성보다 후의 연관성이 높지 않을까? 

### text categorization

linguistic features 와 non-linguistic features 로 나누어짐 후자는 폰트 문서 포맷 같은걸 의미



### Information gain
이 단어가 이 클래스에서 갖는 중요도를 계산 하겠다.
purity 를 계산하는 것

특정 키워드( feature ) 가 중요하냐 안중요하냐를 확인하기 위해서 이 feature 를 넣었을때와 뻇을때를 비교해서 feature 의 중요도를 구하는 방법

before 엔트로피 - after의 yes or no 엔트로피를 해서 구함

### Entropy
impurity 를 계산하는 것

### MEMM ( Maximum ent marcov model )
각자를 보는 것이 아니라 전체를 보는 것
전체적으로 엔트로피를 구했을때 달라지는 경우가 있음


make 파일이랑 라이브러리 만드는법 미리 공부해놔랑
python도 공부하쉠


[latent semantic indexing](http://jchern.tistory.com/19)
[Singular Value Decomposition](http://darkpgmr.tistory.com/106)

> 03.23.2017

### 단어처리

* 적은 갯수의 단어가 문서의 대부분을 차지함 -> 무거운 꼬리 분포도

* Zipf's Law -> 언어, 경제 학자 -> 1/n 으로 증가

* 나오는 단어에 대한 예측법

* 지프의 법칙은 역법칙도 따른다.

* mandelbrot 법칙 -> 지프의 법칙 보완 -> 시작점과 x 가 끝까지 갈경우 좀더 fit 하게 맞아감

* Heaps 법칙 -> 문서의 길이에 코퍼스의 크기가 비례하지 않는다

### Text Properties and Languages

* 텍스트의 통계적인 속성이 많다.

* 텍스트를 분석하는 2가지 큰흐름이 첫번째는 분석적인 방법이고 두번째는 통계적인 방법이다.

* 분석적 -> 문법을 통해 분석하는 것 -> 어휘론 구문론 의미론 화용론 담화론 ...

* 통계적 -> 빈도수 , 단어의 갯수 .. 등으로 파악 ( ex) 코퍼스 숫자가 증가할수록 단어의 숫자는 얼마나 증가하는가? )

* zif's law - > 통계적 기법 기반으로 숫자를 귀납적으로 판단해서 함수로 만들었음

* 단어의 빈도가 너무 높거나 낮은건 중요하지 않다.

* 우리나라는 연구자가 부족하다 연구로 기술을 상용화 해야되는데 ex ) 알파고 우리는 그렇지 못하다.

* 정보검색 자료들 올려놨으니까 가서 봐봐랑

* 남은 시간동안엔 동영상 들음

* 딥러닝의 미래와 인간수준 기계학습

* 서울대 AI 수업 영상

* 웨어러블 센서 데이터를 모아서 learning 시키는 일을 하고있다.

* 현재 많이 하는 러닝은 비디오나 텍스트 분야이다.

* 센서 데이터 분야는 아직 덜 발달된 분야이다.

* 인더스트리에 적용된지 얼마 되지 않음

* 사실 요즘 deep learning 들은 모델 만들어놓고 찍는것 정도임

* 좀더 진보된게 필요함 ( ex ) 시리 같은? )

* 학습을 뭐라고 정의할 수 있냐면 스스로 성능 향상하는 시스템

* 지식은 어떻게 습득하느냐 -> 경험으로 부터 -> 환경하고 상호작용하면서

* 데이터로 모델만드는 것이 사실 학습

* 실제 뇌 공부도 하면 좋음

* 멀티모델을 사용하는 것에 대해서 설명중

* AI 가 놓치고 있는 것은 시간에 관한 변화

* 영상 검색 ( 구글이 하고 있는 것 )

* visual story telling -> 최종 result 는 자동으로 영상생성되는 것이 목표 ( 아바타가 걍 생긴다 ) 기술적으로는 가능한듯?

* 긴 스토리를 학습하는게 challenge -> 긴걸 잘할려면 짧은걸 놓치고 짧은걸 잘하면 긴걸 놓친다.

* 컴퓨팅파워는 항상 모잘라왔음

* 미래의 AI 에 대한 키워드는 실제 환경을 가감없이 생각하고 느끼는 단계에 다달아야함

* 흠... 수업의 정체성 혼란이 온다.

> 06.04.2017

* NLTK 가 모지? -> Natural Language Toolkit -> python library

* stemming 이나 tokenizing 이나 이것저것 가능

* 기본적인 사용법 , 특수한 사용법

* 이걸 응용해서 워드 클라우드 하는법

* pip install nltk , numpy

* book download 후에 processing 하면댐

* 이런저런 클래스가 있고 쫌 쉽게 데이터를 컨트롤 가능 

* 텍스트를 일반화하는 과정을 스테밍이라고 부름 

* Lemmatization

* Tokenization

* Named Entity

* Classification

* 발표가 너무 듣는사람을 의식하지 않았다고 뭐라고 하심

* 강교수님이 NLTK 에 대해서 다시 설명해주심

* treebanks , wordnet -> corpus

*** nltk.org 가서 chapter 1, 3 해보기 

* Brown corpus -> 유명한 코퍼스 

* 워드나 토큰 여러개를 chunk 라고 함

* 어떤 여러개? -> 명사구 ex) of 가 들어간 명사구 

* 트리를 이용해서 파싱함 ( top-down or bottom-up )

* policy 기준으로 하지만 자연어는 사실 policy 기반으로 하기엔 힘들다 -> phrase structure grammar

* 지배소를 찾아야함

* 지배소 -> 밥을 먹었다 -> 먹었다 

* nltk 한번 해보기

* wordnet -> 잘되어있음 한번 확인해봥 단어의 관계를 알려줌


> 07.06.2017

### 기말준비

## NLP

* 형태소 분석, 구문 분석, 의미 분석 등 다양한 분석을 통해서 자연어의 의미를 컴퓨터에 이해시키도록 하는 학문

## 빅데이터 분석

* 매우 큰 데이터를 통해서 그 안에 담긴 의미를 찾아내는 학문

## 텍스트마이닝

* 데이터에서 관계형성의 규칙을 찾아내어서 관계 데이터를 추출해내는 학문

## 머신러닝

* 기계학습

## Stemming

* 주어진 단어의 형태적 근원을 결정하는 프로그램 또는 알고리즘

## wordcount

* 걍 워드 숫자 세는거

## Feature vector

* 무언가를 벡터화 시켰을때 이 오브젝트의 특징들을 가지는 vector

## TF-IDF (Term Frequency - Inverse Document Frequency)

* 정보 검색과 텍스트 마이닝에서 이용하는 가중치로, 여러 문서로 이루어진 문서군이 있을 때 어떤 단어가 특정 문서 내에서 얼마나 중요한 것인지를 나타내는 통계적 수치이다. 문서의 핵심어를 추출하거나 검색엔진에서 검색 결과의 순위를 결정하거나, 문서들 사이의 비슷한 정도를 구하는 등의 용도로 사용 할 수 있다.

## 벡터모델/확률모델

# 벡터모델

* 문헌과 질의등을 벡터공간으로 포팅하고 벡터간의 유사도를 산출하여 문서간의 관계도를 찾아낸다.

# 확률모델

* 정보의 색인과 검색의 문제를 확률적 관점에서 해석한 모델이다. 사용자의 쿼리가 주어졌을 때 확실한 연관된 문헌들의 집합이 존재하고 이를 이상적인 해답집합이라고 생각한다. 이런 모델은 2가지 중요한 기준을 가지는데 1. 각 문헌은 주어진 질의에 적합 혹은 부적합하다. 2. 한 문헌에 대한 적합성 판정은 다른 문헌의 적합성에 영향을 끼치지 않는다. 이 두가지 기준을 부합하며 이를 기준으로 확률이 가장 큰 문헌을 결과로 삼는 모델이다.

## 유사도 계산

# 유사도 지표의 속성

* 두 객체간 유사성은 둘이 공유하는 속성이 많을 수록 증가한다.

* 개별속성은 서로 독립이며, 추가가 가능하다.

* 각 속성이 갖는 추상화 레벨이 동일해야 한다.

* 유사성은 개념구조를 설명하는 데 충분해야한다.

를 기준으로 유사도를 계산하게 

## Text properties

## Zipf law

* 수학적 통계를 바탕으로 밝혀진 경험적 법칙으로, 물리 및 사회 과학 분야에서 연구된 많은 종류의 정보들이 지프 분포에 가까운 경향을 보인다는 것을 뜻함. 
* 지프의 법칙에 따르면 어떠한 자연어 말뭉치 표현에 나타나는 단어들을 그 사용 빈도가 높은 순서대로 나열하였을 때, 모든 단어의 사용 빈도는 해당 단어의 순위에 반비례한다.

## Mandelbrot set

* 복소수의 집합을 예측할 수 없지만 그려보면 그림 비슷한게 나옴 이걸 만델브로 집합이라고 부름
프랙탈

## Heaps's law

* 말뭉치의 크기를 늘려갈 수록 등장하는 토큰의 개수가 로그함수적으로 늘어간다는 법칙

## Link analysis

## PageRank

* www과 같은 하이퍼링크 구조를 가지는 문서에 상대적 중요도에 따라 가중치를 부여하는 방법

## 구글검색 엔진의 구조

## NLP tools

## sktlearn

## ngram Language Model

* 

## Deep Learning

## Word2Vec

* 워드를 벡터로 정리하는것

## word embedding

## POS tagging

* 형태소의 뜻과 문맥을 고려하여 그것에 마크업하는 일 ex) 가방에 들어가신다 -> 가방 + 에 + 들어가 + 시 + 다

## HMM ( 히든 마르코프 모델 )

* 통계적 마르코프 모델의 하나로써, 시스템이 은닉된 상태화 관찰가능한 결과의 두가지 요소로 이루어졌다고 보는 모델. 관찰 가능한 결과를 야기하는 직접적인 원인은 관찰될 수 없는 은닉 상태들이고, 오직 그 상태들이 마르코프 과정을 통해 도출된 결과만이 관찰될 수 있기 때문에 은닉이라는 단어가 붙었다. 

## MEMM

* 학습 할 알려지지 않은 값들이 조건부로 독립적인 것이 아니라 마르코프 연쇄로 연결되어 있다고 가정하고, 표준 최대 엔트로피 분류기를 확장하여 판별하는 모델입니다.

## EM ( 기댓값 최대화 알고리즘 )

* 관측되지 않는 잠재변수에 의존하는 확률 모델에서 최대가능도,최대사후확률을 갖는 매개변수를 찾는 반복적인 알고리즘

## 문서분류 기법

## SVM , CRF++

# SVM ( Support Vector Machine)

* 기계 학습의 분야 중 하나로 패턴 인식, 자료 분석을 위한 지도 학습 모델이며, 주로 분류와 회귀 분석을 위해 사용한다. 데이터를 비선형 맵핑을 통해서 고차원으로 변환한다.

## CRF++

# CRF ( Conditional random field ) 

* 통계적 모델링 방법중에 하나로, 패턴 인식과 기계 학습과 같은 구조적 예측에 사용된다. 레이블의 인접성에 대한 정보를 바탕으로 레이블을 추측하는 기계학습법 

* 하나의 sequence 를 보고 판단하는게 아니라 이전이나 이후의 sequence 를 보고 판단하는 것

# CRF++

* 소프트웨어

