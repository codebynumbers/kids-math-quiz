from random import randint
from operator import add, sub

num_questions = 10
correct = 0
wrong_list = []

def get_and_check(a, b, symbol, operation):
    answer = raw_input("{} {} {} = ".format(a, symbol, b))
    if answer == str(operation(a, b)):
        return 1, None
    else:
	return 0, "{} {} {} = {}, not {}".format(a, symbol, b, operation(a, b), answer)


for i in range(num_questions):
    a = randint(1, 10)
    b = randint(1, 10)
    result, wrong = get_and_check(a, b, '+', add)
    correct += result
    if wrong:
        wrong_list.append(wrong)


score = correct/float(num_questions) * 100

print "You got {} right out of {}, that's {:.0f}%\n".format(correct, num_questions, score)

if score == 100:
    print "Great job, you got them all right\n"
elif score >= 90:
    print "Pretty good, getting there\n"
elif score >= 80:
    print "Ok, keep practicing\n"
else:
    print "Not so good, keep trying, you'll get it.\n"

if score != 100:
    print "You got the following problems wrong:"
    for prob in wrong_list:
        print prob
