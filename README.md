# Team Leave Scheduler

## Run it

1. Activate the virtual environment.
2. Run `python seed.py` to load sample employees, holidays, and requests.
3. Run `python app.py`.
4. Open `http://127.0.0.1:5000`.

## API

- `GET /api/leave-calendar`
- `POST /api/leave-requests`
- `POST /api/leave-requests/<id>/approve`
- `POST /api/leave-requests/<id>/reject`

## Tests

Run `python -m unittest discover`.
