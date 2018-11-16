from random import randint

num_questions = 10
correct = 0

for i in range(num_questions):
    a = randint(1, 10)
    b = randint(1, 10)
    if i % 2 == 0:
        if a < b:
            a, b = b, a
        answer = raw_input("{} - {} = ".format(a, b))
        if answer == str(a - b):
            correct += 1
    else:
        answer = raw_input("{} + {} = ".format(a, b))
        if answer == str(a + b):
            correct += 1
    score = correct/float(num_questions) * 100
print "You got {} right out of {}, that's {:.0f}%".format(correct, num_questions, score)
print

if score == 100:
    print "Great job, you got them all right"
elif score >= 90:
    print "Pretty good, getting there"
elif score >= 80:
    print "Ok, keep practicing"
else:
    print "Not so good, keep trying, you'll get it."

