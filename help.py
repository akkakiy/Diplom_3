from faker import Faker


class RandomUser:
    @staticmethod
    def create_random_user():           # создание пользователя
        faker = Faker('ru_RU')
        user_data = {
            'email': faker.email(),
            'password': faker.password(),
            'name': faker.name()
        }
        return user_data
