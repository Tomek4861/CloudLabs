# Photography Portfolio 

Simple photography portfolio application built with Django, used for practicing hosting and Dockerization. The site includes several pages: homepage, photo gallery, and a contact form.

## Technologies
- **Django 5.1.5**
- **Bootstrap 5.3**
- **Docker**
- **Vercel**
- **Gunicorn**

## Application Structure
- **Homepage** – portfolio landing page.
- **Portfolio** – a gallery with sample photographs.
- **Contact** – a contact form with backend data handling.

## Local Installation

1. Clone the repository:
```bash
git clone https://github.com/Tomek4861/CloudLabs.git
cd CloudLabs
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv .venv
.venv\Scripts\activate 
pip install -r requirements.txt
```

3. Run the application:
```bash
python manage.py runserver
```

4. Open in a browser:
```
http://localhost:8000
```

## Dockerization

Build and run the Docker container:

```bash
docker build -t chmury-app .
docker run -d -p 8000:8000 chmury-app
```

## Hosting on Vercel

The application is hosted on the Vercel platform:

**Link:** [https://chmury-lab.vercel.app/home](https://chmury-lab.vercel.app/home)

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
