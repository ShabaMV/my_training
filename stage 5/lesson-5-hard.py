import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __str__(self):
        return self.lower()

    def __contains__(self, value):
        if value.lower() in self.lower():
            return True
        else:
            return False

    def __eq__(self, value):
        if isinstance(value, str) and self == value:
            return True
        else:
            return False

    def __init__(self):
        self.users = {}
        self.videos = {}
        self.current_user = None


    def log_in(self, nickname, password):
        if nickname in self.users and self.users[nickname].password == hash(password):
            self.current_user = nickname

    def log_out(self):
        self.current_user = None

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f"Пользователь {nickname} уже существует")
        else:
            self.users[nickname] = User(nickname, password, age)
            self.log_in(nickname,password)

    def add(self, *args):
        for video in args:
            if video.title not in self.videos:
                self.videos[video.title] = video

    def get_videos(self, search_request):
        result = []
        for video in self.videos:
            if search_request.lower() in video.lower():
                result.append(video)
        return result;

    def watch_video(self,video_to_play):
        if self.current_user == None:
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            for video in self.videos:
                if video_to_play == video:
                    if self.users[self.current_user].age <= 18:
                        print("Вам нет 18, пожалуйста покиньте страницу")
                    else:
                        for counter in range(0,self.videos[video].duration):
                            self.videos[video].time_now = counter + 1
                            time.sleep(1)
                            print(self.videos[video].time_now,end=' ')
                        print("Конец видео")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')