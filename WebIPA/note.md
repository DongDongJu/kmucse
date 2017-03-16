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

###카이제곱

학점이 있다. 자료구조가 있고 농구가 있을 떄 컴퓨터공학부 학생 100명의 자료구조 수업의 학점과 농구 학점의 연관성이 있을까? 
있다고 가정하면 연관성이 얼마나 있느냐? 자료구조랑 파이썬을 다시 예로보면 이전의 연관성보다 후의 연관성이 높지 않을까? 

###text categorization

linguistic features 와 non-linguistic features 로 나누어짐 후자는 폰트 문서 포맷 같은걸 의미



###Information gain
이 단어가 이 클래스에서 갖는 중요도를 계산 하겠다.
purity 를 계산하는 것

특정 키워드( feature ) 가 중요하냐 안중요하냐를 확인하기 위해서 이 feature 를 넣었을때와 뻇을때를 비교해서 feature 의 중요도를 구하는 방법

before 엔트로피 - after의 yes or no 엔트로피를 해서 구함

###Entropy
impurity 를 계산하는 것

###MEMM ( Maximum ent marcov model )
각자를 보는 것이 아니라 전체를 보는 것
전체적으로 엔트로피를 구했을때 달라지는 경우가 있음


make 파일이랑 라이브러리 만드는법 미리 공부해놔랑
python도 공부하쉠


[latent semantic indexing](http://jchern.tistory.com/19)
[Singular Value Decomposition](http://darkpgmr.tistory.com/106)
  
