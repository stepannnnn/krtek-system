# krtek-system
Simple fullstack web-based system to make sure everyone pays debs (drinks drunked, food eaten, gas driven etc.) to friends (I lost so much money already :(()

This is my first ever app created with django (so please dont be harsh), but I am open to objective feedback

##installation
1. install [Python](https://www.microsoft.com/store/productId/9NRWMJP3717K?ocid=pdpshare)
2. Dowland this directory as .zip and unzip it or clone this directory
3. Create venv in directory (.../krtek-system-main) [Tutorial here](https://docs.python.org/3/tutorial/venv.html)
4. run `pip install django` and `pip install decouple` in cmd repository folder
5. open .env.template inside project, insert your django secrete key from [https://djecrety.ir](https://djecrety.ir) and rename file to .env
6. inside project folder in cmd run `python manage.py createsuperuser` and enter info for admin account
7. run `python manage.py runserver`
8. go to your favorite browser to url [https://127.0.0.1:8000](https://127.0.0.1:8000)
9. To manage what items you offer and guest list, go to [https://127.0.0.1:8000/admin](https://127.0.0.1:8000/admin), log-in and simply odit database via admin UI (Guests, Items tables)


© Made by Štěpán Kobližka aka [stepannnnn](https://github.com/stepannnnn/). Use for personal or commercial use as you want. But I would relly be happy if you give me credit somewhere (Leave signiture in app/write it in menu or wherever you want. However, it is not mandatory.
