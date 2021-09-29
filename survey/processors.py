from lk.models import HADS_Result, HADS_Alarm, SmileStats, ShwabStats, DailyActivityStats


def process_HADS_test(survey_answer):
    survey = survey_answer.survey
    user = survey_answer.user
    summary = 0
    for answer in survey_answer.answers.all():
        if "Я испытываю напряжение, мне не по себе" in answer.question.question:
            if "все время" in answer.answer:
                summary += 3
            elif "часто" in answer.answer:
                summary += 2
            elif "время от времени" in answer.answer or "иногда" in answer.answer:
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
        HADS_Result.objects.create(user=user, depression=0, value=summary)
    elif 10 >= summary >= 8:
        HADS_Result.objects.create(user=user, depression=1, value=summary)
    elif summary >= 11:
        HADS_Result.objects.create(user=user, depression=2, value=summary)


def process_ALARM_test(survey_answer):
    survey = survey_answer.survey
    user = survey_answer.user
    summary = 0
    for answer in survey_answer.answers.all():
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
        HADS_Alarm.objects.create(user=user, alarm=0, value=summary)
    elif 10 >= summary >= 8:
        HADS_Alarm.objects.create(user=user, alarm=1, value=summary)
    elif summary >= 11:
        HADS_Alarm.objects.create(user=user, alarm=2, value=summary)


def process_Smile_test(survey_answer):
    value = survey_answer.answers.all()[0].answer
    user = survey_answer.user
    SmileStats.objects.create(user=user, value=value)


def process_Shwab_test(survey_answer):
    value = survey_answer.answers.all()[0].answer
    percent = 0
    user = survey_answer.user
    if "Я полностью независим. Легко и быстро справляется с повседневными обязанностями. Жалобы отсутствуют" in value:
        percent = 100
    elif "Я полностью независим. Справляюсь с повседневными обязанностями, но более медленно. Нередко в 2 раза " \
         "медленнее, чем в норме. Появляются жалобы на трудность при выполнении повседневных дел." in value:
        percent = 90
    elif "Я полностью независим при выполнении большинства повседневных обязанностей, но трачу на них в 2 раза больше " \
         "времени, чем в норме. Осознаю, что стало сложнее выполнять работу." in value:
        percent = 80
    elif "Частично нуждаюсь в посторонней помощи. С большим трудом справляюсь с некоторыми повседневными " \
         "обязанностями. Трачу на них в 3-4 раза больше времени, чем обычно" in value:
        percent = 70
    elif "Нередко завишу от посторонней помощи. С большинством повседневных обязанностей справляюсь, но медленно, " \
         "прилагая значительные усилия и нередко с ошибками. Некоторые действия выполнить не могу." in value:
        percent = 60
    elif "Еще более зависим от посторонней помощи. Повседневные обязанности выполняю медленно, в половине случаев " \
         "нуждаюсь в посторонней помощи." in value:
        percent = 50
    elif "Зависим от посторонней помощи. Повседневные обязанности выполняю, но почти всегда с посторонней помощью." in value:
        percent = 40
    elif "С трудом выполняю (или начинает выполнять) лишь отдельные повседневные обязанности сам. Нуждаюсь в " \
         "значительной посторонней помощи." in value:
        percent = 30
    elif "Не в состоянии ничего сделать без посторонней помощи. Немного помогает ухаживающему персоналу. Тяжелая " \
         "инвалидизация." in value:
        percent = 20
    elif "Полностью зависим от посторонней помощи. Беспомощен. Полная инвалидизация." in value:
        percent = 10
    elif "Нарушаются вегетативные функции: глотание, мочеиспускание и дефекация" in value:
        percent = 0
    else:
        percent = -1
    ShwabStats.objects.create(user=user, value=percent)


def process_daily_activity_test(survey_answer):
    survey = survey_answer.survey
    user = survey_answer.user
    activity = DailyActivityStats()
    activity.user = user
    for answer in survey_answer.answers.all():
        if "Сколько часов вы Спали" in answer.question.question:
            activity.sleep_time = answer.answer
        elif "Сколько времени вы потратили на занятия физкультурой и спортом" in answer.question.question:
            activity.sport_time = answer.answer
        elif "Сколько времени вы потратили на работу" in answer.question.question:
            activity.work_time = answer.answer
        elif "Сколько времени Вы провели вне дома" in answer.question.question:
            activity.no_hom_time = answer.answer
    activity.save()


def process_PDQ_test(survey_answer):
    pass


def process_test(survey_answer):
    """
    Processes string and addes statistics to Statistics object
    @param survey_answer: SurveyAnswer object
    @return:
    """
    print(survey_answer.survey.title)
    if '№0' in survey_answer.survey.title:
        process_ALARM_test(survey_answer)
    elif '№1' in survey_answer.survey.title:
        process_HADS_test(survey_answer)
    elif '№8' in survey_answer.survey.title:
        process_Smile_test(survey_answer)
    elif '№2' in survey_answer.survey.title:
        process_Shwab_test(survey_answer)
    elif '№6' in survey_answer.survey.title:
        process_daily_activity_test(survey_answer)
    elif '№7' in survey_answer.survey.title:
        process_PDQ_test(survey_answer)
