
from app import current_app


app = current_app('development')


if __name__ == '__main__':
    app.run()
