setwd('~/Documents/sandbox/advent')
text = readLines('dec6.txt')

count = 1
for (i in 1:nchar(text)-3) {
  s = substr(text, i, i+3)
  if (length(unique(unlist(strsplit(s, split = '')))) != 4)
    count = count + 1
  else {
    break
  }
}

print(paste("answer 1:", count))

answer_2 = 1
for (i in 1:nchar(text)-13) {
  s = substr(text, i, i+13)
  if (length(unique(unlist(strsplit(s, split = '')))) != 14)
    answer_2 = answer_2 + 1
  else {
    break
  }
}
print(paste("answer 2:", answer_2))
