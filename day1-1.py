# 연속 부분 수열 합의 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/131701

def solution(elements):
  answer = 0
  sum_set = set()
  
  for n in range(1, len(elements) + 1):
      # n개의 연속 부분 수열 구하기
      for index in range(len(elements)):
          end_index = index + n
          if end_index > len(elements):
              slice_list = elements[index:] + elements[0:abs(len(elements)-end_index)]
          else:
              slice_list = elements[index:end_index]
          
          sum_set.add(sum(slice_list))
          answer = len(sum_set)
      
  return answer


# 훨씬 빠르구나
def solution2(elements):
  answer = 0
  sum_set = set()
  
  for i in range(len(elements)):
      ssum = elements[i]
      sum_set.add(ssum)
      
      for j in range(i+1, len(elements) + i):
          ssum += elements[j % len(elements)]
          sum_set.add(ssum)
      
  answer = len(sum_set)
  
  return answer