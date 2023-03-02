# 크기가 작은 부분문자열
def solution(t, p):
  answer = 0

  for i in range(len(t)+1 - len(p)):
      partstr = t[i:i+len(p)]
      
      if int(partstr) <= int(p):
          answer += 1
  
  return answer