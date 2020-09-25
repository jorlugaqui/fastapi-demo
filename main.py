import logging
import random

from fastapi import FastAPI

app = FastAPI()

log = logging.getLogger(__name__)
handler = logging.StreamHandler()
log.addHandler(handler)


STUDENTS_DB = [
    'Juan Guillermo',
    'Juan Ortiz',
    'Manuela Gonzalez',
    'Carolina Naranjo',
    'Valery Valuarte',
    'Diego Paez',
    'Arley Valencia',
    'Omar Meneses',
    'Fernando Barrera',
    'Sebastian Jaramillo',
]


@app.get('/api/v1/developers/')
async def get_developers():
    return {'developers': STUDENTS_DB}


@app.get('/api/v1/developers/random')
async def get_developers_random():
    return {
        'developer': random.choice(STUDENTS_DB)
    }


@app.get('/api/v1/developers/{index}')
async def get_developer_by_index(index: int):
    try:
        return {'developer': STUDENTS_DB[index]}
    except IndexError:
        log.warning('Defaulting to index 0: first developer in the list')
        return {'developer': STUDENTS_DB[0]}
