import requests
import json
import time


def get_personalities(my_answer, gender):
    url = 'https://www.16personalities.com/test-results'
    url_api = 'https://www.16personalities.com/api/session'

    timestamp = time.strftime('%H-%M-%S', time.localtime())

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Referer": "https://www.16personalities.com/test-results",
        "sec-ch-ua": "'Chromium';v='106', 'Google Chrome';v='106', 'Not;A=Brand';v='99'",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "'Windows'",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        # "X-CSRF-TOKEN": "j2d9axGkWPQAe7pGBDuN8OTFEQ2jyzmj3feXKM0Z",
        "X-Requested-With": "XMLHttpRequest"
    }

    answers_json = {
        "questions": [
            {
                "text": "You regularly make new friends.",
                "answer": my_answer
            },
            {
                "text": "You spend a lot of your free time exploring various random topics that pique your interest.",
                "answer": my_answer
            },
            {
                "text": "Seeing other people cry can easily make you feel like you want to cry too.",
                "answer": my_answer
            },
            {
                "text": "You often make a backup plan for a backup plan.",
                "answer": my_answer
            },
            {
                "text": "You usually stay calm, even under a lot of pressure.",
                "answer": my_answer
            },
            {
                "text": "At social events, you rarely try to introduce yourself to new people and mostly talk to the ones you already know.",
                "answer": my_answer
            },
            {
                "text": "You prefer to completely finish one project before starting another.",
                "answer": my_answer
            },
            {
                "text": "You are very sentimental.",
                "answer": my_answer
            },
            {
                "text": "You like to use organizing tools like schedules and lists.",
                "answer": my_answer
            },
            {
                "text": "Even a small mistake can cause you to doubt your overall abilities and knowledge.",
                "answer": my_answer
            },
            {
                "text": "You feel comfortable just walking up to someone you find interesting and striking up a conversation.",
                "answer": my_answer
            },
            {
                "text": "You are not too interested in discussing various interpretations and analyses of creative works.",
                "answer": my_answer
            },
            {
                "text": "You are more inclined to follow your head than your heart.",
                "answer": my_answer
            },
            {
                "text": "You usually prefer just doing what you feel like at any given moment instead of planning a particular daily routine.",
                "answer": my_answer
            },
            {
                "text": "You rarely worry about whether you make a good impression on people you meet.",
                "answer": my_answer
            },
            {
                "text": "You enjoy participating in group activities.",
                "answer": my_answer
            },
            {
                "text": "You like books and movies that make you come up with your own interpretation of the ending.",
                "answer": my_answer
            },
            {
                "text": "Your happiness comes more from helping others accomplish things than your own accomplishments.",
                "answer": my_answer
            },
            {
                "text": "You are interested in so many things that you find it difficult to choose what to try next.",
                "answer": my_answer
            },
            {
                "text": "You are prone to worrying that things will take a turn for the worse.",
                "answer": my_answer
            },
            {
                "text": "You avoid leadership roles in group settings.",
                "answer": my_answer
            },
            {
                "text": "You are definitely not an artistic type of person.",
                "answer": my_answer
            },
            {
                "text": "You think the world would be a better place if people relied more on rationality and less on their feelings.",
                "answer": my_answer
            },
            {
                "text": "You prefer to do your chores before allowing yourself to relax.",
                "answer": my_answer
            },
            {
                "text": "You enjoy watching people argue.",
                "answer": my_answer
            },
            {
                "text": "You tend to avoid drawing attention to yourself.",
                "answer": my_answer
            },
            {
                "text": "Your mood can change very quickly.",
                "answer": my_answer
            },
            {
                "text": "You lose patience with people who are not as efficient as you.",
                "answer": my_answer
            },
            {
                "text": "You often end up doing things at the last possible moment.",
                "answer": my_answer
            },
            {
                "text": "You have always been fascinated by the question of what, if anything, happens after death.",
                "answer": my_answer
            },
            {
                "text": "You usually prefer to be around others rather than on your own.",
                "answer": my_answer
            },
            {
                "text": "You become bored or lose interest when the discussion gets highly theoretical.",
                "answer": my_answer
            },
            {
                "text": "You find it easy to empathize with a person whose experiences are very different from yours.",
                "answer": my_answer
            },
            {
                "text": "You usually postpone finalizing decisions for as long as possible.",
                "answer": my_answer
            },
            {
                "text": "You rarely second-guess the choices that you have made.",
                "answer": my_answer
            },
            {
                "text": "After a long and exhausting week, a lively social event is just what you need.",
                "answer": my_answer
            },
            {
                "text": "You enjoy going to art museums.",
                "answer": my_answer
            },
            {
                "text": "You often have a hard time understanding other people’s feelings.",
                "answer": my_answer
            },
            {
                "text": "You like to have a to-do list for each day.",
                "answer": my_answer
            },
            {
                "text": "You rarely feel insecure.",
                "answer": my_answer
            },
            {
                "text": "You avoid making phone calls.",
                "answer": my_answer
            },
            {
                "text": "You often spend a lot of time trying to understand views that are very different from your own.",
                "answer": my_answer
            },
            {
                "text": "In your social circle, you are often the one who contacts your friends and initiates activities.",
                "answer": my_answer
            },
            {
                "text": "If your plans are interrupted, your top priority is to get back on track as soon as possible.",
                "answer": my_answer
            },
            {
                "text": "You are still bothered by mistakes that you made a long time ago.",
                "answer": my_answer
            },
            {
                "text": "You rarely contemplate the reasons for human existence or the meaning of life.",
                "answer": my_answer
            },
            {
                "text": "Your emotions control you more than you control them.",
                "answer": my_answer
            },
            {
                "text": "You take great care not to make people look bad, even when it is completely their fault.",
                "answer": my_answer
            },
            {
                "text": "Your personal work style is closer to spontaneous bursts of energy than organized and consistent efforts.",
                "answer": my_answer
            },
            {
                "text": "When someone thinks highly of you, you wonder how long it will take them to feel disappointed in you.",
                "answer": my_answer
            },
            {
                "text": "You would love a job that requires you to work alone most of the time.",
                "answer": my_answer
            },
            {
                "text": "You believe that pondering abstract philosophical questions is a waste of time.",
                "answer": my_answer
            },
            {
                "text": "You feel more drawn to places with busy, bustling atmospheres than quiet, intimate places.",
                "answer": my_answer
            },
            {
                "text": "You know at first glance how someone is feeling.",
                "answer": my_answer
            },
            {
                "text": "You often feel overwhelmed.",
                "answer": my_answer
            },
            {
                "text": "You complete things methodically without skipping over any steps.",
                "answer": my_answer
            },
            {
                "text": "You are very intrigued by things labeled as controversial.",
                "answer": my_answer
            },
            {
                "text": "You would pass along a good opportunity if you thought someone else needed it more.",
                "answer": my_answer
            },
            {
                "text": "You struggle with deadlines.",
                "answer": my_answer
            },
            {
                "text": "You feel confident that things will work out for you.",
                "answer": my_answer
            }
        ],
        "gender": gender,
        "inviteCode": "",
        "teamInviteKey": "",
        "extraData": []
    }

    req = requests.post(url, headers=headers, json=answers_json)
    my_cookie = req.headers['set-cookie']
    my_cookie = my_cookie[my_cookie.find("testResults="):]

    testResults = my_cookie[:my_cookie.find("; expires")]

    headers_for_api = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        # "accept-encoding": "gzip, deflate, br",
        # "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "max-age=0",
        "cookie": testResults,
        "sec-ch-ua": "'Chromium';v='106', 'Google Chrome';v='106', 'Not;A=Brand';v='99'",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "'Windows'",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    }

    req = requests.get(url_api, headers=headers_for_api)

    response_dict = {}
    response_dict = json.loads(req.text)  # конвертировали ответ через json.loads к типу Dictionary

    try:
        response_dict = response_dict['user']  # оставили в ответе только ключ user
    except Exception:
        print('В ответе нет поля user')

    with open(f"user_info_{timestamp}.json", "w", encoding="utf-8") as file:
        json.dump(response_dict, file, indent=4, ensure_ascii=False)


def main():
    get_personalities(-2, "Female")


if __name__ == "__main__":
    main()
