from lk.models import HADS_Result, HADS_Alarm


def process_HADS_test(survey_answer):
    survey = survey_answer.survey
    user = survey_answer.user
    summary = 0
    for answer in survey_answer.answers:
        if "Я испытываю напряжение, мне не по себе" in answer.question.question:
            if "все время" in answer.answer:
                summary += 3
            elif "часто" in answer.answer:
                summary += 2
            elif "время от времени, иногда" in answer.answer:
                summary += 1
            elif "совсем не испытываю" in answer.answer:
                summary += 0
        elif "Я испытываю страх, кажется, что что-то ужасное может вот-вот случиться" in answer.question.question:
            if "определенно это так, и страх очень велик" in answer.answer:
                summary += 3
            elif "да, это так, но страх не очень велик" in answer.answer:
                summary += 2
            elif "иногда, но это меня не беспокоит" in answer.answer:
                summary += 1
            elif "совсем не испытываю" in answer.answer:
                summary += 0
        elif "Беспокойные мысли крутятся у меня в голове" in answer.question.question:
            if "постоянно" in answer.answer:
                summary += 3
            elif "большую часть времени" in answer.answer:
                summary += 2
            elif "время от времени и не так часто" in answer.answer:
                summary += 1
            elif "только иногда" in answer.answer:
                summary += 0
        elif "Я легко могу присесть и расслабиться" in answer.question.question:
            if "совсем не могу" in answer.answer:
                summary += 3
            elif "лишь изредка, это так" in answer.answer:
                summary += 2
            elif "наверно, это так" in answer.answer:
                summary += 1
            elif "определенно, это так" in answer.answer:
                summary += 0
        elif "Я испытываю внутреннее напряжение или дрожь" in answer.question.question:
            if "очень часто" in answer.answer:
                summary += 3
            elif "часто" in answer.answer:
                summary += 2
            elif "иногда" in answer.answer:
                summary += 1
            elif "совсем не испытываю" in answer.answer:
                summary += 0
        elif "Я испытываю неусидчивость, мне постоянно нужно двигаться" in answer.question.question:
            if "определенно, это так" in answer.answer:
                summary += 3
            elif "наверно, это так" in answer.answer:
                summary += 2
            elif "лишь в некоторой степени, это так" in answer.answer:
                summary += 1
            elif "совсем не испытываю" in answer.answer:
                summary += 0
        elif "У меня бывает внезапное чувство паники" in answer.question.question:
            if "очень часто" in answer.answer:
                summary += 3
            elif "довольно часто" in answer.answer:
                summary += 2
            elif "не так уж часто" in answer.answer:
                summary += 1
            elif "совсем не бывает" in answer.answer:
                summary += 0
    if summary <= 7:
        HADS_Result.objects.create(user=user, depression=0)
    elif 10 >= summary >= 8:
        HADS_Result.objects.create(user=user, depression=1)
    elif summary >= 11:
        HADS_Result.objects.create(user=user, depression=2)


def process_ALARM_test(survey_answer):
    survey = survey_answer.survey
    user = survey_answer.user
    summary = 0
    for answer in survey_answer.answers:
        if "То, что приносило мне большое удовольствие, и сейчас вызывает у меня такое же чувство" in answer.question.question:
            if "это совсем не так" in answer.answer:
                summary += 3
            elif "лишь в очень малой степени, это так" in answer.answer:
                summary += 2
            elif "наверное, это так" in answer.answer:
                summary += 1
            elif "определенно, это так" in answer.answer:
                summary += 0
        elif "Я способен рассмеяться и увидеть в том или ином событии смешное" in answer.question.question:
            if "совсем не способен" in answer.answer:
                summary += 3
            elif "лишь в очень малой степени, это так" in answer.answer:
                summary += 2
            elif "наверное, это так" in answer.answer:
                summary += 1
            elif "определенно, это так" in answer.answer:
                summary += 0
        elif "Я испытываю бодрость" in answer.question.question:
            if "совсем не испытываю" in answer.answer:
                summary += 3
            elif "очень редко" in answer.answer:
                summary += 2
            elif "иногда" in answer.answer:
                summary += 1
            elif "практически все время" in answer.answer:
                summary += 0
        elif "Мне кажется, что я стал все делать очень медленно" in answer.question.question:
            if "практически все время" in answer.answer:
                summary += 3
            elif "часто" in answer.answer:
                summary += 2
            elif "иногда" in answer.answer:
                summary += 1
            elif "совсем нет" in answer.answer:
                summary += 0
        elif "Я не слежу за своей внешностью" in answer.question.question:
            if "определенно, это так" in answer.answer:
                summary += 3
            elif "я не уделяю этому столько времени, сколько нужно" in answer.answer:
                summary += 2
            elif "может быть, я стал меньше уделять этому времени" in answer.answer:
                summary += 1
            elif "я слежу за собой так же, как и раньше" in answer.answer:
                summary += 0
        elif "Я считаю, что мои дела (занятия, увлечения) могут принести мне чувство удовлетворения" in answer.question.question:
            if "совсем так не считаю" in answer.answer:
                summary += 3
            elif "значительно меньше, чем обычно" in answer.answer:
                summary += 2
            elif "да, но не в той степени, как раньше" in answer.answer:
                summary += 1
            elif "точно так же, как и обычно" in answer.answer:
                summary += 0
        elif "Я могу получить удовольствие от хорошей книги, радио- или телепрограммы" in answer.question.question:
            if "очень редко" in answer.answer:
                summary += 3
            elif "редко" in answer.answer:
                summary += 2
            elif "иногда" in answer.answer:
                summary += 1
            elif "часто" in answer.answer:
                summary += 0
    if summary <= 7:
        HADS_Alarm.objects.create(user=user, depression=0)
    elif 10 >= summary >= 8:
        HADS_Alarm.objects.create(user=user, depression=1)
    elif summary >= 11:
        HADS_Alarm.objects.create(user=user, depression=2)


def process_test(survey_answer):
    """
    Processes string and addes statistics to Statistics object
    @param survey_answer: SurveyAnswer object
    @return:
    """
    if '№0' in survey_answer.survey.title:
        process_HADS_test(survey_answer)
    if '№1' in survey_answer.survey.title:
        process_ALARM_test(survey_answer)
