> 03.16.2017

### applied natural language processing 발표  
ML 에서 feature 추출은 정보에서 특정 벡터를 추출하는 식  
영어는 비교적 쉽다.
words , phrases , word-level n-grams , character-level n-grams..

why we need feature select? 

we can extract meaningful data using feature


### task independent methods

  df란 
  based on zipf's law
  remove the rare items -> not useful its maybe noise
  plus : easy to compute , task independent
  minus : ad hoc criterion , rare terms can bo good discriminators
  얼마나 많이 나오나 
  
  tf란
  
  얼마나 자주 나오나
  
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

  
